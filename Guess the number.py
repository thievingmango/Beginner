#Guess the number
import random
# What is your name?
print('What is your name?')

name = input()
secretnumber = random.randint(1,30)

#I am thinking of a number between randint
 
print('Hi ' +str(name) +' I am thinking of a number between 1 and 30')

for i in range(1,7): 
    guess = int(input())
    if guess > secretnumber and i < 5:
            print('Your guess is too high, you have ' + str(6-i) + ' guesses left')

    elif guess < secretnumber and i < 5:
        print('Your guess is too low, you have ' + str(6-i) + ' guesses left')
    elif guess > secretnumber and i == 5:
        print('Your guess is too low, this is your last guess')

    elif guess < secretnumber and i == 5:
        print('Your guess is too low, this is your last guess')
    
    else:
        break #correct guess

  
if guess == secretnumber:
    print('Congrats! ' +name + ' you guessed the right number!')
else:
    print('Sorry, the number i was thinking of is ' + str(secretnumber))

