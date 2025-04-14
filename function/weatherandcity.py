def introduce_yourself():
    username = input(f"Hello! would you mind telling me your name? ")
    while True:
        if username.isalpha():
            break
        else:
            username = input(f"Please only use alphabetic characters. would you mind telling me your name? ")
    print(f"Hello {username}, you look good today bbg")
    return username
username = introduce_yourself()

def user_input(city="Jambi", weather="Sunny"):
    user_city = input(f"Where do you live {username}?")
    while not user_city.isalpha():
        user_city = input(f"Please only use alphabetic characters, where do you live {username}? ")
        city = user_city
    user_weather = input(f"What is your preferred weather {username}? ")
    while user_weather and not weather.isalpha():
        user_weather = input(f"Please only use alphabetic characters, what's your preferred weather {username}? ")
        weather = user_weather
    return city, weather
city, weather = user_input()

if weather.lower() == "sunny":
    print(f"In {city}, a {weather} day is nice for a walk in the park {username}!")
elif weather.lower() == "rainy":
    print(f"In {city}, a {weather} weather is perfect for a hot bowl of ramen!")
elif weather.lower() == "stormy":
    print(f"In {city}, you should be careful if it's {weather}!")
else:
    print(f"{weather} in {city} sounds dope, hope your day goes great!")