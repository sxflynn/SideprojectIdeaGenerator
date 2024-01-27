> ## 🚧 This project is under active development. Please consider contributing!

# Side Project Idea Generator
Helps software development students generate project ideas based on their skills and interests. The final version of this product will run on the following stack:
 - Python/FastAPI for prompt-management and handling to LLM provider server
 - React front end with Mantine component library

## Requirements
 - At least one of the following:
   1. Fast computer with > 8GB of RAM to run the offline LLM inference server
      
      or
   1. An API key with one of the supported LLM services (see below)

- Python version 3.11 or greater installed


## LLM Setup
This package requires that you have an LLM inference server setup. [Jan](https://jan.ai) is a recommended desktop GUI application that runs an LLM inference on your computer, no internet connection needed. Ollama is another popular option, but its API is not directly compatible with the OpenAI python library and is therefore not supported at this time.


### Jan instructions
> ⚠️ The default model in JanAi, `phi-2-3b`, requires 8GB of RAM and closing all your other apps, otherwise your computer will grind to a halt.

Settings -> Model: choose Phi-2 3B Q8 (requires 8GB of RAM, closed applications, and a fast computer)

Settings -> Advanced: Enable API Server

### OpenAI / Anyscale / TogetherAi API
You can run this package using OpenAI's, AnyScale's, or TogetherAi's servers, but you will need to obtain an API key and add it in your `.env` file. See Step 6 below.

You can get [$25 in free credits with TogetherAi](https://docs.together.ai/docs/get-started), and [$10 in free credits from Anyscale](https://docs.endpoints.anyscale.com/) when you sign up for their services. No payment details needed.

## Installation
1. Install Python version >= 3.11
1. `git clone` the repo and `cd` into the project directory
2. Set up a virtual environment
```Shell
python3 -m venv .venv
```
4. Activate the virtual environment (macOS/Linux)
```Shell
source .venv/bin/activate
```
5. Install the requirements
```Shell
pip install -r requirements.txt
```
6. (*Optional*) Rename your `.env` file if you plan on using cloud LLMs
```Shell
mv .env.example .env
```
7. (*Optional*) Add your OpenAI/AnyScale keys to your `.env` file
8. (*Optional*) Open `main_cli.py` and switch your LLM provider from Jan to another listed in the `config.toml` file.
```Python
config = Config("JanAi") # Switch "JanAi" to "OpenAI" etc
```
8. Execute the CLI entrypoint
```Shell
python3 main_cli.py
```



## API Endpoints
`POST` `/prompt`

input: 
```json
{
    "unknown_tech": ["Backend", "databases", "Java"],
    "known_tech": ["Javascript", "React", "Typescript", "Vue"],
    "topics": ["Dancing", "Cooking"]
}
```
example response:
```json
{
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
```

# Todo list
### LLM Service
- [x] Build skeletal code for abstracting LLM providers and clients from OpenAI implementation 
- [x] Add multiple LLM API urls and models
- [x] Add Pydantic models and validation
- [x] Create toml file to store endpoint configs
- [x] Refactor `main_cli.py` to emulate a FastAPI entrypoint
- [x] Add Pydantic error handling
- [ ] Add retry logic for failed validation
- [ ] Convert `main_cli.py` to FastAPI `main.py`
- [ ] Add a mocking capability to ease frontend development

### Database
- [ ] Create caching schema

### Frontend
- [ ] Create blank React project with Vite
- [ ] Build barebones app shell with Mantine
- [ ] Create form elements with Mantine/Forms
- [ ] Create form elements with Mantine/Forms


# Contributing
Anyone is welcome to contribute bug fixes and ideas as an issue. Unless it's a quick fix or a documentation enhancement, please report your idea as an issue before submitting a PR.
