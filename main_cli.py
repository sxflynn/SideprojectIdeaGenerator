import json
from pydantic import BaseModel
from typing import List
from src.provider_engine import LLMProvider, Client
from src.prompt_engine import PromptEngine
from src.config import Config
from src.response_validator import ProjectResponse, validate_response

class TechList(BaseModel):
    unknown_tech: List[str]
    known_tech: List[str]
    topics: List[str]
    
def run_prompt(user_input:TechList) -> ProjectResponse:
    config = Config("OpenAI")
    provider = LLMProvider(config)
    client = Client(provider)
    prompt_engine = PromptEngine(user_input)
    system_message = prompt_engine.create_system_message()
    user_prompt = prompt_engine.create_prompt()
    response_content = client.prompt(user_prompt, system_message, full_response=False, json_mode=True)
    return response_content

def main():
    user_input = TechList(
        unknown_tech= ["Backend", "databases", "Java"],
        known_tech= ["Javascript", "React", "Typescript", "Vue"],
        topics= ["Dancing", "Cooking"]
    )
    response = run_prompt(user_input)
    print(validate_response(response))

if __name__ == "__main__":
    main()
