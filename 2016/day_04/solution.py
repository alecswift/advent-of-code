from collections import Counter, deque
from re import findall
from string import ascii_lowercase
from typing import TextIO

Checker = list[tuple[str, tuple[str, int]]]


def main():
    rooms = parse("2016/day_04/input.txt")
    part_1 = find_real_rooms(rooms)
    print(part_1)
    part_2 = decrypt(rooms)
    print(part_2)


def parse(input_file: str) -> list:
    in_file: TextIO
    with open(input_file, encoding="utf-8") as in_file:
        regex: str = r"([a-z-]+)(\d+)(\[[a-z]+\])"
        input_data: list = [findall(regex, line)[0] for line in in_file]
    rooms: list = []
    for line in input_data:
        name, room_id, check_sum = line
        stripped_name: tuple = tuple(findall(r"[^-]", name))
        int_room_id: int = int(room_id)
        room = stripped_name, int_room_id, check_sum
        rooms.append(room)
    return rooms


def find_real_rooms(rooms: list) -> int:
    id_sum: int = 0
    for room in rooms:
        name, room_id, check_sum = room
        check_sum = check_sum.strip("[]")
        char_counts: list = [[char, amt] for char, amt in Counter(name).items()]
        char_counts.sort(key=lambda x: x[1], reverse=True)
        secondary_sort(char_counts)
        letters: str = "".join([char for char, _ in char_counts])[:5]
        if letters == check_sum:
            id_sum += room_id
    return id_sum


def secondary_sort(letters: list[list]) -> None:
    """Sort the characters with the same count"""
    for idx in range(1, len(letters)):
        char, count = letters[idx]
        if count == letters[idx - 1][1]:
            pos: int = idx - 1
            while 0 <= pos and char < letters[pos][0] and count == letters[pos][1]:
                letters[pos + 1] = letters[pos]
                pos -= 1
            letters[pos + 1] = [char, count]


def decrypt(rooms) -> int:
    alphabet: deque = deque(ascii_lowercase)
    for name, room_id, _ in rooms:
        decrypted_name_lst: list[str] = []
        for char in name:
            pos: int = alphabet.index(char)
            alphabet.rotate(-room_id)
            decrypted_name_lst.append(alphabet[pos])
        decrypted_name: str = "".join(decrypted_name_lst)
        if "northpole" in decrypted_name:
            return room_id
    return -1


if __name__ == "__main__":
    main()
