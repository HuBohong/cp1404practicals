from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Represent an unreliable car that may not drive the full distance requested."""

    def __init__(self, name: str, fuel: int, reliability: float):
        """Initialise an UnreliableCar instance.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        reliability: float, a value between 0 and 1 representing the probability of driving the full distance
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """ Drive the car a given distance based on its reliability."""
        if randint(0, 100) / 100 < self.reliability:
            return super().drive(distance)
        else:
            return super().drive(0)
