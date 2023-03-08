import os
import csv

# Path to collect data from the Resources folder
graduation_csv = os.path.join("08-Par_GraduatingFunctions","Resources", "graduation_data.csv")

# Define the function and have it accept the 'state_data' as its sole parameter
def print_percentages(state_data): 
   
# Find the total students
    pub_rate = 100*(int(state_data[2])/int(state_data[1]))
    pub_rate = round(pub_rate,2)
    if int(state_data[3]) != 0:  
        npp_rate = 100*(int(state_data[4])/int(state_data[3]))
        npp_rate = round(npp_rate,2)
    else:
        npp_rate = None
    if int(state_data[5]) != 0:
        fpp_rate = 100*(int(state_data[6])/int(state_data[5]))
        fpp_rate = round(fpp_rate,2)
    else:
        fpp_rate = None
    return(f"the public graduation rate is {pub_rate}%, the NP Private graduation rate is {npp_rate}%, the FP Private graduation rate is {fpp_rate}%")


# Find the total graduates

# Find the public school graduation rate

# Remember that some states do not have nonprofit or forprofit private schools
# Find the non-profit school graduation rate

# Find the for-profit school graduation rate

# Calculate the overall graduation rate

# Print out the state's name and its graduation rates


# Read in the CSV file
with open(graduation_csv, 'r', encoding='utf-8') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # Loop through the data
    #header_row = next(csvfile)
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check == row[0]:
            print(print_percentages(row))
