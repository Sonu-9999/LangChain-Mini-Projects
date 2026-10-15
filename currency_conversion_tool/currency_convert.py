from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import InjectedToolArg
from typing import Annotated
from dotenv import load_dotenv # Load environment variables from .env file
import json

load_dotenv()  # Load environment variables from .env file

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


llm= HuggingFaceEndpoint ( 
    repo_id="Qwen/Qwen3.8-27B:novita",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

#injectedtoolarg-> llm do not substitute values of your own here.. i will give the value from previous tool calls in runtime
@tool
def convert(base_currency_value:int, conversion_rate: Annotated[float, InjectedToolArg])->float:
    '''given a currency conversion rate this function calculates the target currency value from a given base currency value'''
    return base_currency_value*conversion_rate


@tool
def get_conversion_factor(base_currency:str,target_currency:str)->float:
    '''This function fetches the currency conversion factor between a given base currency
    and a target currency'''

    url=f'https://v6.exchangerate-api.com/v6/0f69d21b51c61324e0bfa351/pair/{base_currency}/{target_currency}'

    response=requests.get(url)
    return response.json()

#get_conversion_factor.invoke({'base_currency':'USD','target_currency':'INR'})

#tool binding
llm_with_tools=model.bind_tools([get_conversion_factor,convert])

messages= [HumanMessage(
    content="What is the conversion factor between USD and INR?"
     " and based on that, convert 100 USD to INR"
    )]

ai_message=llm_with_tools.invoke(messages)

messages.append(ai_message)

tool_message1=get_conversion_factor.invoke(ai_message.tool_calls[0])

#json.loads() converts the json to python object like dictionary
conversion_rate=json.loads(tool_message1.content)['conversion_rate']

messages.append(tool_message1)

ai_message2=llm_with_tools.invoke(messages)
print(ai_message2.tool_calls)
print(ai_message2.content)