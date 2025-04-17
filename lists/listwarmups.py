favorite_foods = []

print("Please add items to your list :), type 'done' when you're finished")
while True:
    foods = input(f"Food #{len(favorite_foods) + 1} : ")
    if foods.lower() == "done":
        break
    if foods.lower() == "":
        continue
    favorite_foods.append(foods)

askremove = input("Do you want to remove anything from the list? (yes/no) ")
while not askremove.lower() == "yes" and not askremove.lower() == "no":
    askremove =input("Please only user alphabetic characters, do you want to remove anything? (yes/no) ")
while askremove.lower() == "yes":
    itemremoved = input("Which item? ")
    if itemremoved in favorite_foods:
        favorite_foods.remove(itemremoved)
    askremove = input("Do you want to remove anything else? (yes / no) ")
    while not askremove.lower() == "yes" and not askremove.lower() == "no":
        askremove =input("Please only user alphabetic characters, do you want to remove anything? (yes/no) ")
    if askremove.lower() == "yes":
        continue
    else:
        break
print()
print("Here's your updated grocery list!")
for foods in favorite_foods:
    print(f"- {foods}")

numbers_list = [10, 20, 30, 40, 50, 60, 70]
print(numbers_list[0:2])
print(numbers_list[-2:])
print(numbers_list[1:])