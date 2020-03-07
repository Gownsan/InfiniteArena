# importing packages and functions
from random import randint
from dataclasses import dataclass
from math import floor


# defining classes
@dataclass
class Stats:
    STR: int
    DEX: int
    AGI: int
    VIT: int
    SPR: int
    MND: int


@dataclass
class DmgType:
    slash: int
    pierce: int
    blunt: int
    magic: int
    fire: int
    cold: int
    toxic: int
    bleed: int
    lightning: int
    dark: int


@dataclass
class Origin:
    name: str
    stats: Stats
    block: DmgType
    resist: DmgType
    dodge: int
    weapon: DmgType
    encumbrance: int


@dataclass
class Job:
    name: str
    startHP: int


@dataclass
class Combatant:
    origin: Origin
    job: Job
    maxHP: int
    currentHP: int


# defining origins
knight = Origin(
    name="knight",
    stats=Stats(14, 12, 8, 16, 10, 12),
    block=DmgType(6, 6, 6, 0, 0, 0, 0, 0, 0, 0),
    resist=DmgType(5, 5, 3, 0, 0, 0, 0, 0, 0, 0),
    dodge=0,
    weapon=DmgType(8, 8, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=3
)

soldier = Origin(
    name="soldier",
    stats=Stats(14, 14, 12, 12, 10, 10),
    block=DmgType(4, 4, 4, 4, 0, 0, 0, 0, 0, 0),
    resist=DmgType(3, 3, 3, 0, 1, 0, 0, 0, 0, 0),
    dodge=1,
    weapon=DmgType(8, 8, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=2
)

warrior = Origin(
    name="warrior",
    stats=Stats(16, 14, 12, 12, 10, 8),
    block=DmgType(4, 4, 4, 4, 0, 0, 0, 0, 0, 0),
    resist=DmgType(2, 2, 2, 0, 0, 4, 0, 0, 0, 0),
    dodge=1,
    weapon=DmgType(8, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=2
)

thief = Origin(
    name="thief",
    stats=Stats(10, 16, 16, 8, 10, 12),
    block=DmgType(4, 4, 4, 0, 0, 0, 0, 0, 0, 0),
    resist=DmgType(1, 1, 1, 0, 0, 0, 3, 0, 0, 0),
    dodge=2,
    weapon=DmgType(4, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=1
)

wanderer = Origin(
    name="wanderer",
    stats=Stats(12, 12, 14, 12, 12, 10),
    block=DmgType(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    resist=DmgType(0, 0, 0, 0, 0, 2, 1, 0, 0, 0),
    dodge=0,
    weapon=DmgType(6, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=0
)

herald = Origin(
    name="herald",
    stats=Stats(11, 11, 12, 14, 14, 10),
    block=DmgType(6, 6, 6, 0, 0, 0, 0, 0, 0, 0),
    resist=DmgType(3, 3, 3, 0, 1, 1, 0, 0, 1, 0),
    dodge=1,
    weapon=DmgType(0, 6, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=2
)

cleric = Origin(
    name="cleric",
    stats=Stats(12, 10, 10, 12, 16, 12),
    block=DmgType(4, 4, 4, 4, 0, 0, 0, 0, 0, 0),
    resist=DmgType(0, 0, 0, 1, 0, 0, 1, 0, 1, 2),
    dodge=1,
    weapon=DmgType(0, 0, 6, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=0
)

sorcerer = Origin(
    name="sorcerer",
    stats=Stats(8, 14, 14, 8, 12, 16),
    block=DmgType(4, 4, 4, 0, 0, 0, 0, 0, 0, 0),
    resist=DmgType(0, 0, 0, 3, 2, 1, 0, 0, 0, 0),
    dodge=2,
    weapon=DmgType(0, 0, 6, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=0
)

pyromancer = Origin(
    name="pyromancer",
    stats=Stats(12, 14, 10, 12, 10, 14),
    block=DmgType(4, 4, 4, 4, 0, 0, 0, 0, 0, 0),
    resist=DmgType(0, 0, 0, 0, 4, 0, 1, 0, 0, 1),
    dodge=1,
    weapon=DmgType(6, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    encumbrance=0
)


# defining jobs
barbarian = Job(
    name="barbarian",
    startHP=24
)

fighter = Job(
    name="fighter",
    startHP=21
)

monk = Job(
    name="monk",
    startHP=18
)

rogue = Job(
    name="rogue",
    startHP=18
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


# creating combatants
combatant1 = create_combatant(knight, fighter)
combatant2 = create_combatant(knight, fighter)


# initiating variables to store the outcomes
combatant1_wins = 0
combatant2_wins = 0
double_kill = 0


# specifying number of iterations
iteration = 10000


# let the games ...begin!
for i in range(1, iteration):

    # healing combatants to max hp
    combatant1.currentHP = combatant1.maxHP
    combatant2.currentHP = combatant2.maxHP

    # roll initiative!
    combatant1_initiative = randint(1, 20) + mod(combatant1, "AGI")
    combatant2_initiative = randint(1, 20) + mod(combatant2, "AGI")

    # as long as both live, the battle rages on...
    while combatant1.currentHP > 0 and combatant2.currentHP > 0:
        attack = randint(1, 20) + floor(combatant1.origin.stats.DEX / 2 - 5) + 2
        dodge = randint(1, 20) + floor(combatant2.origin.stats.AGI / 2 - 5) + 2 - combatant2.origin.encumbrance
        if attack >= dodge:
            combatant2.currentHP = combatant2.currentHP - randint(1, combatant1.origin.weapon.slash) + combatan


    if combatant2.currentHP <= 0 and combatant1.currentHP <= 0:
        double_kill = double_kill + 1
    elif combatant2.currentHP <= 0:
        combatant1_wins = combatant1_wins + 1
    else:
        combatant2_wins = combatant2_wins + 1

print(combatant1_wins / iteration * 100)
print(combatant2_wins / iteration * 100)
print(double_kill / iteration * 100)
