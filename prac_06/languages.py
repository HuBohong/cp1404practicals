"""
Estimate: 20 min
start: 3:10
finish: 3:34
CP1404/CP5632 - Practical - Programming Language class
"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    """Create and display ProgrammingLanguage objects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    programming_languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)

main()