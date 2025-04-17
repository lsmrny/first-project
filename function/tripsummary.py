def user_input():
    name = input("What is your name? ")
    while name and not name.replace(" ", "").isalpha():
        name = input("PLease use alphabetic characters, What is your name? ")
    city = input("Where did you go for your trip? ")
    while city and not city.replace(" ", "").isalpha():
        city = input("PLease use alphabetic characters, Where did you go for your trip? ")
    str_days = input(f"How many days did you spent at {city}? ")
    while str_days and not str_days.isdigit():
        str_days = input("PLease use alphabetic characters, Where did you go for your trip? ")
    days = int(str_days)
    activity = input(f"What is your favorite activity during ur time in {city}? ")
    while activity and not activity.replace(" ", "").isalpha():
        activity = input(f"Please only use alphabetic characters, What is your favorite activity during ur time in {city}? ")
    rating_str = input("How would you rate this trip from 1-5? ")
    while rating_str and not (1 <= int(rating_str) <= 5):
        rating_str = input("Please only use numeric characters from 1-5, How would you rate this trip from 1-5? ")
    rating = int(rating_str)
    return name, city, days, activity, rating
def trip_summary(name, city, days, activity, rating):
    print(f"Hey {name}, your {days} days trip to {city} sounds really fun!")
    print(f"{activity} sounds amazing, i should also go try that sometime!")
    print(f"Rating : {'🔥' * rating} ({rating}/5)")
    print()
all_trips = []
while True:
    name, city, days, activity, rating = user_input()
    all_trips.append((name, city, days, activity, rating))
    cont = input("Do you want to input more trips? (yes/no) ")
    if cont.lower() == "no":
        break
    while cont.lower() not in ["yes", "no"]:
        cont = input("PLease only use (yes/no), Do you want to input more trips? ")
print()
print(f"\n---ALL TRIPS SUMMARY---")
for trip in all_trips:
    trip_summary(*trip)