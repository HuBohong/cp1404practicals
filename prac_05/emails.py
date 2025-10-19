"""
CP1404/CP5632 Practical 5
email practice
estimate:40min
actual:35min
"""
EMAIL_SIGN = "@"


def main():
    """Get email and name mapping."""
    email_to_name = {}
    user_email = input("Enter your email address: ").strip()
    while user_email != "":
        user_email = get_validate_email(user_email)
        user_name = get_user_name(user_email)
        email_to_name[user_email] = user_name
        user_email = input("Enter your email address: ")
    print_email_to_name(email_to_name)


def get_validate_email(user_email):
    """ Validate user email address."""
    while EMAIL_SIGN not in user_email:
        user_email = input("Please enter a correct email address:").strip()
    return user_email


def get_user_name(user_email):
    """Get user's name from email or input."""
    user_name = user_email.strip().replace(".", " ").split("@")[0].title()
    is_username = input(f"Is your name {user_name}? (Y/n)")
    if is_username.upper() == "Y":
        return user_name
    else:
        user_name = input("Please enter your name").title()
        return user_name

def print_email_to_name(email_to_name):
    """Print email to name mapping."""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
