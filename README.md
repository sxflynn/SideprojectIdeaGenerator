# Side Project Idea Generator
Helps software development students generate project ideas based on their skills and interests. The final version of this product will run on the following stack:
 - Python/FastAPI for prompt-management and handling to LLM provider server
 - React front end with Mantine component library

## LLM Setup
This package requires that you have an LLM inference server setup. [Jan.ai](https://jan.ai) is a recommended desktop GUI application that runs an LLM inference with OpenAI API compatible server. Another application that does this is **GPT4All** although you'd have to change the port number in the code to make it work.

Model: TinyLlama Chat 1.1B Q4
About: TinyLlama is a tiny model with only 1.1B. It's a good model for less powerful computers.

### OpenAI API
You can run this package using OpenAI's servers, but you will need to obtain an API key and add it in the source code. Environment variables have not yet been implemented.

## Installation
1. Install Python version 3.11
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
6. Execute the CLI entrypoint
```Shell
python3 main_cli.py
```

# Contributing
Anyone is welcome to contribute bug fixes and ideas as an issue. Unless it's a quick fix or a documentation enhancement, please report your idea as an issue before submitting a PR.

# This project is under active development and is incomplete.
