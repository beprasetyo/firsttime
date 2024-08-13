#concantenate string
name = input("What is your name ? ")
age = int(input("How old are you ? "))
height = float(input("How tall are you ? "))

age = age + 1
height = height + 3
print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+" cm height")