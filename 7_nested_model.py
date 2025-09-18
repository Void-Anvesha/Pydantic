from pydantic import  BaseModel

#class for address
class Address(BaseModel):
    city:str
    state:str
    pin:str

#Patient can use the address model as a field 
class Patient(BaseModel):
    name:str
    gender:str
    age:int
    #address stores complex data
    address:Address


address_dict={'city':'gurgaon','state':'haryana','pin':'21203'}


address1=Address(**address_dict)

patient_dict={'name':'anvesha','gender':'female','age':20,'address':address1}
patient_1=Patient(**patient_dict)


print(patient_1)
print(patient_1.address.city)
