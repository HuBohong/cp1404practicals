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

    def play(self):
        """Return a string of all musicians playing their instruments."""
        for musician in self.musicians:
            if len(musician.instruments) == 0:
                print(f"{musician.name} needs an instrument!")
            else:
                print(f"{musician.name} is playing: {musician.instruments[0]}")
