#Q1. Transform the json data into a tabular structure (csv) USING CORE PYTHON as shown here:
#["title", "smdName", "organizationName", "sourceType", "sourceUrl", "icarUrl", "keywords", language]

import json
import csv
#Q Convert json file into the csv file 

# simple file format used to store tabular data
# with the help of json Opening JSON file and loading the data

with open (r'C:\Users\rhutuja.b.patil\Desktop\Pandas\source.json',encoding='utf-8') as file:
    dic=json.load(file)
    
information1=dic['data']

# now we will open a file for writing mode
csv_file=open('source.csv','w',encoding='utf-8')

csv_writer=csv.writer(csv_file)

# with the help of loop writing keys as header and values as rows
count=0
for i in information1:
    if count==0:
        key=i.keys()
        csv_writer.writerow(key)
        count+=1
    value=i.values()
    csv_writer.writerow(value)
# and finally file is closed
csv_file.close()