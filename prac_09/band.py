from prac_09.musician import Musician


class Band:
    """Represent a band with its musicians."""

    def __init__(self, name):
        """Initialize band with name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician:Musician):
        """Add a musician to the band."""
        self.musicians.append(musician)


