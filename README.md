# Zvirevo: Shona Language Word Embeddings

Zvirevo is a project aimed at bridging the digital divide for Shona speakers through advanced natural language processing techniques. We've developed word embeddings for the Shona language using Word2Vec and FastText models, enabling powerful word similarity and analogy calculations.

## Key Features

- Word embeddings for the Shona language
- Trained using Word2Vec and FastText algorithms
- Supports word similarity calculations
- Enables analogy computations (e.g., "man" is to "woman" as "king" is to "queen")
- API deployed on Google Cloud Run for easy integration

## Why Zvirevo?

Shona, spoken by over 80% of Zimbabwe's population, is underrepresented in modern NLP technologies. Zvirevo aims to change that by providing foundational NLP resources for Shona, paving the way for more advanced applications like chatbots and virtual assistants in the future.

## Usage

Our API allows developers to easily integrate Shona language processing into their applications. Use it for:

- Improving search relevance for Shona content
- Enhancing machine translation systems
- Developing educational tools for Shona language learners
- Powering recommendation systems for Shona-language e-commerce platforms

## Installation and Setup

### Prerequisites

- Python 3.7+
- pip
- Docker (for containerization)
- Google Cloud SDK (for deployment to Google Cloud Run)

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/your-username/zvirevo.git
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
   docker build -t gcr.io/[PROJECT-ID]/zvirevo .
   ```

2. Push the image to Google Container Registry:
   ```
   docker push gcr.io/[PROJECT-ID]/zvirevo
   ```

3. Deploy to Cloud Run:
   ```
   gcloud run deploy --image gcr.io/[PROJECT-ID]/zvirevo --platform managed
   ```

Follow the prompts to complete the deployment. Once finished, Google Cloud Run will provide a URL where your application is accessible.

## API Documentation

[Include details about your API endpoints, request/response formats, and example usage here]

## Future Directions

While currently focused on word embeddings, we envision Zvirevo as a stepping stone towards more complex NLP tasks in Shona, including sentiment analysis, named entity recognition, and eventually, full-fledged conversational AI.

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Join us in our mission to bring the Shona language into the digital age!
