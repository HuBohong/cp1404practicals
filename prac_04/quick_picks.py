from random import randint

COLUMN_COUNT = 6
MAX_NUMBER = 45
MIN_NUMBER = 1
NUMBER_WIDTH = 2


def main():
    """ """
    valid_number = get_valid_picks()
    numbers = generate_numbers(valid_number)
    print_in_format(numbers)


def get_valid_picks():
    """ """
    is_valid = False
    while not is_valid:
        try:
            user_input = int(input(f"how many ""quick picks"" you wish to generate:"))
            if user_input > 0:
                is_valid = True
            else:
                print("Wrong input")
        except ValueError:
            print("Wrong input")
    return user_input


def generate_numbers(user_number):
    """ """
    numbers = [[] for i in range(user_number)]
    for i in range(user_number):
        while len(numbers[i]) < COLUMN_COUNT:
            random_number = randint(MIN_NUMBER, MAX_NUMBER)
            if random_number not in numbers[i]:
                numbers[i].append(random_number)
        numbers[i].sort()

    return numbers


def print_in_format(numbers):
    """ """

    for i in range(len(numbers)):
        print(" ".join(f"{number:{NUMBER_WIDTH}}" for number in numbers[i]))

        # for j in range(COLUMN_COUNT):
            # print(f"{numbers[i][j]:{NUMBER_WIDTH}}",end=" ")
        # print()


main()
