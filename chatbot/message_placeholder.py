from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

#chat template
chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
   
])
chat_history=[]
#load chat history from a file-> previously saved chat history usually saved in a database
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

#create prompt 
prompt=chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund?'})

print(prompt)