"""Puzzle explanation: https://adventofcode.com/2015/day/11"""

from string import ascii_lowercase


def main():
    password = "vzbxkghb"  # -> aaa
    password = list(password)
    while not password_checker(password):
        increment_string(password)
    print("Santa's new password is", "".join(password))
    print("Santa's password has expired")
    increment_string(password)
    while not password_checker(password):
        increment_string(password)
    print("Santa's new password is", "".join(password))


def increment_string(password: list[str]):
    for index, char in enumerate(password[::-1]):
        if char != "z":
            new_char_idx = (ascii_lowercase.index(char) + 1) % 26
            password[-index - 1] = ascii_lowercase[new_char_idx]
            break
        password[-index - 1] = "a"
    if set(password) == set("a"):
        password.append("a")


def password_checker(password):
    if "i" in password or "o" in password or "l" in password:
        return False
    length = len(password)
    # Check for two instances of pairs of letters
    count = 0
    repeating = 0
    for index in range(1, length):
        letter = password[index]
        prev_letter = password[index - 1]
        if prev_letter == letter:
            count += 1
        else:
            count = 0
        if count == 1:
            repeating += 1
    if repeating < 2:
        return False
    # Check for an increasing sequence of 3 letters
    count = 0
    for index in range (1, length):
        if count == 2:
            return True
        letter = password[index]
        prev_letter = password[index - 1]
        if (
            ascii_lowercase.index(prev_letter)
            == ascii_lowercase.index(letter) - 1
        ):
            count += 1
        else:
            count = 0
    return False


if __name__ == "__main__":
    main()
