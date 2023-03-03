"""Puzzle explanation: https://adventofcode.com/2016/day/10"""

from __future__ import annotations
from re import findall
from typing import Optional, TextIO


def main():
    bot_vals, bot_instructions = parse("2016/day_10/input.txt")
    curr_bot = None
    for bot, vals in bot_vals.items():
        if len(vals) == 2:
            curr_bot = bot_instructions[bot]
    outputs = {}
    bot_num = find_bot(bot_vals, bot_instructions, [curr_bot], outputs)
    print(bot_num)
    print(outputs["0"][0] * outputs["1"][0] * outputs["2"][0])


class Bot:
    def __init__(self, bot_num: str, out_nums: list[str], out_types: list[str]):
        self.bot_num = bot_num
        self.out_nums = out_nums
        self.out_types = out_types


BotVals = dict[str, list[int]]
Bots = dict[str, Bot]


def parse(input_file: str) -> tuple[BotVals, Bots]:
    in_file: TextIO
    bot_vals: BotVals = {}
    bot_instructions: Bots = {}
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


Out = dict[str, list[int]]
BotNum = Optional[str]


def find_bot(
    b_vals: BotVals,
    bots: Bots,
    curr_bots: list[Bot],
    outs: Out,
    bot: BotNum = None,
) -> BotNum:
    curr_bot = curr_bots[0]
    vals = b_vals[curr_bot.bot_num]
    low_val, high_val = min(vals), max(vals)
    low_out, high_out = curr_bot.out_nums
    low_type, high_type = curr_bot.out_types
    next_bot = None

    if low_type == "output":
        add_val_to(outs, low_out, low_val)
    else:
        add_val_to(b_vals, low_out, low_val)
        if len(b_vals[low_out]) == 2:
            curr_bots.append(bots[low_out])

    if high_type == "output":
        add_val_to(outs, high_out, high_val)
    else:
        add_val_to(b_vals, high_out, high_val)
        if len(b_vals[high_out]) == 2:
            curr_bots.append(bots[high_out])

    b_vals[curr_bot.bot_num].clear()
    curr_bots.pop(0)
    next_bot = curr_bots[0]
    if min(b_vals[next_bot.bot_num]) == 17 and max(b_vals[next_bot.bot_num]) == 61:
        bot = next_bot.bot_num
    if outs.get("0") and outs.get("1") and outs.get("2"):
        return bot
    return find_bot(b_vals, bots, curr_bots, outs, bot)


def add_val_to(a_dict, key, val):
    if a_dict.get(key) is None:
        a_dict[key] = [val]
    else:
        a_dict[key].append(val)


if __name__ == "__main__":
    main()
