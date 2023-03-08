# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]
candy_cart = [] 
# Print out options
for x in range(len(candy_list)):
    print(f"[{x}]{candy_list[x]}")

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
for y in range(allowance):
    candy_ix = int(input("which candy would you like? "))
    candy_cart.append(candy_list[candy_ix])

for w in range(len(candy_cart)):
    print(f"you have purchased {candy_cart [w]}")

