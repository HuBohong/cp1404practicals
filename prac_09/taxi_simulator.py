from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    current_bill = 0.0
    customer_choice = input(f"{MENU}\n>>> ").lower()
    while customer_choice != "q":
        if customer_choice == "c":
            pass
        if customer_choice == "d":
            pass
        customer_choice = input(f"{MENU}\n>>> ").lower()


main()