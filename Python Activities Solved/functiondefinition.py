# def name(first_name):
#     upper_name = first_name.upper()
#     return(upper_name)
#     print(upper_name)
# # name("Piro")

# # def name(first_name): 
# #     upper_name = first_name.upper()
# #     return upper_name 

# new_name = name("Piro")
# print(new_name)

def name(first_name, last_name="Dhimitri"): 
    upper_fname = first_name.upper()
    upper_lname = last_name.upper()
    return(f"{upper_fname} {upper_lname}")

print(name("Piro", "CRUISE"))

def squared(num=4): 
    return num*num

print(squared())