from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv # Load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

model=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

@tool
def multiply(a:int,b:int) ->int:
    '''Given 2 numbers a and b this tool returns their product'''
    return a*b

query=HumanMessage('can you multiply 3 with 10')
llm_with_tools=model.bind_tools([multiply])
messages=[query]

result=llm_with_tools.invoke(messages)
#append Humanmessage and AI message
messages.append(result)
#executes logic of multiply function by extracting the tool_call subsection in the ai message
tool_result=multiply.invoke(result.tool_calls[0])

messages.append(tool_result)



print(llm_with_tools.invoke(messages).text)