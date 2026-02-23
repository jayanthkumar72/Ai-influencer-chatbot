from langchain_groq import ChatGroq
from config import Config

def get_llm():
    if not Config.GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set")

    return ChatGroq(
        model="llama3-70b-8192",
        groq_api_key=Config.GROQ_API_KEY,
        temperature=0.3
    )