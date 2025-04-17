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
    askitemremoved = input("First or last one? (first / last) ")
    while not askitemremoved.lower() == "first" and not askitemremoved.lower() == "last":
        askitemremoved =input("Please only user alphabetic characters, First or last one? (first / last) ")
    if askitemremoved =="last":
        favorite_foods.pop()
    elif askitemremoved == "first":
        favorite_foods.remove(favorite_foods[0])
    askremove = input("Do you want to remove more items? (yes/no) ")
    while not askremove.lower() == "yes" and not askremove.lower() == "no":
        askremove =input("Please only user alphabetic characters, do you want to remove anything? (yes/no) ")
print()
print("Here's your updated grocery list!")
for foods in favorite_foods:
    print(f"- {foods}")