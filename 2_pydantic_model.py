from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

#Type validation
# By default all the fiels are req
#but when you make a field optional then it's not req
#Data Validation : Fields which are coming are correct
#Field can specify the owrd limit or any constarinits but other than that 
#It can also attach description to the fields(metadata) & using Annotated
    name:Annotated[str,Field(max_length=50,title='Name of the patient',
            description='Give the name of patient in less than 50 words' ,examples='anvesha')]
    #Data validation ->there's a certain format for email & url
    email : EmailStr
    linkedin : AnyUrl 
    #custom data validation
    age:int=Field(gt=0,lt=120)
    #Constraint lag g ya koi bhi weight ki value 0 se kam nahi set kar skta
    #strict =True : Type version matt karne dena
    weight:Annotated[float,Field(gt=0,strict=True)]
    #can also attach default val
    married:Annotated[bool,Field(default=None,description='Is the patient married or not')]
#allergies is a list containing integer
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details : Dict[str,str]

#patient obj->Patient class
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('Inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_info={'name':'anveshaa','email':'abc@gmail.com','linkedin':'https://www.linkedin.com/in/anvesha-rastogi-905535311?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BBGEtFnByQgqGXHeKyKGCqQ%3D%3D','age':30,'weight':75.2,'married':True,
          'contact_details':{'email':'abc@gmail.com','phone':'78979873'}   }

#object
patient_1=Patient(**patient_info)#Since it's a dict you'll need to unpack it

insert_patient_data(patient_1)
update_patient_data(patient_1)





