"""
Finds the total score for a rock, paper, scissor tournament given the input file
"""
import re
from typing import TextIO


def parse(input_file: str) -> list[tuple[str, str]]:
    """
    Returns a list of tuples of each rock, paper, scissors round
    from a given input file
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    parsed_data: list[tuple[str, str]] = re.findall(r"([A-C]) ([X-Z])", input_data)
    return parsed_data


def total_score(input_file: str) -> int:
    """
    Return my total score from an input file containing
    the rock paper scissors tournament results
    """
    results: list[tuple[str, str]] = parse(input_file)
    shape_scores: dict[str, int] = {"X": 1, "Y": 2, "Z": 3}
    outcome_scores: dict[tuple[str, str], int] = {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,
        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 3,
    }
    outcome_scores_2: dict[tuple[str, str], tuple[int, int]] = {
        ("A", "X"): (0, 3),
        ("A", "Y"): (3, 1),
        ("A", "Z"): (6, 2),
        ("B", "X"): (0, 1),
        ("B", "Y"): (3, 2),
        ("B", "Z"): (6, 3),
        ("C", "X"): (0, 2),
        ("C", "Y"): (3, 3),
        ("C", "Z"): (6, 1),
    }
    score: int = 0
    score_2: int = 0
    for game in results:
        score += shape_scores[game[1]]
        score += outcome_scores[game]
        score_2 += sum(outcome_scores_2[game])
    return score, score_2

print(total_score("2022/day_2/input.txt"))
