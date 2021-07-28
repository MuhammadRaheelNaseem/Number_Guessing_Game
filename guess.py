import random

number=random.randint(1,11)
print("Please Guess Number From 1 to 10")

for i in range(0,3):
    user=int(input("Guess The number"))
    if user==number:
        print("Hurray!!")
        print(f"You guessed the number right it's {number}")
        break
    else:
        print("Ops! try again")
        
if user!=number:
    print(f"Your guess is incorrect the number is {number}")
