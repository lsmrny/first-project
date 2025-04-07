print("Welcome to you personalized food tracker, lets get this started!")
#ask how many types of food they want to enter
food_count = int(input("How many favourite foods do you want to input?"))
#make an empty list, at this moment have no idea what this does
foods = []
#use a loop to collect each food
for i in range(food_count):
    food = input(f"Enter food #{i+1}: ")
    foods.append(food)

print("\nHere's what you entered!")
for food in foods:
    print(f"The {food}")

for food in foods:
    if food.lower() == "salad" or food.lower() == "broccoli":
        print(f"Yooo, you're ealting healthy with the {food}!")
