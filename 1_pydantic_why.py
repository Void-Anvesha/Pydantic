def insert_patient_data(name:str,age:int):
  

    print(name)
    print(age)
    print('Insert into database')


#Here our code is not following type validation as age should be an integer
#insert_patient_data('anvesha','twenty')

#1.How you can solve this issue ->Type hinting

"""def insert_patient_data(name:str,age:int):


    print(name)
    print(age)
    print('Insert into database')"""
insert_patient_data('nitish',20)

# 2. 
def insert_patient_data(name:str,age:int):

    if type(name)==str and type(age)==int:
       if age<0:
        raise ValueError('Age cant be negative')
       else:
        print(name)
        print(age)
        print('Inserted into database')
    else:
        raise TypeError('Incorrect data type')
insert_patient_data('nitish','30')


#Update
def update_patient_data(name:str,age:int):

    if type(name)==str and type(age)==int:

        print(name)
        print(age)
        print('Updated')
    else:
        raise TypeError('Incorrect data type')
update_patient_data('nitish','30')

#Prblm in the above code that it's not scalable for diff funcn you'll
#have to make changes in each one of them


