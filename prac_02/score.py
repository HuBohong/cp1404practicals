"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from random import randint


def main():
    score = float(input("Enter score: "))
    score_level = determine_score(score)
    print(f"Your score is {score_level}")

    random_score = randint(1, 101)
    random_score_level = determine_score(random_score)
    print(f"Your random score level is {random_score_level} with score of {random_score}")


def determine_score(score):
    """Determine the score level"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
