user = 'poly'

password = '1234'

userInput = input("What is your username?")

if userInput == user:
    x=input("Password?")
    if x == password:
        print("Welcome!")
    else:
        print("password wrong.")
else:
    print("something wrong.")