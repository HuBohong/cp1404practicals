"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month : "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """ only print income information """

    print("\nIncome Report\n-------------")
    for i in range(len(incomes)):
        total_income = get_total_income(incomes, i + 1)
        print(f"Month {i + 1:2} - Income: ${incomes[i]:10.2f} Total: ${total_income:10.2f}")


def get_total_income(incomes, number_of_months):
    """ calculate total income """
    total_income = 0
    for month in range(number_of_months):
        total_income += incomes[month]

    return total_income


main()
