import imp
import openai

from settings import settings


class OpenAIClient(object):
    def __init__(self):
        openai.api_key = settings.openai_api_key

    def create(self, prompt: str) -> str:
        response = openai.Completion.create(
            engine='davinci',
            prompt=prompt,
            max_tokens=140,
            temperature=0.3,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response['choices'][0].text
