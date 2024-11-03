from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI
app = FastAPI(
    title="Translation API",
    description="API for translating text using GPT-4",
    version="1.0.0"
)

class TranslationRequest(BaseModel):
    text: str
    target_language: str  # Two-letter language code (e.g., 'es', 'fr', 'de')

class TranslationResponse(BaseModel):
    translated_text: str
    source_text: str
    target_language: str

@app.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    """
    Translate text to the specified target language.
    
    - **text**: The text to translate
    - **target_language**: Two-letter language code (e.g., 'es' for Spanish, 'fr' for French)
    """
    try:
        # Create system message for translation
        system_message = f"You are a translator. Translate the following text into {request.target_language}. Only respond with the translation, nothing else."
        
        # Call OpenAI API
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": request.text}
            ],
            temperature=0.3
        )

        # Extract translated text
        translated_text = response.choices[0].message.content.strip()

        return TranslationResponse(
            translated_text=translated_text,
            source_text=request.text,
            target_language=request.target_language
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Translation API. Use /docs for the Swagger documentation."}
