
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Create and display Guitar objects."""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)
    user_guitar = get_user_guitar()
    guitars.append(user_guitar)
    write_file(guitars)

def load_guitars(filename) -> list:
    """Load guitars from a file and return a list of Guitar objects."""
    guitars = []

    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    guitars.sort()
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for guitar in guitars:
        print(guitar)


def get_user_guitar() -> Guitar:
    """Get guitar details from user input."""
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    user_guitar = Guitar(name, year, cost)
    print(f"You have added: {user_guitar}")
    return user_guitar

def write_file(guitars):
    """Write the list of guitars to a file."""
    with open(FILENAME,"w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}",file=out_file)

main()
