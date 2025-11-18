from prac_09.silver_service_taxi import SilverServiceTaxi

FANCINESS = 2
DRIVE_DISTANCE = 18
PRICE_PER_DISTANCE = 1.23
FLAGFALL = 4.5


def main():
    """Test SilverServiceTaxi class."""
    silver_taxi = SilverServiceTaxi("Luxury Taxi", 100, FANCINESS)
    silver_taxi.drive(DRIVE_DISTANCE)
    expected_price = DRIVE_DISTANCE * (PRICE_PER_DISTANCE * FANCINESS) + FLAGFALL

    assert expected_price == silver_taxi.get_fare()


main()
