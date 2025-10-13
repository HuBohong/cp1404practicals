COLOR_TO_CODE = {"Azure1": "#f0ffff", "Azure2": "#e0eeee", "Azure3": "#c1cdcd", "Azure4": "#838b8b",
                 "Aquamarine1": "#7fffd4", "Aquamarine2": "#76eec6", "Aquamarine4": "#458b74", "Asparagus": "#87a96b",
                 "Baby Blue": "#89cff0", "Baby Pink": "#f4c2c2"}


def main():
    user_color = get_valid_color()
    print_color_code(user_color)

def get_valid_color():
    user_color = input("Enter color code: ").title()
    while user_color not in COLOR_TO_CODE:
        print("Invalid color name")
        user_color = input("Enter color code: ").title()

    return user_color

def print_color_code(user_color):
    print(f"{user_color} color code is {COLOR_TO_CODE[user_color]}")

main()
