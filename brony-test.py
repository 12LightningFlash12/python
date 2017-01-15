POINTS = 0
name = raw_input('Please enter your name: ')

print 'Hello, {0} and welcome to The Brony Test.\n'.format(name)

print 'Here is your first Question: '
q1 = raw_input('Who is the creator of MLP Generation 4? ')

if q1 == 'Lauren Faust' or q1 == 'lauren faust':
    print 'Correct\n'
    POINTS += 1
    print 'Points: '
    print POINTS
else:
    print 'Wrong\n'
    POINTS -= 1
    print 'Points: '
    print POINTS

print '\n'


print 'Here is your second Question: '
q2 = raw_input('Who voice acts Princess Luna? ')

if q2 == 'Tabitha St. Germain':
    print 'Correct\n'
    POINTS += 1
    print 'Points: '
    print POINTS
else:
    print 'Wrong\n'
    POINTS -= 1
    print 'Points: '
    print POINTS

print '\n'


print 'Here is your third Question: '
q3 = raw_input('What was the original release date for MLP FIM season one? (use mm/dd/yy format) ');

if q3 == '10/10/10':
    print 'Correct\n'
    POINTS += 1
    print 'Points: '
    print POINTS
else:
    print 'Wrong\n'
    POINTS -= 1
    print 'Points: '
    print POINTS
    
print'\n'


print 'Here is your fourth Question: '
q4 = raw_input('Who is the newest princess of Equestria? ')

if q4 == 'princess twilight' or q4 == 'Princess Twilight':
    print 'Correct\n'
    POINTS += 1
    print 'Points: '
    print POINTS
else:
    print 'Wrong\n'
    POINTS -= 1
    print 'Points: '
    print POINTS

print '\n'


print 'Here is your fifth Question: '
q5 = raw_input('What is Celestia\'s filly name? ')

if q5 == 'Tia' or q5 == 'tia':
    print 'Correct\n'
    POINTS += 1
    print 'Points: '
    print POINTS
else:
    print 'Wrong\n'
    POINTS -= 1
    print 'Points: '
    print POINTS

print '\n'


print 'Here is your sixth Question: '
q6 = raw_input('What is Luna\'s filly name? ')

if q6 == 'lulu' or q6 == 'Lulu':
    print 'Correct\n'
    POINTS += 1
    print 'Points: '
    print POINTS
else:
    print 'Wrong\n'
    POINTS -= 1
    print 'Points: '
    print POINTS

print '\n'


print 'Here is your seventh Question: '
q7 = raw_input('What is Trixie\'s full name? ')

if q7 == 'Trixie Lulamoon' or q7 == 'trixie lulumoon':
    print 'Correct\n'
    POINTS += 1
    print 'Points: '
    print POINTS
else:
    print 'Wrong\n'
    POINTS -= 1
    print 'Points: '
    print POINTS

'''
print 'Your final points are: '
print POINTS

if POINTS <= 20 and POINTS >= 16:
    print ''
elif POINTS <= 15 and POINTS >= 11:
    print ''
elif POINTS <= 10 and POINTS >=6:
    print ''
else:
    print ''
'''
