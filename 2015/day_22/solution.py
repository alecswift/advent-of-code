"""Puzzle explanation: https://adventofcode.com/2015/day/22"""

# Hit Points: 58
# Damage: 9

    
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

# return function if move is a current prolonged effect.
# return if one of the characters died
# return mana is greater than the current min mana
# states: (wizhp, bosshp, mana, visited, counters)

class MinManaSpent:

    def __init__(self, min_mana_spent=None):
        self.min_mana_spent = min_mana_spent

def rec_fight_simulator(wizhp, wizarmour, mana, bosshp, visited, mana_spent, min_inst=None):
    # can I get the names of wizard class methods another way
    # rather than hardcoding?
    wizard_moves = [
        ("magic_missile", 53),
        ("drain", 73),
        ("shield", 113),
        ("poison", 173),
        ("recharge", 229)
    ]
    shield_visited, poison_visited, recharge_visited = visited
    # currently simulating 1 fight with random moves, will iterate recursively over paths later
    for move, mana_cost in wizard_moves:
        # wiz turn
        if shield_visited is not None:
            if shield_visited == 0:
                wizarmour = 0
                shield_visited = None
            else:
                shield_visited -= 1
        if poison_visited is not None:
            if poison_visited == 0:
                poison_visited = None
            else:
                bosshp -= 3
                poison_visited -= 1
        if recharge_visited is not None:
            if recharge_visited == 0:
                recharge_visited = None
            else:
                mana += 101
                recharge_visited -= 1

        if mana < mana_cost:
            return

        if move == "magic_missile":
            bosshp -= 4
            mana -= mana_cost
            mana_spent += mana_cost
        elif move == "drain":
            bosshp -= 2
            wizhp += 2
            mana -= mana_cost
            mana_spent += mana_cost
        elif move == "shield":
            if shield_visited is not None:
                return
            wizarmour += 7
            shield_visited = 6
            mana -= mana_cost
            mana_spent += mana_cost
        elif move == "poison":
            if poison_visited is not None:
                return
            poison_visited = 6
            mana -= mana_cost
            mana_spent += mana_cost
        elif move == "recharge":
            if recharge_visited is not None:
                return
            recharge_visited = 5
            mana -= mana_cost
            mana_spent += mana_cost

        if min_inst.min_mana_spent is not None and min_inst.min_mana_spent <= mana_spent:
            return

        if bosshp <= 0:
            if min_inst.min_mana_spent is None:
                min_inst.min_mana_spent = mana_spent
            elif mana_spent < min_inst.min_mana_spent:
                min_inst.min_mana_spent = mana_spent
            return min_inst.min_mana_spent
        # boss turn
        if shield_visited is not None:
            if shield_visited == 0:
                wizarmour = 0
                shield_visited = None
            else:
                shield_visited -= 1
        if poison_visited is not None:
            if poison_visited == 0:
                poison_visited = None
            else:
                bosshp -= 3
                poison_visited -= 1
        if recharge_visited is not None:
            if recharge_visited == 0:
                recharge_visited = None
            else:
                mana += 101
                recharge_visited -= 1

        if 9 <= wizarmour:
            wizhp -= 1
        else:
            wizhp -= (8 - wizarmour)

        if wizhp <= 0:
            return None

        visited = (shield_visited, poison_visited, recharge_visited)
        rec_fight_simulator(wizhp, wizarmour, mana, bosshp, visited, mana_spent, min_inst)

    return min_inst.min_mana_spent

min_mana_spent_my_input = MinManaSpent()
print(rec_fight_simulator(10, 0, 250, 13, (None, None, None), 0, min_mana_spent_my_input))
