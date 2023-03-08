# int 
# float
# string 
# boolean 

# lists -> mutable 
# tuples -> immutable 

# myTuple = ("Toronto", "Vancouver", "Montreal")

# ___myList_ix = [0, 1, 2]
# myList = ["Toronto", "Vancouver", "Montreal"]
# myList[0] # ==> Toronto
# myList[1] # ==> Vancouver


# # key : value 
# myCities = {0 : "Toronto"
#                 , 1 : "Vancouver"
#                 , 2: "Montreal"}



# print(myCities[0]) # ==> Toronto
# print(myCities[1]) # ==> Vancouver

myCities = {"Ontario" : "Toronto",
            "BC" : "Vancouver", 
            "Quebec": "Montreal",
            "Ontario": "Ottawa"}

print(myCities["Ontario"])  # ==> Toronto 

actors = {
    "name": "Tom Cruise", 
    "age" : 32, 
    "movies" : ["Top Gun", "Top Gun 2"], 
    "best_movies" :     {
            "1986": "Top Gun", 
            "2022" : "Top Gun 2" 
    }
}

print(actors["best_movies"]["1986"])

print(actors.keys())
