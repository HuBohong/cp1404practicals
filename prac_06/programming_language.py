"""
Estimate: 20 min
start: 3:10
finish: 3:34
CP1404/CP5632 - Practical - Programming Language class
"""

class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=0):
        """
        Initialize a ProgrammingLanguage instance.
        :param name: name of the programming language
        :param typing: dynamic or static typing
        :param reflection: reflection capability (True/False)
        :param year: year of creation
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string format of the ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"
