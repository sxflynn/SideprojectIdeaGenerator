from src.provider_engine import LLMProvider, Client
from src.prompt_engine import PromptEngine
from src.config import Config

def run_prompt(unknown_tech, known_tech):
    config = Config("JanAi")
    provider = LLMProvider(config)
    client = Client(provider)
    generated_prompt = PromptEngine.prompt_project(known_tech,unknown_tech)
    response_content = client.prompt(generated_prompt, full_response=True)
    return response_content

def main():
    unknown_tech = ["Backend", "databases", "Java"]
    known_tech = ["Javascript", "React", "Typescript", "Vue"]
    response = run_prompt(unknown_tech, known_tech)
    print (response)

if __name__ == "__main__":
    main()
