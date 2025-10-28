"""
Estimate: 30 minutes
Start time: 4:00
"""


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
