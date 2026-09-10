from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv # Load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

model=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

#tool create

@tool
def multiply(a:int ,b:int)->int:
    '''Given two numbers a and b this tool returns their product'''
    return a*b

llm_with_tools=model.bind_tools([multiply])

result=llm_with_tools.invoke('can you multiply 3 with 10')

print(result.tool_calls)

print(multiply.invoke(result.tool_calls[0]['args']))
print(multiply.invoke(result.tool_calls[0]))  #returns tool message