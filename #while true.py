#while true

#directly using true instead of a conditional statement
#will make an infinite loop

while True:
    s = input("Please input some thing :")
    if s.lower() == "quit":
        break
    print("Lenght of given text is ",len(s))
print("good bye")