import csv

place = []
population = []
income = []
poverty = []
povertyr = []

with open('census_starter.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        place.append(row[0])
        population.append(row[1])
        income.append(row[4])
        poverty.append(row[5])
        povertyr.append(str(row[2]) + "%")

    databunch = zip(place, population, income, poverty, povertyr)

with open('censusnew.csv', 'w', newline='', encoding='utf-8') as f: 
    
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Place', "Population", "Per Capita Income", "Poverty Count", "Poverty Rate"])
    
    writer.writerows(databunch)