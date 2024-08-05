import os
from google.cloud import storage
from flask import Flask, request, jsonify
from gensim.models import KeyedVectors, FastText
import numpy as np
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

w2v_model = None
ft_model = None

def download_model_files(model_name, model_type):
    bucket_name = "zvirevo-bucket"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Define file lists for different model types
    if model_type == 'word2vec':
        files_to_download = [f"{model_name}"]
    elif model_type == 'fasttext':
        files_to_download = [
            f"{model_name}",
            f"{model_name}.syn1neg.npy",
            f"{model_name}.wv.vectors_ngrams.npy",
            f"{model_name}.wv.vectors_vocab.npy"
        ]
    else:
        raise ValueError("Invalid model type. Expected 'word2vec' or 'fasttext'.")

    for file_name in files_to_download:
        destination_file_name = f"/tmp/{file_name}"
        blob = bucket.blob(file_name)
        blob.download_to_filename(destination_file_name)
        print(f"File {file_name} downloaded to {destination_file_name}")

    return f"/tmp/{model_name}"

def load_models():
    global w2v_model, ft_model
    
    logging.info("Starting to load models...")
    try:
        # Download and load Word2Vec model
        logging.info("Downloading Word2Vec model...")
        w2v_model_path = download_model_files("word2vec.bin", 'word2vec')
        logging.info(f"Word2Vec model downloaded to {w2v_model_path}")
        logging.info("Loading Word2Vec model...")
        w2v_model = KeyedVectors.load_word2vec_format(w2v_model_path, binary=True)
        logging.info("Word2Vec model loaded successfully")
        
        # Download and load FastText model
        logging.info("Downloading FastText model...")
        ft_model_path = download_model_files("fasttext_shona.bin", 'fasttext')
        logging.info(f"FastText model downloaded to {ft_model_path}")
        logging.info("Loading FastText model...")
        ft_model = FastText.load(ft_model_path)
        logging.info("FastText model loaded successfully")
        
        logging.info("All models loaded successfully")
    except Exception as e:
        logging.error(f"Error loading models: {str(e)}")
        logging.error(f"Error details: {type(e).__name__}")

# Load models when the application starts
load_models()

@app.route('/health')
def health_check():
    if w2v_model is None or ft_model is None:
        return jsonify({'status': 'Models not loaded'}), 503
    return jsonify({'status': 'healthy'}), 200

@app.route('/')
def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Zvirevo API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                text-align: center;
            }
            h1 {
                color: #2c3e50;
                margin-bottom: 20px;
            }
            p {
                margin-bottom: 15px;
            }
            a {
                color: #3498db;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Zvirevo API!</h1>
        <p>Developed by <strong>Daisy Tsenesa</strong> and <strong>Ruvarashe Sadya</strong> as part of a word embeddings project for Shona.</p>
        <p>We used both FastText and Word2Vec models.</p>
        <p>Check us out on GitHub:</p>
        <p>Daisy Tsenesa: <a href='https://github.com/daisy-py-bot'>https://github.com/daisy-py-bot</a></p>
        <p>Ruvarashe Sadya: <a href='https://github.com/RuvaS20'>https://github.com/RuvaS20</a></p>
    </body>
    </html>
    """
    return html_content

@app.route('/similar', methods=['POST'])
def get_similar_words():
    if w2v_model is None or ft_model is None:
        return jsonify({'error': 'Models not loaded yet. Please try again later.'}), 503

    data = request.json
    word = data['word']
    model_type = data.get('model', 'word2vec')
    model = w2v_model if model_type == 'word2vec' else ft_model

    try:
        if model_type == 'word2vec':
            similar_words = model.most_similar(word, topn=10)
        else:
            similar_words = model.wv.most_similar(word, topn=10)
        return jsonify({'similar_words': similar_words})
    except KeyError:
        return jsonify({'error': f"Word '{word}' not found in vocabulary"}), 400
    except Exception as e:
        app.logger.error(f"Unexpected error in get_similar_words: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/analogy', methods=['POST'])
def get_analogy():
    if w2v_model is None or ft_model is None:
        return jsonify({'error': 'Models not loaded yet. Please try again later.'}), 503

    data = request.json
    word1 = data['word1']
    word2 = data['word2']
    word3 = data['word3']
    model_type = data.get('model', 'word2vec')
    model = w2v_model if model_type == 'word2vec' else ft_model

    try:
        if model_type == 'word2vec':
            result = model.most_similar(positive=[word2, word3], negative=[word1], topn=1)
        else:
            result = model.wv.most_similar(positive=[word2, word3], negative=[word1], topn=1)
        return jsonify({'result': result[0]})
    except KeyError as e:
        return jsonify({'error': f"Word not found in vocabulary: {str(e)}"}), 400
    except Exception as e:
        app.logger.error(f"Unexpected error in get_analogy: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
