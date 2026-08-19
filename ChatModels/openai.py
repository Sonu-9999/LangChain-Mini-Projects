from langchain_openai import ChatOpenAI
from dotenv import load_dotenv # Load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

Chat=ChatOpenAI(model="gpt-4")

result=Chat.invoke("Who is the prime minister of India")

print(result.content)