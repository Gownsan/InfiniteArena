# importing packages and functions
from random import randint
from dataclasses import dataclass
from math import floor


# defining classes
# @dataclass
class Stats:
    def __init__(self, STR: int, DEX: int, AGI: int, VIT: int, SPR: int, MND: int):
        self.STR = STR
        self.DEX = DEX
        self.AGI = AGI
        self.VIT = VIT
        self.SPR = SPR
        self.MND = MND


#@dataclass
class DmgType:
    def __init__(self, slash: int, pierce: int, blunt: int, magic: int, fire: int, cold: int, toxic: int, bleed: int, lightning: int, dark: int):
        self.slash = slash
        self.pierce = pierce
        self.blunt = blunt
        self.magic = magic
        self.fire = fire
        self.cold = cold
        self.toxic = toxic
        self.bleed = bleed
        self.lightning = lightning
        self.dark = dark


#@dataclass
class Origin:
    def __init__(self, name: str, stats: Stats, block: DmgType, resist: DmgType, dodge: int, weapon: DmgType, encumbrance: int, passedList: list):
        self.name = name
        self.stats = stats
        self.block = block
        self.resist = resist
        self.dodge = dodge
        self.weapon = weapon
        self.encumbrance = encumbrance
        self.passedList = passedList.append(self)


#@dataclass
class Job:
    def __init__(self, name: str, startHP: int, passedList: list):
        self.name = name
        self.startHP = startHP
        self.passedList = passedList.append(self)


#@dataclass
class Combatant:
    def __init__(self, origin: Origin, job: Job, maxHP: int, currentHP: int):
        self.origin = origin
        self.job = job
        self.maxHP = maxHP
        self.currentHP = currentHP


listOfOrigins = [] # listOfOrigins will contain the list of all 
# created origins so the script can itterate through it
listOfJobs = [] # Idem for jobs

