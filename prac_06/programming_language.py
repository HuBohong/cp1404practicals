class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"
