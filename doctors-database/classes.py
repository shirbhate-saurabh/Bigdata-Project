"""creating classes for doctor database in which base class is "Person" and other classes are
   "doctor", "patient", "appointment""""

from collections import defaultdict
from datetime import datetime


class Person:
    def __init__(self,first_name,last_name):
        
        self.first_name = ['Saurabh','shreays',"Akshay","Ritesh"]
        
        self.last_name = ["S","Shirbhate","Kale","Shivkar"]
        
        
class Doctor:
    def __init__(self):
        pass
        
    def doctor_id_generator():
        temp = defaultdict(lambda: len(temp) + 1)
        temp1 = [temp[ele] for ele in self.first_name]
        doctor_id = str(temp1)
        print(doctor_id)
        
        
class Patient:
    def __init__(self):
        pass
    
    def patient_id_generator():
        temp = defaultdict(lambda: len(temp) + 1000)
        temp1 = [temp[ele] for ele in self.first_name]
        patient_id = str(temp1)
        print(patient_id)
    
class Aappointment:
    def __init__(self):
        pass
    
    def appointment_id_generator():
        temp = datetime.now().timestatmp()
        temp1 = str(temp).replace('.','')
        appointment_id = temp1
    
    
    
            
        