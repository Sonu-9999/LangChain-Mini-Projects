from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from dotenv import load_dotenv # Load environment variables from .env file
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()  # Load environment variables from .env file

model=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class FeedBack(BaseModel):
    sentiment:Literal['positive','negative']=Field(description="Give the sentiment of the feedback")

parser=StrOutputParser()

parser2=PydanticOutputParser(pydantic_object=FeedBack)

#we structure the output using pydantic output parser so that result from the llm is consistent as our flow depends on it
prompt1= PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative: \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)
classifier_chain= prompt1 |model|parser2

prompt2= PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3= PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']

)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2|model|parser),
    (lambda x:x.sentiment=='negative', prompt3|model|parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain= classifier_chain | branch_chain

print(chain.invoke({'feedback':'This is a terrible phone'}))


chain.get_graph().print_ascii()