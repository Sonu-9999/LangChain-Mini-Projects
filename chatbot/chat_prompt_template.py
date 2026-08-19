from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

chat_template=ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Please answer the following question: {question}'),
   
])

prompt=chat_template.invoke({'domain': 'AI', 'question': 'What is the difference between supervised and unsupervised learning?'})
print(prompt)