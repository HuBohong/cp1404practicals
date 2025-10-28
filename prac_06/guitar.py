"""
Estimate: 30 minutes
Start time: 4:00
Finish time: 4:21
"""
from prac_06.programming_language import ProgrammingLanguage
VINTAGE_THRESHOLD = 50

class Guitar:
    """Represent a Guitar object"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost
        self.guitar_age = 0

    def __str__(self):
        """Return a string representation of a Guitar instance."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return the age of the guitar."""
        self.guitar_age = current_year - self.year
        return self.guitar_age

    def is_vintage(self):
        return self.guitar_age >= VINTAGE_THRESHOLD