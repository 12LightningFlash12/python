import random

uCh = raw_input('Rock, paper, or scissors? ')
cCh = random.randint(0, 30)

if(cCh < 10):
    cCh = 'rock'
elif(cCh < 20):
    cCh = 'paper'
else:
    cCh = 'scissors'

def compare(uCh, cCh):
    if(uCh == cCh):
        print 'The result is a tie'
    elif(uCh == 'rock'):
        if(cCh == 'scissors'):
            print 'rock wins'
        else:
            print 'paper wins'
    elif(uCh == 'paper'):
        if(cCh == 'rock'):
            print 'paper wins'
        else:
            print 'scissors wins'
    elif(uCh == 'scissors'):
        if(cCh == 'rock'):
            print 'rock wins'
        else:
            print 'scissors win'

print('Usr choice: {0}'.format(uCh))
print('Computer choice: {0}'.format(cCh))

compare(uCh, cCh)
