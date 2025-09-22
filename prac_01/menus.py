"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name = input("Enter name: ")
print("(H)ello \n(G)oodbye \n(Q)uit")

# Get user choice with upper case
option = input(">>> ").upper()

# Main loop for choice selection
while option != "Q":
    if option == "H":
        print(f"Hello {name}")
    elif option == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
        # Reenter the choice if invalid
    print("(H)ello \n(G)oodbye \n(Q)uit")
    option = input(">>> ").upper()

print("Finished.")
