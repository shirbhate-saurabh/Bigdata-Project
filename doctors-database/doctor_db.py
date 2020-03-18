#Doctor's Table

doctor = {'DID':
          {1: {'First_Name':'Rajesh', 'Last_Name': 'Singh'},
           2: {'First_Name':'Sonal', 'Last_Name': 'Dutt'},
           3: {'First_Name':'J.S.', 'Last_Name': 'Chandra'}
          }
         }

#Patient Table##########PENDING#################

patient = {'PID':
           {11:{'PFN':'Saurabh', 'PLN':'S'},
            12:{'PFN':'Shreyas', 'PLN':'N'}
           },
           'P_add':['N Panvel','Ghatkopar'],
           'P_City':['Mumbai','Delhi'],
           'P_State':['Maharashtra','Delhi']
          }

#Bill Table

bill = {'Bill_No':{111:{'Bill_Date':'15-10-2018', 'Bill_Status':'Pending'},
                   112:{'Bill_Date':'20-10-2018', 'Bill_Status':'Paid'}
                  }
       }

#payment Table

payment = {'Receipt_No':{1010:{'Pay_Date':'15-10-2018', 'Pay_Method':'Cash', 'Pay_Amt':2000},
                         1016:{'Pay_Date':'20-10-2018', 'Pay_Method':'Card', 'Pay_Amt':5000}
                        }
          }
           

#Appointment Table
appointment = {'App_Date':{'15-10-2018':{'App_Time':'10:30 AM', 'App_Dur':'00:30:00',
                                         'App_Reason':'Report Checking'},
                           '20-10-2018':{'App_Time':'0630 PM', 'App_Dur':'01:00:00',
                                         'App_Reason':'Routine Checkup'}
                          }
              }