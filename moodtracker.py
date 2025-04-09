def check_mood(mood):
    if mood == "happy":
        print("That's great to hear, keep your spirits up!")
    elif mood =="sad":
        print("Aww, i'm sorry to hear that, let's put on some music and fight the sadness okay?")
    elif mood =="angry":
        print("Okay, let's calm down, i'll bring snacks later, don't lash out alright?")
    else:
        print("Well, i hope your day goes great:D")

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
feel = input(f"How are you feeling today {username}? ")
while True:
    if feel.isalpha():
        feel.lower()
        break
    else:
        feel = input(f"Please only use alphabetic characters. How are you feeling today {username}? ")
check_mood(feel)