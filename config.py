import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "vectorstore/index")