# Translation API

A FastAPI-based translation API that uses OpenAI's GPT-4 to translate text into different languages.

## Features

- Text translation to any language using two-letter language codes
- Swagger documentation
- OpenAI GPT-4 integration
- Simple REST API interface

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```bash
   cp .env.example .env
   ```
5. Edit `.env` and add your OpenAI API key

## Running the API

Run the API using uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Access the Swagger documentation at `http://localhost:8000/docs`

## API Endpoints

### POST /translate

Translates text to the specified target language.

Request body:

```json
{
  "text": "Hello, how are you?",
  "target_language": "es"
}
```

Response:

```json
{
  "translated_text": "¡Hola, cómo estás?",
  "source_text": "Hello, how are you?",
  "target_language": "es"
}
```

Common language codes:

- es: Spanish
- fr: French
- de: German
- it: Italian
- pt: Portuguese
- nl: Dutch
- ru: Russian
- ja: Japanese
- ko: Korean
- zh: Chinese
