from dotenv import load_dotenv
import os

load_dotenv()

class TinyLlamaJanAi:
    url = "http://localhost:1337/v1"
    model = "tinyllama-1.1b"
    key = "no-key-needed!"

class OpenAIAPI:
    url = "none"
    model = "none"
    key = "none"