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

print 'Your final points are: '
print POINTS
