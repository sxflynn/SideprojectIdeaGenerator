import os
from typing import List
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import ValidationError
import pydantic
from dotenv import load_dotenv
from src.provider_engine import LLMProvider, Client
from src.prompt_engine import PromptEngine
from src.config import Config
from src.response_validator import ProjectResponse, TechList, validate_response


load_dotenv()
dev_mode = os.getenv("DEV_MODE", "false").lower() == "true"
limiter_enabled = not dev_mode

limiter = Limiter(key_func=get_remote_address, enabled=limiter_enabled)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/prompt")
@limiter.limit("5/minute")
async def run_prompt(user_input:TechList, request: Request) -> ProjectResponse:
    print(user_input)
    print(request.client)
    config = Config("JanAi")
    provider = LLMProvider(config)
    client = Client(provider)
    prompt_engine = PromptEngine(user_input)
    system_message = prompt_engine.create_system_message(json=False)
    user_prompt = prompt_engine.create_prompt()
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        try:
            system_message = prompt_engine.create_system_message(json=False)
            response_content = client.prompt(user_prompt, system_message, full_response=False, json_mode=False)
            parsed_response: ProjectResponse = validate_response(response_content)
            return parsed_response
        except pydantic.ValidationError as e:
            attempts += 1
            if attempts == max_attempts:
                raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail="An error occurred while processing the prompt.")

@app.post("/test")
@limiter.limit("5/minute")
async def test(user_input:TechList, request: Request) -> ProjectResponse:
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
