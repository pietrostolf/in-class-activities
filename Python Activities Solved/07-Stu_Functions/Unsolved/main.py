# @TODO: Write a function that returns the arithmetic average for a list of numbers


def average(numbers): 
    average = sum(numbers) / len(numbers)
    return(f"the average is {average}")

# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))
