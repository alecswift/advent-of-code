"""Puzzle explanation: https://adventofcode.com/2016/day/19
Related video: https://www.youtube.com/watch?v=uCsD3ZGzMgE
"""

from math import log2

y = ((3014387 - 2**(int(log2(3014327)))) * 2) + 1
print(y)

x = list(range(1, 3014388))
curr_idx = 0
while 1 < len(x):
    length = len(x)
    if length % 10000 == 0:
        print(length)
    steal = int((length // 2) + curr_idx)
    if length <= steal:
        steal %= len(x)
    else:
        curr_idx += 1
    x.pop(steal)
    curr_idx %= len(x)

print(x)