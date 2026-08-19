from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10) #checks if the cgpa is within the range of 0 to 10, if not it will throw error

new_student= {'name':'John',#if we do not pass string it will throw error
              'age': '20',  #pydantic will automatically convert the string to int->type coercing
              'email': 'john@example.com',#checks if the email is valid or not
              'cgpa': 8
              } 
student=Student(**new_student) # ** is dictionary unpacking operator

dict_student=dict(student) #converts the pydantic model to dictionary

print(student)
print(dict_student['email'])