"""
CP1404/CP5632 Practical 5
wimbledon game practice
estimate: 1h30min
actual:
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    champion_to_count = {}
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        information_champions = [[information[1], information[2]] for information in list(reader)]
        for pair in information_champions:
            champion_to_count[pair[1]] = champion_to_count.get(pair[1], 0) + 1

        champion_country = set(pair[0] for pair in information_champions)
        print(sorted(champion_country))


main()
