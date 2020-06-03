# importing packages and functions
from random import randint
from math import floor
import pandas as pd

# load origins
origins = pd.read_csv("origins.csv")

# load jobs
jobs = pd.read_csv("jobs.csv")

# load weapons
weapons = pd.read_csv("weapons.csv")

# load armours
armours = pd.read_csv("armours.csv")

# load shields
shields = pd.read_csv("shields.csv")


# defining function to get stat bonus from stat
def mod(creature, stat):
    """returns the ability modifier of a specified stat (string) for a creature"""
    return floor(getattr(creature, stat) / 2 - 5)


# defining function to create combatants from combination of origin and job
def create_combatant(chosen_origin, chosen_job):
    """creates a combatant that includes the info from origin and job"""
    combatant = origins[origins.name==chosen_origin]
    combatant.rename(columns={'name':'origin'}, inplace=True)
    combatant['job'] = chosen_job
    combatant['startHP'] = combatant.vit + jobs[jobs.name==chosen_job]['startHP'].iloc[0]
    combatant['currentHP'] = combatant.startHP
    if combatant.origin.iloc[0] == 'monk':
        combatant['dodge'] = mod(combatant, 'agi') + mod(combatant, 'spr') + 2
    else:
        combatant['dodge'] = mod(combatant, 'agi') + shields[shields.name==combatant.shield.iloc[0]]['dodge'].iloc[0] - armours[armours.name==chosen_origin]['encumbrance'].iloc[0] + 2
    combatant['damage'] = weapons[weapons.name==combatant.weapon_1.iloc[0]]['damage'].iloc[0]
    return combatant


combatant1 = create_combatant('knight', 'fighter')
combatant2 = create_combatant('knight', 'fighter')

combatant1_wins = 0
combatant2_wins = 0
double_kill = 0
iteration = 100

for i in range(1, iteration):
    # print(i)
    combatant1.currentHP = combatant1.startHP
    combatant2.currentHP = combatant2.startHP
    # roll initiative
    combatant1_initiative = randint(1, 20) + mod(combatant1, "agi") + randint(1, 9)/10
    combatant2_initiative = randint(1, 20) + mod(combatant2, "agi") + randint(1, 9)/10
    # determine turn order
    if combatant1_initiative > combatant2_initiative:
        player1 = combatant1
        player2 = combatant2
    else:
        player1 = combatant2
        player2 = combatant1
    # begin combat!
    while player1.currentHP.iloc[0] > 0 and player2.currentHP.iloc[0] > 0:
        # player1's turn
        attack = randint(1, 20) + mod(player1, "dex") + 2
        dodge = randint(1, 20) + player2.dodge.iloc[0]
        if attack >= dodge:
            player2.currentHP = player2.currentHP.iloc[0] - randint(1, player1.damage.iloc[0]) + mod(player1, "str")
        # player2's turn
        attack = randint(1, 20) + mod(player2, "dex") + 2
        dodge = randint(1, 20) + player1.dodge.iloc[0]
        if attack >= dodge:
            player1.currentHP = player1.currentHP.iloc[0] - randint(1, player2.damage.iloc[0]) + mod(player2, "str")
    # end combat and record results
    if player2.currentHP <= 0 and player1.currentHP <= 0:
        double_kill = double_kill + 1
    elif player2.currentHP <= 0:
        combatant1_wins = combatant1_wins + 1
    else:
        combatant2_wins = combatant2_wins + 1


print(combatant1_wins / iteration * 100)
print(combatant2_wins / iteration * 100)
print(double_kill / iteration * 100)
