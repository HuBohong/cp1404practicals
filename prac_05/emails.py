"""
CP1404/CP5632 Practical 5
email practice
estimate:40min
actual:
"""
EMAIL_SIGN = "@"


def main():
    email_to_name = {}
    get_user_info(email_to_name)


def get_user_info(email_to_name):
    user_email = input("Enter your email address: ")
    while EMAIL_SIGN not in user_email:
        user_email = input("Please enter a correct email address")

    while user_email != "":
        user_name = user_email.strip().replace(".", " ").split("@")[0].title()



main()
