from src.provider_engine import LLMProvider, Client
from src.prompt_engine import PromptEngine
from src.config import TinyLlamaJanAi


def run_prompt():
    provider = LLMProvider(TinyLlamaJanAi)
    client = Client(provider)
    unknown_tech = ["Backend", "databases", "Java"]
    known_tech = ["Javascript", "React", "Typescript", "Vue"]
    generated_prompt = PromptEngine.prompt_project(known_tech,unknown_tech)
    response_content = client.prompt(generated_prompt, full_response=True)
    print(response_content)

def main():
    run_prompt()

if __name__ == "__main__":
    main()
