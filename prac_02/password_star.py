"""
CP1404/CP5632 Practical
HuBohong
Program to get a valid password and display it as stars

"""
MIN_PASSWORD_LENGTH = 6


def main():
    user_password = get_password()
    while len(user_password) < MIN_PASSWORD_LENGTH:
        print("invalid password")
        user_password = get_password()
    print_star(user_password)


def print_star(user_password: str):
    """print stars according to the length of the password"""
    print("*" * len(user_password))


def get_password() -> str:
    """get a valid password"""
    user_password = input("please enter a valid password:")
    return user_password


main()
