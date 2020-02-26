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

# defining jobs
fighter = Job(
    name="fighter",
    startHP=21
)


# defining function to create combatants from combination of origin and job
def create_combatant(chosen_origin, chosen_job):
    combatant = Combatant(
        origin=chosen_origin,
        job=chosen_job,
        maxHP=chosen_origin.stats.VIT + chosen_job.startHP,
        currentHP=chosen_origin.stats.VIT + chosen_job.startHP
    )
    return combatant


# defining function to get stat bonus from stat
def mod(creature, stat):
    '''returns the ability modifier '''
    floor(getattr(creature.origin.stats, "DEX") / 2 - 5)


combatant1 = create_combatant(knight, fighter)
combatant2 = create_combatant(knight, fighter)

combatant1_wins = 0
combatant2_wins = 0
double_kill = 0
iteration = 10000

for i in range(1, iteration):
    # print(i)
    combatant1.currentHP = combatant1.maxHP
    combatant2.currentHP = combatant2.maxHP

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
