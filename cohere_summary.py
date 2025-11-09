# cohere_summary.py
import os
import cohere
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

co = cohere.Client(api_key)

def generate_cohere_summary(text, prompt):
    try:
        response = co.generate(
            model='command-r-plus',
            prompt=prompt + text,
            max_tokens=300,
            temperature=0.5
        )
        return response.generations[0].text
    except Exception as e:
        return f"Error during summary generation: {str(e)}"
