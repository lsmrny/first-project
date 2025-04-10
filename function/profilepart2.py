def collect_user_data(name, age, city="Jambi"):
    return print(f"Hello {name} from {city}, age {age}")

username = input("Hello!! What is your name? ")
while not username.isalpha():
    username = input("Please use only alphabetic characters, What is your name? ")
user_age = input(f"How old are you {username}? ")
while not user_age.isdigit():
    user_age = input(f"Please use only numeric characters, How old are you {username}? ")
user_city = input(f"Where are you from {username}? (City) ")
while user_city and not user_city.isalpha():
    user_city = input(f"Please use only alphabetic characters, where are you from {username}? ")

if user_city:
    user_data = collect_user_data(username, user_age, user_city)
else:
    user_data = collect_user_data(username, user_age)
print(user_city)