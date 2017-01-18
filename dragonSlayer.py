import random

slaying = True
youHit = random.randint(0, 1)
damageThisRound = random.randint(1, 5)
totalDamage = 0

while slaying:
    if youHit == 1:
        print'you hit the dragon and did {0} damage!'.format(damageThisRound)
        totalDamage = damageThisRound
        
        if totalDamage >= 4:
            print 'You did it! You slayed the dragon!'
            slaying = False
        else:
            youHit = random.randint(0, 1)
    else:
        print 'The dragon burns you! You are toast!'
        slaying = False
