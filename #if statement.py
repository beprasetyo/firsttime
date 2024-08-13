#if statement
age = int(input("How old are you ? "))

if age >= 18 and age <100:
    print("You are an adult")
elif age < 0:
    print("you have not been born yet")
elif age >=100:
    print("you are too old")
else:
    print("You are a child")