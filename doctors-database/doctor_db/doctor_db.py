#Doctor's Table

doctor = {
          1: {'first_name':'Rajesh', 'last_name': 'Singh'},
          2: {'first_name':'Sonal', 'last_name': 'Dutt'},
          3: {'first_name':'J.S.', 'last_name': 'Chandra'}
         }

#Patient Table

patient = {
           11:{'first_name':'Saurabh', 'last_name':'S', 'address':'New Panvel','city':'Navi Mumbai','state':'Maharashtra'},
           12:{'first_name':'Shreyas', 'last_name':'N', 'address':'Ghatkopar','city':'Delhi','state':'Delhi'}
          }

#Bill Table

bill = {
        111:{'bill_date':'15-10-2018', 'bill_status':'Pending'},
        112:{'bill_date':'20-10-2018', 'bill_status':'Paid'}
       }

#payment Table

payment_receipt = {
                   1010:{'payment_date':'15-10-2018', 'payment_method':'Cash', 'payment_amount':2000},
                   1016:{'payment_Date':'20-10-2018', 'payment_method':'Card', 'pay_amount':5000}
                  }
          

#Appointment Table
appointment_details = {
                       '15-10-2018':{'appointment_time':'10:30 AM', 'appointment_duration':'00:30:00',
                                     'appointment_reason':'Report Checking', 'doctor_id':1},
                       '20-10-2018':{'appointment_time':'06:30 PM', 'appointment_duration':'01:00:00',
                                     'appointment_reason':'Routine Checkup', 'doctor_id':3}
                      }