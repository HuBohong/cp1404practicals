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
    information_champions = get_champion_information()
    count_campion(champion_to_count, information_champions)

    champion_country = get_distinct_champion_country(information_champions)
    print_format_information(champion_country, champion_to_count)


def print_format_information(champion_country, champion_to_count):
    for name, count in champion_to_count.items():
        print(f"{name}: {count}")
    print(f"These 12 countries have won Wimbledon:")
    print(", ".join(sorted(champion_country)))


def get_distinct_champion_country(information_champions):
    champion_country = set(pair[0] for pair in information_champions)
    return champion_country


def get_champion_information():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        information_champions = [[information[1], information[2]] for information in list(reader)]
        return information_champions


def count_campion(champion_to_count, information_champions):
    for pair in information_champions:
        champion_to_count[pair[1]] = champion_to_count.get(pair[1], 0) + 1


main()
