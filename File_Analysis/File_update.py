import csv
import pandas as pd

path = 'D:\Study\Big Data\data_test.csv'
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)  #this skips the first line considered as header
data = [row for row in reader]  #this will read the data line by line and stored in list

print(header)
a = (int(input("enter no : ")))
b = (int(input("enter no : ")))
print(data[a:b])