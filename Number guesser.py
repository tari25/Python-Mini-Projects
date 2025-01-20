import random

print("A number between 0 and 1000 will be chosen at random. You will be given 10 chances to guess the number. Good luck!!")
number = random.randint(0, 1000)
chances = 10
guessed = False
while chances > 0:
    guess = int(input("Guess the number: "))
    if guess == number:
        print("Congratulations, you guessed the number correctly!!")
    elif guess > number:
        print("too big")
    else:
        print("too small")
    chances -=1

if guessed == False :
    print("Game over, the number was " + str(number))
else:
    print("Game Over!!")