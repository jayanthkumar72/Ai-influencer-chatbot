from langchain_community.llms import Ollama
from config import Config

def get_llm():
    return Ollama(model=Config.OLLAMA_MODEL)