import csv 

filepath = 'Tuesday/OfficeData.csv'
with open(filepath, 'w', newline='') as csvfile: 

    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow(["firstname", 'lastname', 'age'])

    writer.writerow(['Piro', "Dhimitri", '30'])


indexes = [1, 2, 3, 4]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]

roster = zip(indexes, employees, department)

#for employee in roster: 
    #print(employee)

with open(filepath, 'w', newline='') as f: 
    
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['ID', "Employee", "Dept"])
    #writer.writerows(roster)
    for employee in roster: 
        writer.writerow(employee)