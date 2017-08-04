#Exercise 1
inventory = {
            'gold' : 500,
            'pouch' : ['flint', 'twine', 'gemstone'],
            'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
        }
inventory["pocket"] = "key"
inventory["pocket"] = ["seashell", "strange berry", "lint"]

list.sort(inventory["backpack"])
inventory["backpack"].sort()
print(inventory)


inventory["backpack"].remove("dagger")
inventory["gold"] += 50
print(inventory)


#Exercise 2

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }
purchased_items = {"banana" : 5,
                   "orange" : 3}

for i in prices:
    if i in purchased_items:
        print(i, ", quantity :", purchased_items[i], ", unit price", prices[i])
    else:
        print(i, ", quantity :", 0, ", unit price", prices[i])

total = 0
for n in purchased_items:
   total = total + prices[n] * purchased_items[n]
print("The total cost is", total)
