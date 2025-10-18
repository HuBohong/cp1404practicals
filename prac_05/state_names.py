"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

shortcut_width = max(len(province_shortcut) for province_shortcut in CODE_TO_NAME.keys())
province_width = max(len(province_name) for province_name in CODE_TO_NAME.values())

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for province_shortcut, province in CODE_TO_NAME.items():
    print(f"{province_shortcut:{shortcut_width}} is {province:{province_width}}")
