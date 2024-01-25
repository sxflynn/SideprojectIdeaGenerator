# Side Project Idea Generator
Helps software development students generate project ideas based on their skills and interests. The final version of this product will run on the following stack:
 - Python/FastAPI for prompt-management and handling to LLM provider server
 - React front end with Mantine component library

## LLM Setup
This package requires that you have an LLM inference server setup. [Jan](https://jan.ai) is a recommended desktop GUI application that runs an LLM inference with OpenAI API compatible server on your computer. Ollama is another popular option, but its API is not directly compatible with the OpenAI python library and is therefore not supported at this time.

### Jan settings
Settings -> Model: TinyLlama Chat 1.1B Q4 (or a more powerful model if your computer has a lot of RAM)
Settings -> Advanced: Enable API Server

### OpenAI / Anyscale API
You can run this package using OpenAI's or AnyScale's servers, but you will need to obtain an API key and add it in your `.env` file.

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

# Contributing
Anyone is welcome to contribute bug fixes and ideas as an issue. Unless it's a quick fix or a documentation enhancement, please report your idea as an issue before submitting a PR.

# This project is under active development and is incomplete.
