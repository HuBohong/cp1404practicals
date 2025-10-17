COLOR_TO_CODE = {"Azure1": "#f0ffff", "Azure2": "#e0eeee", "Azure3": "#c1cdcd", "Azure4": "#838b8b",
                 "Aquamarine1": "#7fffd4", "Aquamarine2": "#76eec6", "Aquamarine4": "#458b74", "Asparagus": "#87a96b",
                 "BabyBlue": "#89cff0", "BabyPink": "#f4c2c2"}


def main():
    """Main function to transfer color to code."""
    user_color = input("Enter color code: ").strip().title().replace(" ", "")
    while user_color != "":
        try:
            print(user_color, "is", COLOR_TO_CODE[user_color])           # user_color = input("Enter color code: ").strip().title().replace(" ", "")
        except KeyError:
            print("Invalid color name")           # user_color = input("Invalid color name please enter correct color code: ").strip().title().replace(" ", "")
        user_color = input("Enter color code: ").strip().title().replace(" ", "")


main()
