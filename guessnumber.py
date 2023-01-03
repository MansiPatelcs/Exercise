import random
a=random.randint(1,9)


while True:
    guess=int(input('Guess the number between 1 to 9:'))

    if guess==a:
        print("well guessed number")
        break
    else:
        print("Please choose the number between 1 to 9")
        continue





