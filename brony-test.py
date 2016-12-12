POINTS = 0
name = raw_input('Please enter your name: ')

print 'Hello, {0} and welcome to The Brony Test.\n'.format(name)

print 'Hre is your first Question: '

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

print '\n'


q4 = raw_input("What is the name of Rarity's boulder")

if q4 == 'Tom' or q4 == 'tom':
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


print 'Your final points are: '
print POINTS

print '\n'

if POINTS <= 20 and POINTS >= 16:
    print ''
elif POINTS <= 15 and POINTS >= 11:
    print ''
elif POINTS <= 10 and POINTS >=6:
    print ''
else:
    print ''
