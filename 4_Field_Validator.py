from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    contact_details:Dict[str,str]

#decorator
#In this you tell apka decorator kis field me apply hoga
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains=['hdfc.com','icici.com','ac.in']
         #abc@gmail.com
         #after '@' evrything would be validated
        domain_name=value.split('@')[1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
#Patient name: Capital
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode='before')
    @classmethod

    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_info={'name':'anveshaa','email':'abc@hdfc.com','age':'30','weight':75.2,'married':True,
          'contact_details':{'phone':'78979873'} }

patient1=Patient(**patient_info)
update_patient_data(patient1)
