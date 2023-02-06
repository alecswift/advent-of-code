"""Puzzle explanation: https://adventofcode.com/2015/day/22"""

from random import randint
# Hit Points: 58
# Damage: 9

class Boss:

    def __init__(self, hp, damage):
        self._hp = hp
        self._damage = damage

    def get_hp(self):
        return self._hp

    def get_damage(self):
        return self._damage

    def lose_hp(self, amount):
        self._hp -= amount

class Wizard:

    def __init__(self):
        self._hp = 50
        self._mana = 500
        # implement stoppers for moves when mana is out
        self._armor = 0

    def get_hp(self):
        return self._hp

    def take_damage(self, boss):
        damage = boss.get_damage()
        if damage <= self._armor:
            self._hp -= 1
        else:
            self._hp -= boss.get_damage() - self._armor

    def magic_missile(self, boss):
        self._mana -= 53
        boss.lose_hp(4)

    def drain(self, boss):
        # can you heal above 50??
        self._hp += 2
        boss.lose_hp(2)
    
    # have to decide how to deal with turned base effects
    # Shield, poison, recharge
    
# dynamic programming
# state is data members of boss object and data members of wizard object
# for the turned base game

# subproblem to recursively implement to find all paths then find the path with the min mana
# for move in moveset, chose move, implement turn boss and wizards data members change
# choose another move (if a turn based move is activated keep track of the
# turns and don't use the move again until the counter is over)
# Repeat this process until one of the character's is dead
# only keep track of paths where the wizard wins
# keep track of the minimum amount of mana utilized so far and
# only continue path if you have used less mana than the minimum

def fight_simulator(wizard, boss):
    # can I get the names of wizard class methods another way
    # rather than hardcoding?
    wizard_moves = [
        "magic_missile",
        "drain"
    ]
    # currently simulating 1 fight with random moves, will iterate recursively over paths later
    while 0 < wizard.get_hp() and 0 < boss.get_hp():
        getattr(w1, wizard_moves[randint(0,1)])(b1)
        wizard.take_damage(b1)

    return boss.get_hp() <= 0
        




w1 = Wizard()
b1 = Boss(21, 9)
print(fight_simulator(w1, b1))