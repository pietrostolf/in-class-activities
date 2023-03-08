import csv
import os

myfile = "Tuesday/myData.csv"
myfilepath = os.path.join("Tuesday", "myData.csv")

print(myfilepath)

with open(myfile, 'r') as csvfile:

    #print(csvfile.read())
    output = csv.reader(csvfile, delimiter=",")

    for line in output: 
        print(line)

print(csvfile.read())