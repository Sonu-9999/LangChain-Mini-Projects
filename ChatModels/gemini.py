from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv # Load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

Chat=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

result=Chat.invoke("What is the capital of India?")

print(result.content)