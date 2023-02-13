from collections import Counter, deque
from re import findall
from strings import ascii_lower
from typing import TextIO

RoomCodes = list[tuple[str, str, str]]
Checker = list[tuple[str, tuple[str, int]]]


def main():
    rooms = parse("2016/day_04/input.txt")
    part_1 = find_real_rooms(rooms)
    print(part_1)


def parse(input_file: str) -> RoomCodes:
    in_file: TextIO
    with open(input_file, encoding="utf-8") as in_file:
        regex: str = r"([a-z-]+)(\d+)(\[[a-z]+\])"
        input_data: RoomCodes = [findall(regex, line)[0] for line in in_file]
    rooms: RoomCodes = []
    for line in input_data:
        name, room_id, check_sum = line
        stripped_name = tuple(findall(r"[^-]", name))
        int_room_id = int(room_id)
        room = stripped_name, int_room_id, check_sum
        rooms.append(room)
    return rooms


def find_real_rooms(rooms: RoomCodes):
    id_sum = 0
    for room in rooms:
        name, room_id, check_sum = room
        check_sum = check_sum.strip("[]")
        char_counter = Counter(name)
        char_counts = sorted(char_counter.items(), key=lambda x: x[1], reverse=True)
        print(char_counts)
        char_counts = [[char, amt] for char, amt in char_counts]
        secondary_sort(char_counts)
        print(char_counts)
        letters = "".join([char for char, _ in char_counts])[:5]
        if letters == check_sum:
            id_sum += room_id
    return id_sum
            



def secondary_sort(letters):
    """Sort the characters with the same count"""
    for idx in range(1, len(letters)):
        char, count = letters[idx]
        if count == letters[idx - 1][1]:
            pos = idx - 1
            while 0 <= pos and char < letters[pos][0] and count == letters[pos][1]:
                letters[pos + 1] = letters[pos]
                pos -= 1
            letters[pos + 1] = [char, count]

def decrypt(rooms):
    pass


if __name__ == "__main__":
    main()
