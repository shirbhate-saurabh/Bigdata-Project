import csv
from datetime import datetime

path = 'D:\Study\TestData.csv'
file = open(path, newline='') #opens the file
reader = csv.reader(file) # reads the data line by line

header = next(reader)  #this skips the first line considered as header

#data = [row for row in reader]  #this will read the data line by line and store in list as it is

#but below process stores the data in format as required.

data = [] #for storing the read data in row manner with the changed format as per requirement.
for row in reader:
    sr_no = int(row[0])
    source = row[1]
    name = row[2]
    contact_no = int(row[3])
    branch = row[4]
    course = row[5]
    paid_fees = int(row[6])
    paid_date = datetime.strptime(row[7], '%d-%b-%y')

    data.append([sr_no,source,name,contact_no,branch,
                     course,paid_fees,paid_date])

    
print(header)
a = (int(input("enter no : ")))
b = (int(input("enter no : ")))
print(data[a:b])


 
