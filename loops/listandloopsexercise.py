#ill try to use loops in something else, lets hope for the best
print(f"Hello hello, it's me Louis, your health advisor, i'm gonna ask about your exercise routine")
#ill try to make a logic tree, again
response = input(f"Are you okay with it? (Yes/No) ")
if response.lower() == "yes":
    print("Okayyy :D, let's get started then")
    exercise_types = int(input(f"How many types of exercises do you do? "))
    #making a list
    exercises = []
    for i in range(exercise_types):
        exercise = input(f"Exercise #{i + 1}: ")
        exercises.append(exercise)
    print("\nAlright, this's what you entered")
    for exercise in exercises:
        print(f"{exercise}")
    #ill also try to make the silly comments based on logic
    print() #idk how to skip a row lolol
    for exercise in exercises:
        if exercise.lower() == "gym":
            print("Looking big bro, keep grinding!!")
        if exercise.lower() in ["run", "running", "jogging", "jog", "marathon"]:
            print("I bet u have one hell of an endurance")
        if exercise.lower() in ["swim", "swimming"]:
            print("GO ON MICHAEL PHELPS LET'S GOO")
else:
    print("Uh, okay then i suppose :D")
