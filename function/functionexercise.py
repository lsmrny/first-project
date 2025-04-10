def introduce_yourself():
    username = input(f"Hello! would you mind telling me your name? ")
    while True:
        if username.isalpha():
            break
        else:
            username = input(f"Please only use alphabetic characters. would you mind telling me your name? ")
    print(f"Hello {username}, you look good today bbg")
def bmi_calculator(weight, height):
    height_m = height/100
    BMI = weight / (height_m * height_m)
    return round (BMI, 2)

introduce_yourself()
height = input("Would you mind telling me ur height? (cm) ")
while True:
    if height.isnumeric():
        break
    else:
        height  = input(f"Please only use valid characters. Would you mind telling me ur height? (cm) ")
weight = input("Would you mind telling me ur weight? (kg) ")
while True:
    if weight.isnumeric():
        break
    else:
        weight  = input(f"Please only use valid characters. Would you mind telling me ur weight? (kg) ")
a = int(weight)
b = int(height)
bmi = bmi_calculator(a, b)
print(f"Okay i've analyzed your BMI is {bmi}")
if bmi < 18.5:
    print("Hmmm you're a bit underweight, let's try and eat more!")
elif 18.5 < bmi < 24.9:
    print("You're doing great, keep doing what ur doing!")
elif 24.9 < bmi < 29.9:
    print("You're like a tiny tiny bit overweight, let's try to tone it down justtt a little bit ok?")
else:
    print("You are obese, let's try to eat less and eat healthier foods okayy?")