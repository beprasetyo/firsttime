#if statement2

temp = int(input("What is the temperature outside today ?"))

if not(temp >=0 and temp <= 32):
    print("The weather is good today, go outside")
elif not(temp < 0 or temp > 32):
    print("The weather is bad today, just stay inside")