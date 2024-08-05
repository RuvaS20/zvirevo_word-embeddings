# Zvirevo: Shona Language Word Embeddings

Zvirevo is a project aimed at bridging the digital divide for Shona speakers through advanced natural language processing techniques. We've developed word embeddings for the Shona language using Word2Vec and FastText models, enabling powerful word similarity and analogy calculations.

## Creators

This project was developed by:

- **Daisy Tsenesa**
- **Ruvarashe Sadya**

## Key Features

- Word embeddings for the Shona language
- Trained using Word2Vec and FastText algorithms
- Supports word similarity calculations
- Enables analogy computations (e.g., "mambo" - "murume" + "mukadzi" = "mambokadzi")
- API deployed on Google Cloud Run for easy integration

## Demo

Check out our video demonstration to see Zvirevo in action:

[Zvirevo Demo Video](https://www.youtube.com/watch?v=your-video-id)

This video showcases the capabilities of our Shona word embeddings and how to use the API.

## Data Sources

Our word embeddings were trained on a corpus of Shona text collected from various sources:

1. Shona Dictionary: A comprehensive source of formal Shona text.
2. [Shona Language Corpus](https://wortschatz.uni-leipzig.de/en/download/Shona#sna-zw_web_2016): Kwayedza news articles and randomly chosen websites covering a wide range of topics in Shona.
3. [Belebele Dataset](https://paperswithcode.com/dataset/belebele): A multiple-choice machine reading comprehension (MRC) dataset spanning 122 language variants.
4. VOA News: A collection of Shona news articles and short stories.
5. Shona Bible and Quran

We are grateful to these sources for providing the rich textual data necessary for training our models.

## Why Zvirevo?

Shona, spoken by over 80% of Zimbabwe's population, is underrepresented in modern NLP technologies. Zvirevo aims to change that by providing foundational NLP resources for Shona, paving the way for more advanced applications like chatbots and virtual assistants in the future.

## Usage

Our API allows developers to easily integrate Shona language processing into their applications. Use it for:

- Improving search relevance for Shona content
- Enhancing machine translation systems
- Developing educational tools for Shona language learners
- Powering recommendation systems for Shona-language e-commerce platforms

## API Documentation

The Zvirevo API is accessible at: `https://word2vec-app-tk6uqeiatq-uc.a.run.app/`

### Endpoints

1. Word Similarity
   - Endpoint: `/similar`
   - Method: POST
   - Request Body:
     ```json
     {
       "word": "baba",
     }
     ```
   - Response:
     ```json
     {
       "similar words: [["tete", 0.83], ["vamwene", 0.81]]"
     }
     ```

2. Word Analogy
   - Endpoint: `/word-analogy`
   - Method: POST
   - Request Body:
     ```json
     {
       "word1": "mambo",
       "word2": "murume",
       "word3": "mukadzi"
     }
     ```
   - Response:
     ```json
     {
       "result": "mambokadzi"
     }
     ```

### Example Usage

Using Python with the `requests` library:

```python
import requests

API_URL = "https://word2vec-app-tk6uqeiatq-uc.a.run.app/"

# Word Similarity
similarity_response = requests.post(f"{API_URL}/similar", json={
    "word": "murume"
})
print(similarity_response.json())

# Word Analogy
analogy_response = requests.post(f"{API_URL}/word-analogy", json={
    "word1": "mambo",
    "word2": "murume",
    "word3": "mukadzi"
})
print(analogy_response.json())
```

## Installation and Setup

### Prerequisites

- Python 3.7+
- pip
- Docker (for containerization)
- Google Cloud SDK (for deployment to Google Cloud Run)

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/your-username/zvirevo_word-embeddings.git
   cd zvirevo
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application locally:
   ```
   python app.py
   ```

The application should now be running on `http://localhost:5000`.

### Deployment to Google Cloud Run

1. Build the Docker image:
   ```
   docker build -t gcr.io/main-duality-431514-n3/word2vec-app .
   ```

2. Push the image to Google Container Registry:
   ```
   docker push gcr.io/main-duality-431514-n3/word2vec-app
   ```

3. Deploy to Cloud Run:
   ```
   gcloud run deploy --image gcr.io/main-duality-431514-n3/word2vec-app --platform managed
   ```

Follow the prompts to complete the deployment. Once finished, Google Cloud Run will provide a URL where your application is accessible.

## Future Directions

While currently focused on word embeddings, we envision Zvirevo as a stepping stone towards more complex NLP tasks in Shona, including sentiment analysis, named entity recognition, and, eventually, full-fledged conversational AI.

## Contributing

We welcome contributions! Email us at daisykudzaitsenesa@gmail.com and ruvarashe.sadya@gmail.com for Daisy and Ruvarashe, respectively.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Join us in our mission to bring the Shona language into the digital age!
