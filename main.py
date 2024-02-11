from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.provider_engine import LLMProvider, Client
from src.prompt_engine import PromptEngine
from src.config import Config
from src.response_validator import ProjectResponse, TechList, validate_response

app = FastAPI()

@app.post("/prompt")
async def run_prompt(user_input:TechList) -> ProjectResponse:
    config = Config("TogetherAi")
    provider = LLMProvider(config)
    client = Client(provider)
    prompt_engine = PromptEngine(user_input)
    system_message = prompt_engine.create_system_message(json=False)
    user_prompt = prompt_engine.create_prompt()
    response_content = client.prompt(user_prompt, system_message, full_response=False, json_mode=False)
    parsed_response:ProjectResponse = validate_response(response_content)
    return parsed_response

@app.post("/test")
async def healthcheck(user_input:TechList) -> ProjectResponse:
    # Raw JSON data
    mock_response = {
    "project_title": "Dance Recipe App",
    "description": "An app that combines dancing and cooking by providing users with fun dance routines while preparing recipes, creating an interactive and enjoyable cooking experience.",
    "technical_requirements": [
        "Develop the app using React and Typescript for the frontend to ensure a robust and efficient user interface.",
        "Incorporate Vue.js for interactive and visually engaging dance routine display and user interaction.",
        "Utilize JavaScript for implementing audio playback functionality and dance routine synchronization with recipe steps."
    ],
    "user_stories": [
        "As a user, I can browse through a variety of recipes and select one to prepare.",
        "As a user, I can view and follow along with a dance routine that complements the cooking process for a selected recipe.",
        "As a user, I can pause, replay, or adjust the speed of the dance routine to match my preference and cooking pace.",
        "As a user, I can see the ingredients and cooking steps for a recipe while simultaneously watching and following the dance routine.",
        "As a user, I can track my progress and save my favorite recipes and dance routines for future use."
    ]
}
    project_response = ProjectResponse(**mock_response)   
    return project_response


app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
