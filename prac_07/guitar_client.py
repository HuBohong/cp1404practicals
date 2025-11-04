from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Create and display Guitar objects."""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)


def load_guitars(filename):
    guitars = []

    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    guitars.sort()
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


main()
