"""
Estimate: 30 minutes
Start time: 4:00
Finish time: 4:21
"""

VINTAGE_THRESHOLD = 50
CURRENT_YEAR = 2025


class Guitar:
    """Represent a Guitar object"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar instance."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare guitars based on their year."""
        return self.year < other.year

    def get_age(self):
        """Return the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar age is greater than 50, else False."""
        return CURRENT_YEAR - self.year >= VINTAGE_THRESHOLD
