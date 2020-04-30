# Guess The Number Game
import random
secretNumber= random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask player to take a guess 6 times
for guessesTaken in range (1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #this is the correct guess

if guess == secretNumber:
    print('Good job! You guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Sorry. The number I was thinking of was ' +  str(secretNumber))
