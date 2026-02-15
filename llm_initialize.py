import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

#LLM

llm = init_chat_model(
    model="gpt-4o-mini",
    model_provider="azure_openai",
    azure_deployment="gpt-4o-mini",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"))