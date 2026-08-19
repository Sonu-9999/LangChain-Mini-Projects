from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
    
)

model= ChatHuggingFace(llm=llm)


#1st prompt->detailed report
template1= PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

template2= PromptTemplate(
    template="Write a 5 line summary on the following text: {text}",
    input_variables=['text']
)

prompt1=template1.invoke({'topic':'black holes'})
result=model.invoke(prompt1)

prompt2=template2.invoke({'text':result.content})
result2=model.invoke(prompt2)

print(result2.content)