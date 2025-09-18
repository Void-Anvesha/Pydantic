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


#converts pydantic model obj into python dict
temp1=patient_1.model_dump()

#converting pydantic model obj into json
temp2=patient_1.model_dump_json()

print(temp1)
print(type(temp1))


print(temp1)
print(type(temp2))