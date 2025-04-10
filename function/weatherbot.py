def weather_reaction(weather):
    if weather == "sunny":
        reaction = f"Sounds like a great day for a walk!"
    elif weather == "rainy":
        reaction = f"Don’t forget your umbrella!"
    elif weather == "cloudy":
        reaction = f"Perfect time to chill with some coffee."
    elif weather == "snowy":
        reaction = f"Stay warm out there!"
    else:
        reaction = f"Hmm, that's an unusual weather!"
    return reaction

def introduce_yourself():
    username = input(f"Hello! would you mind telling me your name? ")
    while True:
        if username.isalpha():
            break
        else:
            username = input(f"Please only use alphabetic characters. would you mind telling me your name? ")
    print(f"Hello {username}, you look good today bbg")

introduce_yourself()
user_weather = input("What's the weather like today? ")
while not user_weather.isalpha():
    user_weather = input("Please use only alphabetic characters, What's the weather like today? ")
else:
    user_weather = user_weather.lower()
print(f"Weather-bot says '{weather_reaction(user_weather)}'")
    