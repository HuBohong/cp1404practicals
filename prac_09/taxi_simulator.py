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
            current_taxi, trip_cost = drive_taxi(current_taxi)
            current_bill += trip_cost
        customer_choice = input(f"{MENU}\n>>> ").lower()


def drive_taxi(current_taxi):
    trip_cost = 0.0
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        distance = float(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost}")

    return current_taxi, trip_cost


main()
