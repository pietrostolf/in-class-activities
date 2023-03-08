myList = ["Piro", 30, True, 3.14]
print(myList)
print(myList[0])

myList.append("Toronto")
print(myList)

myList[2] = 85
print(myList)

myList.index("Piro")

print(len(myList))

myList.remove("Piro")
print(myList)

myList.pop(3)
print(myList)

myTuple = ("Piro", 30, True, 3.14)
#myTuple.remove("Piro") does not work, tuples are not mutable