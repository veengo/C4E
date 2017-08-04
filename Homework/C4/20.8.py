#20.8.1
letters = input("Insert a sentence: ")
letters = letters.lower()
letter_counts = {}
for letter in letters:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

letter_list = list(letter_counts.items())
letter_list.sort()
print(letter_list)

#20.8.2
def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] = inventory[fruit] + quantity
    else:
        inventory[fruit] = quantity
    print("new inventory has:", inventory[fruit], fruit)
    return

def test(test):
    print(test)
    return

new_inventory = {}

print("")
print("add 10 strawberries")
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)

print("")
print("after added 25 more strawberries")
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)
