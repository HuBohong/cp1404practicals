from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A Silver Service Taxi class, derived from Taxi class."""
    flagfall = 4.50

    def __init__(self, fanciness: float):
        super().__init__()
        self.fanciness = fanciness
        self.price_per_km = fanciness * Taxi.price_per_km

    def get_price(self):
        """Return the price for the taxi trip including flagfall."""
        return self.price_per_km * self.current_fare_distance + self.flagfall

