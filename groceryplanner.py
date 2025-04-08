groceries_list = []

print("Welcome to your monthly shopping list!")
print("Please add items to your list :), type 'done' when you're finished")
while True:
    groceries = input(f"Item #{len(groceries_list) + 1} : ")
    if groceries.lower() == "done":
        break
    if groceries.lower() == "":
        continue
    groceries_list.append(groceries)
print()
askremove = input("Do you want to remove any items? (yes/no) ")
if askremove.lower() == "yes":
    print("type 'done' when you're finished :)")
    while True:
        itemremoved = input(f"Item : ")
        if itemremoved in groceries_list:
            groceries_list.remove(itemremoved)
        if itemremoved.lower() == "done":
            break
    print()
else:
    print()
print("Here's your updated grocery list")
for groceries in groceries_list:
    print(f"- {groceries}")