# defining origins
knight = Origin(
    name="knight",
    stats=Stats(14, 12, 8, 16, 10, 12),
    block=DmgType(6, 6, 6, 0, 0, 0, 0, 0, 0, 0),
    resist=DmgType(5, 5, 3, 0, 0, 0, 0, 0, 0, 0),
    dodge=0,
    weapon=DmgType(8, 8, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=3,
    passedList= listOfOrigins # Needed to be passed on to the init function
)

soldier = Origin(
    name="soldier",
    stats=Stats(14, 14, 12, 12, 10, 10),
    block=DmgType(4, 4, 4, 4, 0, 0, 0, 0, 0, 0),
    resist=DmgType(3, 3, 3, 0, 1, 0, 0, 0, 0, 0),
    dodge=1,
    weapon=DmgType(8, 8, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=2,
    passedList= listOfOrigins # Needed to be passed on to the init function
)

warrior = Origin(
    name="warrior",
    stats=Stats(16, 14, 12, 12, 10, 8),
    block=DmgType(4, 4, 4, 4, 0, 0, 0, 0, 0, 0),
    resist=DmgType(2, 2, 2, 0, 0, 4, 0, 0, 0, 0),
    dodge=1,
    weapon=DmgType(8, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=2,
    passedList= listOfOrigins # Needed to be passed on to the init function
)

thief = Origin(
    name="thief",
    stats=Stats(10, 16, 16, 8, 10, 12),
    block=DmgType(4, 4, 4, 0, 0, 0, 0, 0, 0, 0),
    resist=DmgType(1, 1, 1, 0, 0, 0, 3, 0, 0, 0),
    dodge=2,
    weapon=DmgType(4, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=1,
    passedList= listOfOrigins # Needed to be passed on to the init function
)

wanderer = Origin(
    name="wanderer",
    stats=Stats(12, 12, 14, 12, 12, 10),
    block=DmgType(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    resist=DmgType(0, 0, 0, 0, 0, 2, 1, 0, 0, 0),
    dodge=0,
    weapon=DmgType(6, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=0,
    passedList= listOfOrigins # Needed to be passed on to the init function
)

herald = Origin(
    name="herald",
    stats=Stats(11, 11, 12, 14, 14, 10),
    block=DmgType(6, 6, 6, 0, 0, 0, 0, 0, 0, 0),
    resist=DmgType(3, 3, 3, 0, 1, 1, 0, 0, 1, 0),
    dodge=1,
    weapon=DmgType(0, 6, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=2,
    passedList= listOfOrigins # Needed to be passed on to the init function
)

cleric = Origin(
    name="cleric",
    stats=Stats(12, 10, 10, 12, 16, 12),
    block=DmgType(4, 4, 4, 4, 0, 0, 0, 0, 0, 0),
    resist=DmgType(0, 0, 0, 1, 0, 0, 1, 0, 1, 2),
    dodge=1,
    weapon=DmgType(0, 0, 6, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=0,
    passedList= listOfOrigins # Needed to be passed on to the init function
)

sorcerer = Origin(
    name="sorcerer",
    stats=Stats(8, 14, 14, 8, 12, 16),
    block=DmgType(4, 4, 4, 0, 0, 0, 0, 0, 0, 0),
    resist=DmgType(0, 0, 0, 3, 2, 1, 0, 0, 0, 0),
    dodge=2,
    weapon=DmgType(0, 0, 6, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=0,
    passedList= listOfOrigins # Needed to be passed on to the init function
)

pyromancer = Origin(
    name="pyromancer",
    stats=Stats(12, 14, 10, 12, 10, 14),
    block=DmgType(4, 4, 4, 4, 0, 0, 0, 0, 0, 0),
    resist=DmgType(0, 0, 0, 0, 4, 0, 1, 0, 0, 1),
    dodge=1,
    weapon=DmgType(6, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=0,
    passedList= listOfOrigins # Needed to be passed on to the init function
)


# defining jobs
barbarian = Job(
    name="barbarian",
    startHP=24,
    passedList= listOfJobs
)

fighter = Job(
    name="fighter",
    startHP=21,
    passedList= listOfJobs
)

monk = Job(
    name="monk",
    startHP=18,
    passedList= listOfJobs
)

rogue = Job(
    name="rogue",
    startHP=18,
    passedList= listOfJobs
)


# defining function to create combatants from combination of origin and job
def create_combatant(chosen_origin, chosen_job):
    """creates a combatant object from an origin and job"""
    combatant = Combatant(
        origin=chosen_origin,
        job=chosen_job,
        maxHP=chosen_origin.stats.VIT + chosen_job.startHP,
        currentHP=chosen_origin.stats.VIT + chosen_job.startHP
    )
    return combatant


# defining function to get stat bonus from stat
def mod(creature, stat):
    """returns the ability modifier for the specified creature's stat"""
    modifier = floor(getattr(creature.origin.stats, stat) / 2 - 5)
    return modifier


# defining function to roll initiative and determine starting character
def initiative_roll(player0, player1):
    """rolls initiative and returns the starting character (1 or 2)"""
    # roll initiative!
    player0_initiative = randint(1, 20) + mod(player0, "AGI") + getattr(player0.origin.stats, "AGI")/100
    player1_initiative = randint(1, 20) + mod(player1, "AGI") + getattr(player1.origin.stats, "AGI")/100
    # return starting character
    if player0_initiative > player1_initiative:
        return 0
    elif player0_initiative < player1_initiative:
        return 1
    else:
        return randint(0,1)

# Initializing the 4x forLoop 
individualCombos = len(listOfOrigins) * len(listOfJobs)
combatant1Origins = []
combatant1Jobs = []
combatant1VictoryRates = []

comboNumber = 0 #To track which cmbt1 jobs x orgn number this is

for origin1 in listOfOrigins:
    for job1 in listOfJobs:
        combatant1_total_wins = 0

        # set up the list / table values
        combatant1Origins.append(origin1.name)
        combatant1Jobs.append(job1.name)

        for origin2 in listOfOrigins:
            for job2 in listOfJobs:
                
                # creating combatants and the roster of contenders
                combatant1 = create_combatant(origin1, job1)
                combatant2 = create_combatant(origin2, job2)
                pc = [combatant1, combatant2]

                # initiating variables to store the outcomes
                combatant1_wins = 0
                combatant2_wins = 0
                double_kill = 0

                # specifying number of iterations
                iteration = 10


                # let the games ...begin!
                for i in range(1, iteration):

                    # healing combatants to max hp
                    pc[0].currentHP = pc[0].maxHP
                    pc[1].currentHP = pc[1].maxHP

                    # roll initiative!
                    current_turn = initiative_roll(pc[0], pc[1])

                    # as long as both live, the battle rages on...
                    while pc[0].currentHP > 0 and combatant2.currentHP > 0:
                        # ...whose turn is it now?
                        active = current_turn
                        passive = abs(active - 1)
                        # active pc attacks!
                        attack = randint(1, 20) + mod(pc[active], "DEX")
                        # passive pc dodges...?
                        dodge = randint(1, 20) + mod(pc[passive], "AGI") + pc[passive].origin.dodge - pc[passive].origin.encumbrance
                        # if they didn't dodge, passive pc loses HP!
                        if attack >= dodge:
                            #TODO Buggy line to fix with Guillaume
                            print(f"Bug occurs at {origin2.name} and {job2.name}")
                            pc[passive].currentHP = pc[passive].currentHP - randint(1, pc[active].origin.weapon.slash) + mod(pc[active], "STR")
                        # end of active pc's turn
                        current_turn = abs(current_turn -1)


                    if pc[1].currentHP <= 0 and pc[0].currentHP <= 0:
                        double_kill = double_kill + 1
                    elif pc[1].currentHP <= 0:
                        combatant1_total_wins = combatant1_total_wins +1
                        #combatant1_wins = combatant1_wins + 1
                    else:
                        combatant2_wins = combatant2_wins + 1

                #print(combatant1_wins / iteration * 100)
                #print(combatant2_wins / iteration * 100)
                #print(double_kill / iteration * 100)
                

        combatant1VictoryRates.append(combatant1_total_wins)
        print(f"This was the {origin1.name} origin with a {listOfJobs.name} job...")
        comboNumber = comboNumber + 1