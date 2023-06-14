userName = input("What is your name?")
userAge = input("And How old are you?")

print("Hello " + userName)

if int(userAge) >= 18:
    print("You're old enought to vote in the United States")
else: 
    print("Wait a few more years before you can vote in the United States.")