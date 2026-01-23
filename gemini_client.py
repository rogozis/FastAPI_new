from google import genai

from config import settings

client = genai.Client(api_key=settings.gemini_api_key)

def get_answer_from_gemini(prompt: str):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )
    print(response.text)

if __name__ == "__main__":
    get_answer_from_gemini('Напиши сегодняшюю дату')