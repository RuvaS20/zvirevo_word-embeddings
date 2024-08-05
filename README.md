## Video Demo:
[https://www.youtube.com/results?search_query=zvirevo+project]


# Zvirevo: Shona Language Word Embeddings

Zvirevo is a project aimed at bridging the digital divide for Shona speakers through advanced natural language processing techniques. We've developed word embeddings for the Shona language using Word2Vec and FastText models, enabling powerful word similarity and analogy calculations.

![image](https://github.com/user-attachments/assets/7b4f953b-bb3f-4cbd-80d3-970323d11758)



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
       "word": "baba"
     }
     ```
   - Response:
     ```json
     {
       "similar words": "[["tete", 0.83], ["vamwene", 0.81]]"
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


## Flask App Documentation


### Features

- Retrieve similar words using Word2Vec or FastText models.
- Compute word relationships based on provided expressions.
- Send email notifications via a contact form.

### Installation

1. **Clone the repository:**
   ```bash
   git lfs install
   git clone [https://huggingface.co/yourusername/your-repo-name](https://huggingface.co/dkt-py-bot/zvirevo_word2vec)
   cd zvirevo_word2vec
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download and place your pre-trained models:**
   - Place your Word2Vec model (`w2v_shona2.model`) and FastText model (`ft_model1.model`) in the project directory.

5. **Configure Flask-Mail:**
   - Update the email configuration in the `app.py` file with your email credentials.

### Usage

1. **Run the Flask app:**
   ```bash
   flask run
   ```

2. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

### Endpoints

#### Home

- **URL:** `/`
- **Method:** `GET`
- **Description:** Renders the home page.

#### Get Similar Words

- **URL:** `/get_similar_words`
- **Method:** `POST`
- **Description:** Retrieves similar words using the selected model.
- **Request Body:**
  ```json
  {
    "word": "example",
    "model_type": "word2vec",
    "top_n": 10
  }
  ```
- **Response:**
  ```json
  {
    "similar_words": [["word1", 0.85], ["word2", 0.80], ...]
  }
  ```

#### Compute Word Relationships

- **URL:** `/compute`
- **Method:** `POST`
- **Description:** Computes word relationships based on provided expressions.
- **Request Body:**
  ```json
  {
    "expression": "mwana - vakomana + vasikana",
    "model": "word2vec",
    "top_n": 5
  }
  ```
- **Response:**
  ```json
  {
    "result": [{"word": "mukadzi", "similarity": 0.85}, ...]
  }
  ```

#### Submit Contact Form

- **URL:** `/submit`
- **Method:** `POST`
- **Description:** Sends an email notification with the contact form details.
- **Form Data:**
  - `name`
  - `email`
  - `message`
  - `subscribe`
- **Response:**
  ```json
  {
    "status": "success",
    "message": "Your message has been received and the email has been sent!"
  }
  ```

### Configuration

- **Email Configuration:** Update the email server, port, username, and password in the `app.py` file.

### Dependencies

- Flask
- Gensim
- Flask-Mail
- Numpy


## Future Directions

While currently focused on word embeddings, we envision Zvirevo as a stepping stone towards more complex NLP tasks in Shona, including sentiment analysis, named entity recognition, and, eventually, full-fledged conversational AI.

## Contributing

We welcome contributions! Email us at daisykudzaitsenesa@gmail.com and ruvarashe.sadya@gmail.com for Daisy and Ruvarashe, respectively.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/RuvaS20/zvirevo_word-embeddings/blob/main/GCP%20Deployment/LICENSE) file for details.

Join us in our mission to bring the Shona language into the digital age!
