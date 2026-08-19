from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 

load_dotenv()

llm= HuggingFaceEndpoint ( 
    repo_id="empero-ai/Qwen3.8-9B:featherless-ai",
    task="text-generation",
    max_new_tokens=1024,
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)


messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me a joke")
]
result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)