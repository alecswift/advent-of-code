"""Puzzle explanation: https://adventofcode.com/2016/day/10"""

from re import findall
from typing import TextIO


def main():
    bot_vals, bot_instructions = parse("2016/day_10/input.txt")
    curr_bot = None
    for bot, vals in bot_vals.items():
        if len(vals) == 2:
            curr_bot = bot_instructions[bot]
    bot_num, outputs = find_bot(bot_vals, bot_instructions, [curr_bot], {})
    print(bot_num)
    print(outputs["0"][0] * outputs["1"][0] * outputs["2"][0])


# first carry out the instructions that initialize bot with
# values. Also, add instructions to dict with key: value = bot num: (low, high)
# find bots with two values (have a full bot stack) and execute their instructions checking the values they
# have until we find the ones we're looking for


class Bot:
    def __init__(self, bot_num, out_nums, out_types):
        self.bot_num = bot_num
        self.out_nums = out_nums
        self.out_types = out_types


def parse(input_file: str) -> list[str]:
    in_file: TextIO
    bot_vals = {}
    bot_instructions = {}
    with open(input_file, encoding="utf-8") as in_file:
        for line in in_file:
            if "value" in line:
                val, bot_num = findall(r"\d+", line)
                if bot_vals.get(bot_num):
                    bot_vals[bot_num].append(int(val))
                else:
                    bot_vals[bot_num] = [int(val)]
            else:
                num, out_low, out_high = findall(r"[a-z]+ \d+", line)
                _, bot_num = num.split(" ")
                type_low, num_low = out_low.split(" ")
                type_high, num_high = out_high.split(" ")
                bot = Bot(bot_num, [num_low, num_high], [type_low, type_high])
                bot_instructions[bot_num] = bot
    return bot_vals, bot_instructions


def find_bot(bot_vals, bot_instructions, curr_bots, outputs, bot=None):
    curr_bot = curr_bots[0]
    vals = bot_vals[curr_bot.bot_num]
    low_val = min(vals)
    high_val = max(vals)
    low_out, high_out = curr_bot.out_nums
    low_type, high_type = curr_bot.out_types
    next_bot = None

    if low_type == "output":
        add_val_to(outputs, low_out, low_val)
    else:
        add_val_to(bot_vals, low_out, low_val)
        if len(bot_vals[low_out]) == 2:
            curr_bots.append(bot_instructions[low_out])

    if high_type == "output":
        add_val_to(outputs, high_out, high_val)
    else:
        add_val_to(bot_vals, high_out, high_val)
        if len(bot_vals[high_out]) == 2:
            curr_bots.append(bot_instructions[high_out])

    bot_vals[curr_bot.bot_num].clear()
    curr_bots.pop(0)
    next_bot = curr_bots[0]
    if min(bot_vals[next_bot.bot_num]) == 17 and max(bot_vals[next_bot.bot_num]) == 61:
        bot = next_bot
    if outputs.get("0") and outputs.get("1") and outputs.get("2"):
        return bot.bot_num, outputs
    return find_bot(bot_vals, bot_instructions, curr_bots, outputs, bot)


def add_val_to(a_dict, key, val):
    if a_dict.get(key) is None:
        a_dict[key] = [val]
    else:
        a_dict[key].append(val)


if __name__ == "__main__":
    main()
