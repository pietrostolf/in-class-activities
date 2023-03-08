import os
import csv



cereal_csv = os.path.join("Resources", "cereal.csv")
cereal_csv = os.path.normpath(cereal_csv)


#with open('C:/git/in-class-activities/Python Activities Solved/01-Stu_CerealCleanerSolved/Resources/cereal.csv', 'r', encoding='utf-8') as csvfile:
with open(cereal_csv, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)

    header_row = next(csvfile)
    for row in csvreader:
        if float(row [7]) >= 5:
            print (row)
       

        
        