import csv
import pandas as pd
import re
data =[]


with open('/home/ap/PycharmProjects/Portafolio/customers.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile, delimiter=',')
    for row in reader:
        data.append(row)

for row in data:
    pattern = row['SSN']
    row['SSN'] = pattern.replace(row['SSN'],'xxx/xx/xxxx')
    print(row['SSN'])