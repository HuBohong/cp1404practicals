from prac_09.musician import Musician


class Band:
    """Represent a band with its musicians."""

    def __init__(self, name):
        """Initialize band with name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({','.join(str(musician) for musician in self.musicians)})"

    def add(self, musician: Musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of all musicians playing their instruments."""
        musicians_plays = []
        for musician in self.musicians:
            musicians_plays.append(musician.play())
        return "\n".join(musicians_plays)
