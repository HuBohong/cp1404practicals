from prac_06.guitar import Guitar


def main():
    pass


def get_guitars():
    guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: ").replace("$", ""))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        guitar_name = input("Name: ")
    return guitars


main()
