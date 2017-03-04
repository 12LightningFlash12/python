import random

uH = 10
eH = 50
slaying = True


while slaying:
    atk = raw_input("Attack Y or N? ")
    damage = random.randint(10, 20)
    eDamage = random.randint(0, 5)
    if atk == "y" or atk == "Y":
        print "You attack with %s damage!" % (damage)
        eH = eH - damage
    if atk == "n" or atk == "N":
        print "You stand your groung and take %s damage from the enemy" % (eDamage)
        uH = uH - eDamage
    print "User Health: %s" % (uH)
    print "Enemy Health : %s" % (eH)
    
    if uH <= 0:
        slaying = False
    
    if eH <= 0:
        slaying = False
