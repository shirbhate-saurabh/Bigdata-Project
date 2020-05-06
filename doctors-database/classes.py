r"""creating classes for doctor database in which base class is "Person" and other classes are
   "doctor", "patient", "appointment\""""

from collections import defaultdict
from datetime import datetime


class Person:
    
    def __init__(self,first_name,last_name,address):
        
        self.first_name = ['Saurabh','shreays',"Akshay","Ritesh"]
        
        self.last_name = ["S","Shirbhate","Kale","Shivkar"]
        
        self.address = ["panvel","ghatkopar","vashi","bhingari"]

        
class Doctor(Person):

    def doctor_id_generator():
        temp = defaultdict(lambda: len(temp) + 1)
        temp1 = [temp[ele] for ele in self.first_name]
        doctor_id = str(temp1)
        print(doctor_id)


class Patient(Person):

    def patient_id_generator():
        temp = defaultdict(lambda: len(temp) + 1000)
        temp1 = [temp[ele] for ele in self.first_name]
        patient_id = str(temp1)
        return patient_id

class Aappointment(Person):

    def appointment_id_generator():
        temp = datetime.now().timestatmp()
        temp1 = str(temp).replace('.','')
        appointment_id = temp1
        return appointment_id



a1 = Person("Rohan","Shirke","Nerul")
print("enter the first_name :")
a2 = input()
print("enter the last_name :")
a3 = input()
print("enter the address :")
a4 = input()
a1.first_name.append(a2)
a1.last_name.append(a3)
a1.address.append(a4)
print(a1.first_name)
print(a1.last_name)
print(a1.address)
