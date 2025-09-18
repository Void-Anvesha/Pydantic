from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict,Optional,Annotated

#we'll perform model validation on:
#if age>60 ask emergency number

class Patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    contact_details:Dict[str,str]

#you're working on all the fields of class so no need to specify field
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
       if model.age>60 and 'emergency' not in model.contact_details:
           raise ValueError('Patients older than 60 must have an emergency contact')
       return model



def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_info={'name':'anveshaa','email':'abc@hdfc.com','age':65,'weight':75.2,'married':True,
          'contact_details':{'phone':'78979873','emergency':'2235243'} }

patient1=Patient(**patient_info)
update_patient_data(patient1)