fav_numbers = []
num_qty = 5
print("Hello hello there, you need to give me 5 of your favourite numbers, for no reason in particular ;)")
for i in range(num_qty):
    numbers = int(input(f"Number #{i + 1} : "))
    if numbers == "":
        continue
    fav_numbers.append(numbers)
print()
askremove = input("Okay, now do you want to remove any of the numbers? (yes/no) ")
if askremove.lower() == "yes":
    print("Alright then, go for it, just tyoe '000' when you're finished")
    while True:
        removed_num = int(input(f"What number ? "))
        if removed_num == 000:
            break
        if removed_num in fav_numbers:
            fav_numbers.remove(removed_num)
    print()
else:
    print()
numbers_sum = sum(fav_numbers)
numbers_max = max(fav_numbers)
numbers_min = min(fav_numbers)
print("Okay, so here's what i've analyzed")
print("These are the numbers you inputted")
for numbers in fav_numbers:
    print(f"- {numbers}")
print(f"Here's the sum of all your numbers : {numbers_sum}")
print(f"Here's what the largest number : {numbers_max}")
print(f"Here's what the smallest number : {numbers_min}")