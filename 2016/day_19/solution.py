from math import floor

x = list(range(1, 3014388, 2))
start = 1
while len(x) != 1:
    length = len(x)
    largest = x[-1]
    b = []
    for idx in range(start, len(x), 2):
        b.append(x[idx])
    if largest == b[-1]:
        start = 1
    else:
        start = 0
    x = b

print(x)

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