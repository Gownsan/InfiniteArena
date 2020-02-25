from random import randint

combatant1HP = 10
combatant2HP = 10

while combatant1HP > 0 & combatant2HP > 0:
    combatant1HP = combatant1HP - randint(0, 3)
    combatant2HP = combatant2HP - randint(0, 3)

if combatant1HP <= 0:
    print("Winner is combatant 2")
else:
    print("Winner is combatant 1")
