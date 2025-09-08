from sqlalchemy.orm import Session
from core.config import settings

from openai import OpenAI
from core.prompts import STANDARD_STORY_PROMPT
from models.story import Story

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = settings.API_KEY
)
# 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
def generate_story (user_prompt:str) -> str:
    try:
        prompt = STANDARD_STORY_PROMPT
        response = client.chat.completions.create(
            model ="deepseek/deepseek-r1-0528:free",
            messages= [
                {"role":"system", "content": prompt},
                {"role":"user", "content": user_prompt}
            ], 
            temperature=0.8
        )
        story_text = response.choices[0].message.content.strip()
        return story_text
    except Exception as e:
        print(f" Error generating story: {e}")
        return "Sorry, I could not generate a story at the moment."