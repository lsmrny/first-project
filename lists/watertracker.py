print("Hello hello, i'm your personal water tracker, please tell me how many glasses of water u drank today!")
glass_list = []
while True:
    water = input(f"how many glass of water have u drank? ")
    if water == "done":
        break
    if water == "":
        continue
    if not water.isdigit():
        print("Please input a valid number!")
    else:
        water_glass = int(water)
        glass_list.append(water_glass)
print()
print("Okay, thanks for your input, here's your results")
water_sum = sum(glass_list)
if len(glass_list) > 0:
    water_avg = water_sum / len(glass_list)
else:
    water_avg = 0
print(f"You drank a total of {water_sum} glasses of water")
if water_sum > 10:
    print("Good job on hydrating yourself, keep it going!😎")
elif water_sum < 4:
    print("Maybe.. you should drink more water haha😀")
print(f"The average glasses per entry is {water_avg}")

