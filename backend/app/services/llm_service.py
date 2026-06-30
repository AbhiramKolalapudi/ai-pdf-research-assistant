from google import genai
from google.genai import types

from app.models.prompt import Prompt
from app.settings import settings


class LLMService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def generate(
        self,
        prompt: Prompt
    ) -> str:

        response = self.client.models.generate_content(
            model=settings.llm_model,
            contents=prompt.user,
            config=types.GenerateContentConfig(
                system_instruction=prompt.system,
                temperature=settings.temperature,
            )
        )

        return response.text