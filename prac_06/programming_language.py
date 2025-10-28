class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=0):
        """
        Initialize a ProgrammingLanguage instance.
        :param name: name of the programming language
        :param typing: dynamic or static typing
        :param reflection: reflection capability (Yes/No)
        :param year: year of creation
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"
