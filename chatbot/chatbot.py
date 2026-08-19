from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

llm= HuggingFaceEndpoint ( 
    repo_id="empero-ai/Qwen3.8-9B:featherless-ai",
    task="text-generation",
    max_new_tokens=1024,
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)

chat_history=[
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user_input= input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)