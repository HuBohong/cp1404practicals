"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """ """
    classes = load_data(FILENAME)
    print_info(classes)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    pairs = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        pairs.append(parts)  # append list to pairs list
    input_file.close()
    return pairs


def print_info(classes: list):
    """ """
    course_width = max(len(part[0]) for part in classes)
    name_width = max(len(part[1]) for part in classes)
    number_width = max(len(str(part[2])) for part in classes)

    for course, name, number in classes:
        print(f"{course:{course_width}} is taught by {name:{name_width}} and has {number:{number_width}} students.")


main()
