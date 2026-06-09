from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Person(BaseModel):
    name : str

#This throws Error
"""
new_person = {'name' : 23}

person = Person(**new_person)

"""

#This works fine
"""
new_person = {'name' : 'Ashu'}
person = Person(**new_person)

"""

#default value in pydantic, also optional in pydentic

class man(BaseModel):
    Name : str
    language : str = 'Hindi' #default val in case other not mentioned at runtime
    age : Optional[int] = 'None' 
    email : EmailStr # a special type defined to check for valid email types, error if wrong

"""
new_man = {'Name' : 'Ashu', 'email' = 'asta05@gmai.com'} #if not *@gmail.com it'll throw error
new_man2 = {'Name': 'Kaalu', 'age':34, 'language':'english'} #the key word names must exactly match with the class attributes
mann = man(**new_man)
mann2 = man(**new_man2)

print(mann)
print(mann2)

"""

#Coercing in pydantic:

"""
new_man = {'Name': 'Ajay', 'age' : '17'} #age type is int but assinging str '17', pydantic auto-converts
mann = man(**new_man)

print(type(mann.age)) #shows int
"""

#Pydantic field and email

class Employee(BaseModel):
    Name : str 
    language : str = Field(default = 'English', description = 'Language that the employee is most comfortable in. ' )
    age : Optional[int] = 'None' 
    email : EmailStr # a special type defined to check for valid email types, error if wrong


new_emp = {'Name': 'Ashutosh', 'age' : 22, 'email' : 'ash23s'} #throws an error
new_emp2 = {'Name': 'Ashutosh', 'age' : 22, 'email' : 'ash23@gmail.com'} 

'''
emp1 = Employee(**new_emp)
print(emp1)
''' 

emp2 = Employee(**new_emp2)
print(emp2)