import pandas as pd
from datetime import date
import matplotlib.pyplot as plt


# Each person has its own unique id
person_id = {'P1': 'Sam Ovens',
             'P2': 'Jessica Ricks',
             'P3': 'Mark Schuztler',
             'P4': 'Saul Goodman',
             'P5': 'Amber Parker',
             'P6': 'Stephen King'
            }

# Each group has its own unique id 
group_id = {'G1': 'Mavericks',
            'G2': 'Blue Jays',
            'G3': 'Panthers'
           }

# Each subject has its own subject id
subject_id = {'S1': 'Physics',
              'S2': 'Maths',
              'S3': 'Chemistry',
              'S4': 'Biology', 
              'S5': 'English'
              }

# Role of each person
role = {
        'T': 'Teacher',
        'S': 'Student'
        }

# Modeling table using a dictionary 
marks = {'P2':[{'S1': date(2019, 7, 17),
                'S2': date(2020, 7, 18),
                'S3': date(2020, 7, 19)},
                {
                'S1': 56,
                'S2': 98,
                'S3': 75,
              }],

         'P4':[{'S2': date(2017, 8, 15),
                'S5': date(2019, 8, 16),
                'S4': date(2019, 8, 17)},
                {
                'S2': 95,
                'S5': 99,
                'S4': 78,
               }],

          'P6':[{'S1': date(2019, 7, 15),
                 'S2': date(2019, 7, 16),
                 'S3': date(2020, 7, 17)},
                {
                 'S1': 45,
                 'S3': 56,
                 'S4': 60
             }],
        }

# Datapipeline = (JSON data -> functions -> values access (Viz, Machine Algorithm, Data cleaning, Data Proces)-> manipulate value -> update JSON )

def get_value(student_id, type_of_value):
    if type_of_value == 'Marks':
        #print("Marks of: ", student_id)
        type_of_value = 1
    else:
        #print("Date of: ", student_id)
        type_of_value = 0
    
    dict_marks = marks[student_id][type_of_value]
    marks_list = dict_marks.values() # list of marks 
    subjects  = dict_marks.keys() # list of student id 


    student_name = person_id[student_id]
    student_subjects = []
    

    for sid in subjects:
        sub_name = subject_id[sid]
        student_subjects.append(sub_name)

    title = 'Marks of: ' + student_name 
   
    # plotting marks of student for their subjects
    plt.title(title)
    plt.ylabel('Marks')
    plt.xlabel('Subjects')
    plt.bar(student_subjects, marks_list)
    plt.show()
    
    return marks[student_id][type_of_value]




get_value('P2', 'Marks')

# Exam time
# check for the consistency between subject taken and the exams given
exam_date  = {'P2':{
                    'S1': date(2020, 2, 25),
                    'S2': date(2020, 1, 17),
                    'S3': date(2019, 8, 17),
                    },

            'P4':{
                    'S2': date(2020, 1, 18),
                    'S5': date(2019, 6, 19),
                    'S5': date(2019, 3, 20),
                    },

            'P6':{
                   'S1': date(2018, 2, 20),
                   'S3': date(2018, 2, 21),
                   'S4': date(2018, 2, 22),
                 },
            }


# Create function to create dataframes, manipulate dataframe, clean, csv, json,
# Mongodb

# Records (Automate)
initial_records = [['P1', 'G1', 'T'], 
                   ['P2', 'G1', 'S'],
                   ['P3', 'G1', 'T'],
                  ]

# Create lists
Names = []
Groups = []
Subjects = []
Roles = []

for records in initial_records:
    name, group, role = records
    Names.append(name)
    Groups.append(group)
    Roles.append(role)


# Create dataframe
df_student_dataframe = pd.DataFrame({'Name Id': Names, 'Group Id':Groups, 'Role Id':Roles})



