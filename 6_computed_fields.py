from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    contact_details:Dict[str,str]


    @computed_field
    @property
    def bmi(self)->float:
       bmi = self.weight / (self.height ** 2)
       return bmi



def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('bmi',patient.bmi)
    print('Updated')

patient_info={'name':'anveshaa','email':'abc@hdfc.com','age':'30','weight':75.2,'height':1.72,'married':True,
          'contact_details':{'phone':'78979873'} }

patient1=Patient(**patient_info)
update_patient_data(patient1)