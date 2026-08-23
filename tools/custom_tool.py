from langchain_core.tools import tool

#step1- create a function

def multiply(a,b):
    '''Multiply two numbers''' #adding docstring is highly recommended
    return a*b

#step2-> add type hints
def multiply(a:int, b:int) -> int :
    '''Multiply two numbers''' 
    return a*b

#step3-> add tool decorator

@tool
def multiply(a:int, b:int) -> int :
    '''Multiply two numbers''' 
    return a*b

result=multiply.invoke({"a":3,"b":5}) #as tool is a runnable
print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

print(multiply.args_schema.model_json_schema()) #jo info llm ko jata hai regarding the input information of this tool