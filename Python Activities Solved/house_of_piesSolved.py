pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee",  "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
purchased_pies = []
totals = [0,0,0,0,0,0,0,0,0,0]

for x in range(len(pie_list)):
    print(f"[{x}]{pie_list[x]}")

status = "y"

while status =="y":
    pie = int(input("which pie would you like? "))
    print(f"Great! We'll have that {pie_list[pie]} right out for you")
    status = input("would you like another one? (y/n) ")
    purchased_pies.append(pie_list[pie])
    totals[pie] = totals[pie] + 1

print(f"you have oredered {len(purchased_pies)} pies")

for w in range(len(pie_list)):
    print(f"{totals[w]} {pie_list[w]}")