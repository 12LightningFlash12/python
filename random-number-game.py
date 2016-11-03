import random

guesses_made = 0
name = raw_input('Hello! What is your name?\n')
number = random.randint(1, 100)

print 'Well, {0} i am thinking of a number from 1 to 100'.format(name)

while guesses_made < 6:
    
    guess = int(raw_input('Take a guess: \n'))
    guesses_made += 1
    
    if guess < number:
        print 'Your guess is too low.\n'
    
    if guess > number:
        print 'Your guess is too high.\n'
    
    if guess == number:
        break

if guess == number:
    print 'Good job, {0}! you guessed my number in {1} guesses!'.format(name, guesses_made)
else:
    print 'Nope. The number I was thinking of was {0}'.format(number)
