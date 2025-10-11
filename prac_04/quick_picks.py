"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

from random import randint

COLUMN_COUNT = 6
MAX_NUMBER = 45
MIN_NUMBER = 1
NUMBER_WIDTH = 2


def main():
    """ main logic for function call """
    valid_pick = get_valid_picks()
    picks = generate_pick_numbers(valid_pick)
    print_picks(picks)


def get_valid_picks():
    """ get a valid user input """
    is_valid = False
    while not is_valid:
        try:
            user_input = int(input(f"how many 'quick picks' you wish to generate:"))
            if user_input > 0:
                is_valid = True
            else:
                print("Wrong input")
        except ValueError:
            print("Wrong input")
    return user_input


def generate_pick_numbers(user_number):
    """ generate picks """
    # random.sample
    # numbers = [[] for i in range(user_number)]
    picks = []
    for i in range(user_number):
        random_numbers = set()
        while len(random_numbers) < COLUMN_COUNT:
            random_numbers.add(randint(MIN_NUMBER, MAX_NUMBER))
            # if random_number not in numbers[i]:
            #     numbers[i].append(random_number)
        # numbers[i].sort()
        picks.append(sorted(random_numbers))

    return picks


def print_picks(picks):
    """ printout picks in format """

    for i in range(len(picks)):
        print(" ".join(f"{number:{NUMBER_WIDTH}}" for number in picks[i]))

        # for j in range(COLUMN_COUNT):
        # print(f"{numbers[i][j]:{NUMBER_WIDTH}}",end=" ")
        # print()


main()
