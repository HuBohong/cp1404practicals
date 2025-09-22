"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
# The score must be between 0 and 100
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
# if enter into else then score must be valid between 0 and 100
else:
    # select above 90 first for highest range
    if score > 90:
        print("Excellent")
    # select above 50 next for middle range
    elif score > 50:
        print("Passable")
    # select below 50 for lowest range
    elif score < 50:
        print("Bad")
