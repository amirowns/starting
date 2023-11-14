"""
Can you create a function using python that returns the name of the winner in a fight between two fights?
Each fighter takes turns attacking the other and whoever kills the other first is victorious.
Death is defined as having health <= 0.
Each fighter will be a Fighter object/instance.
Both health and damage_per_attack will be integers larger than 0.
You can mutate the Fighter objects.
Your function also receives a third argument, a string, with the name of the fighter that attacks first.
Here is the Fighter class:
"""


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__


# muffin
def declare_winner(fighter1, fighter2, first_attacker):
    current_attacker = first_attacker
    while True:
        if current_attacker == fighter1.name:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            current_attacker = fighter2.name
        else:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            current_attacker = fighter1.name


# banana
def declare_winner2(fighter1, fighter2, first_attacker):
    curr_attacker = first_attacker
    while True:
        if curr_attacker == fighter1.name:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            curr_attacker = fighter2.name
        else:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            curr_attacker = fighter1.name


# better 
def declare_winner3(fighter1, fighter2, first_attacker):
    current, opponent = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while current.health > 0:        
        opponent.health -= current.damage_per_attack
        current, opponent = opponent, current
    return opponent.name

print(declare_winner3(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"))