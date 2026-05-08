import os
from dotenv import load_dotenv

load_dotenv()

def load_config():
    """Load and validate environment variables."""
    required = [
        "OPENAI_API_KEY", "OPENAI_BASE_URL", "OPENAI_MODEL",
        "OPENAI_EMBEDDINGS_MODEL",
        "LANGCHAIN_API_KEY", "LANGCHAIN_PROJECT", "LANGCHAIN_ENDPOINT",
    ]
    for var in required:
        if not os.getenv(var):
            print(f"⚠️  Missing {var} in .env")
    
    print("✅ Config loaded successfully")
    print(f"   LangSmith project : {os.getenv('LANGCHAIN_PROJECT')}")
    print(f"   OpenAI endpoint   : {os.getenv('OPENAI_BASE_URL')}")
    print(f"   Default LLM model : {os.getenv('OPENAI_MODEL')}")
    print(f"   Embedding model   : {os.getenv('OPENAI_EMBEDDINGS_MODEL')}")

if __name__ == "__main__":
    load_config()