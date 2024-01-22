from openai import OpenAI

class LLMProvider:
    def __init__(self, config):
        self.url = config.url
        self.key = config.key
        self.model = config.model

class Client:
    def __init__(self, provider):
        self.provider = provider
        self.client = OpenAI(
        api_key=provider.key,
        base_url=provider.url
        )
    
    def prompt(self, prompt_text,full_response=False):
        response = self.client.chat.completions.create(
            model=self.provider.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_text}
            ]
        )
        if full_response:
            return response
        else:
            return response.choices[0].message.content