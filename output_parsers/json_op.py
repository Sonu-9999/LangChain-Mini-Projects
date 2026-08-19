
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# llm=HuggingFacePipeline.from_model_id(    cannot follow instructions to give output in json very small parameter model
#     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
    
# )

# model= ChatHuggingFace(llm=llm)
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv # Load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

model=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

parser=JsonOutputParser()


template1= PromptTemplate(
    template="Give me the name, age and city of a fictional character \n {format_instruction}", #additional instructions sent with template and it is filled by json parser
    input_variables=[],
    partial_variables={"format_instruction":parser.get_format_instructions()} #partial variable because it is not filled during runtime, it is filled before it
)

prompt=template1.format()
print(prompt)

chain=template1 | model | parser

result=chain.invoke({})
print(result)
print(type(result))