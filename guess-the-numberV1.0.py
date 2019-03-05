#Guess The Number Game
import random

number = random.randint(1,101)
guess_counter = 1
guess = ""

while guess != number:
    guess = int(input("Guess a number: "))
    guess_counter + 1

    if guess < number:
        print ("Guess to low.")
        guess_counter += 1

    elif guess > number:
        print ("Guess to high.")
        guess_counter += 1
        
    else:
        print ("Guess correct!\nIn",guess_counter)


































