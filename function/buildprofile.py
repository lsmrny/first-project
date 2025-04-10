def build_profile(name, age, hobby="napping"):
    return f"Name : {name} | Age : {age} | Hobby : {hobby}"

name = input(f"What is your name? ")
while not name.isalpha():
    name = input(f"Please only use alphabetic characters. would you mind telling me your name? ")
age_str = input("How old are you? ")
while not age_str.isdigit():
    age_str = input("Please only use valid characters! How old are you?")
age = int(age_str)
hobby = input("Would you mind telling me your hobby? (optional) ")
while hobby and not hobby.isalpha():
    hobby = input(f"Please only use alphabetic characters. would you mind telling me your hobby? (optional) ")

if hobby:
    profile = build_profile(name, age, hobby)
else:
    profile = build_profile(name, age)
print(profile)