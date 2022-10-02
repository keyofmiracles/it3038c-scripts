import random
number = random.randrange(0, 25)

print("Guess what the number is and enter your choice:")
guess = int(input())

while guess > number:
    print("Too high! Try again!")
    guess = int(input())

while guess < number:
    print("Too low! Try again!")
    guess = int(input())

print("Good job!")
 

    

2