import csv

title = input("which book would you like to search? ")

# open the CSV file in read mode
with open('comic_books.csv', 'r', encoding='utf-8') as csvfile:
    # create a CSV reader object
    csvreader = csv.reader(csvfile)

    # iterate through each row in the CSV file
    for row in csvreader:
        # iterate through each cell in the row
            if row[0] == title:
                # print the row and column index of the cell
                print(f"{row[0]} was published by {row[8]} in {row[9]}")