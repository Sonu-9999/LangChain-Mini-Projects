from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 

load_dotenv()

llm= HuggingFaceEndpoint ( 
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

result=model.invoke("Write a poem about the moon")

print(result.content)