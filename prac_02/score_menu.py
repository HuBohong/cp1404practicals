"""
CP1404 - Practical
HuBohong
Program of score menu

"""

MENU = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result (copy or import your function to determine the result from score.py)\n(S)how stars (this should print as many stars as the score)\n(Q)uit"


def main():

    user_score = 0
    print(MENU)
    user_choice = input("please select the function:").upper()
    while user_choice != "Q":
        if user_choice == "G":
            user_score = get_valid_score()
        elif user_choice == "P":
            score_level = determine_score(user_score)
            print(f"Your score level is {score_level}")
        elif user_choice == "S":
            print("*" * user_score)
        else:
            print("Invalid option please select again")

        print(MENU)
        user_choice = input("please select the function:").upper()

    print("Thank you bye.")


def get_valid_score():
    """get a valid score"""
    user_score = int(input("please enter a score between 0 and 100:"))
    while user_score < 0 or user_score > 100:
        print("invalid score please enter again")
        user_score = int(input("please enter a score between 0 and 100:"))
    return user_score


def determine_score(user_score: int):
    """Determine the score level"""
    if user_score < 0 or user_score > 100:
        return "Invalid score"
    elif user_score >= 90:
        return "Excellent"
    elif user_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
