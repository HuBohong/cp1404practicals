from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A Silver Service Taxi class, derived from Taxi class."""
    flagfall = 4.50

    def __init__(self, name: str, fuel: int, fanciness: float):
        """
        Initialize a Silver Service Taxi instance.
        :param name: name of the taxi
        :param fuel: amount of fuel in the taxi
        :param fanciness: fanciness multiplier for the taxi
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string representation of the Silver Service Taxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        return self.price_per_km * self.current_fare_distance + self.flagfall
