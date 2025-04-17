numbers = []

print("Hello hello, please input some numbers, for no reason in particular, type 'done' when you are")
while True:
    num_str = input(f"Number #{len(numbers) + 1} : ")
    if num_str.lower() == "done":
        break
    while num_str and not num_str.isdigit():
        num_str = input(f"Please only use numeric characters, Number #{len(numbers) + 1} : ")
        if num_str.lower() == "done":
            break
    if num_str.lower() == "done":
        break
    num = int(num_str)
    numbers.append(num)
print()
print("Okay, here's the full list")
for num in numbers:
    print(f"- {num}")
print("Here's the list in an ascending order")
numbers.sort()
for num in numbers:
        print(f"- {num}")
print("Here's the list in a descending order")
numbers.reverse()
for num in numbers:
        print(f"- {num}")
max_num = max(numbers)
print(f"Here's how many times {max_num} appeared")
print(f"{numbers.count(max_num)} times!")