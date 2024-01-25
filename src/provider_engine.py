from openai import OpenAI
from pydantic import BaseModel
from src.config import Config


class LLMProvider:
    def __init__(self, config: Config):
        self.url = config.url
        self.key = config.key
        self.model = config.selected_model

class Client:
    def __init__(self, provider: LLMProvider):
        self.provider = provider
        self.client = OpenAI(
        api_key=provider.key,
        base_url=provider.url
        )
    
    def prompt(self, prompt_text: str, full_response=False, json_mode=False):
        request_args = {
            "model": self.provider.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_text}
            ]
        }
        if json_mode:
            request_args["response_format"] = {"type": "json_object"}
        response = self.client.chat.completions.create(**request_args)
        if full_response:
            return response
        else:
            return response.choices[0].message.content
