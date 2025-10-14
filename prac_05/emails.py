"""
CP1404/CP5632 Practical 5
email practice
estimate:40min
actual:
"""
EMAIL_SIGN = "@"


def main():
    email_to_name = {}
    user_email = input("Enter your email address: ")
    while user_email != "":
        user_email = get_validate_email(user_email)
        user_name = get_user_name(user_email)
        email_to_name[user_email] = user_name

        user_email = input("Enter your email address: ")


def get_validate_email(user_email):
    while EMAIL_SIGN not in user_email:
        user_email = input("Please enter a correct email address:")
    return user_email


def get_user_name(user_email):
    user_name = user_email.strip().replace(".", " ").split("@")[0].title()
    is_username = input(f"Is your name {user_name}? (Y/n)")
    if is_username.upper() == "Y":
        return user_name
    else:
        user_name = input("Please enter your name").title()
        return user_name


main()
