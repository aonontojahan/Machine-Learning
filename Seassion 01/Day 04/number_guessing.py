# number guessing game

from random import randint

number = randint(1,100)
count = 0

while True:
    guess = int(input("Please guess the number from 1-100: "))
    count +=1
    if guess == number:
        print(f"You guess the right number with {count} times")
        break
    elif guess < number:
        print(f"Your guess is low")
        print(f"Try higher value")
    else:
        print(f"Your guess is high")
        print(f"Try lower value")