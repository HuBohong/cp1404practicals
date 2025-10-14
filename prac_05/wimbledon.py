"""
CP1404/CP5632 Practical 5
wimbledon game practice
estimate: 1h30min
actual:
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    with open(FILENAME,"r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        information_champions = [[information[1],information[2]] for information in list(reader)]
        print(information_champions)




main()