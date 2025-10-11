"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

NUMBER_LENGTH = 5
USERNAME = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
            'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    """ function call for check username and validation """
    numbers = get_valid_number(NUMBER_LENGTH)
    print_info(numbers)
    user_name = input("please enter your username")
    check_username(USERNAME, user_name)


def get_valid_number(number_length):
    """ get a valid number list """
    numbers = []
    for i in range(number_length):
        is_valid = False
        while not is_valid:
            try:
                number = int(input("Numbers: "))
                numbers.append(number)
                is_valid = True
            except ValueError:
                print("Invalid number")
    return numbers


def print_info(numbers):
    """ Print the required format """
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of number is {sum(numbers) / len(numbers)}")


def check_username(USERNAME , user_name):
    """ check user input """
    if user_name not in USERNAME:
        print("Access denied")
    else:
        print("Access granted")

main()
