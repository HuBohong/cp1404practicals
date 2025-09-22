"""
1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program
"""

user_choice = int(input("please select the method you would like to try \n"
                        "1. Show the even numbers from x to y \n"
                        "2. Show the odd numbers from x to y \n"
                        "3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16) \n"
                        "4. Exit the program\n"))

while user_choice != 4:
    # case 1 even numbers
    if user_choice == 1:
        x = int(input("enter x number:"))
        y = int(input("enter y number:"))
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end=' ')

    # case 2 odd numbers
    elif user_choice == 2:
        x = int(input("enter x number:"))
        y = int(input("enter y number:"))
        for i in range(x, y + 1):
            if i % 2 != 0:
                print(i, end=' ')

    # case 3 squares of numbers
    elif user_choice == 3:
        x = int(input("enter x number:"))
        y = int(input("enter y number:"))
        for i in range(x, y + 1):
            print(i ** 2, end=' ')

    else:
        print("invalid input")

    user_choice = int(input("please select the method you would like to try \n"
                            "1. Show the even numbers from x to y \n"
                            "2. Show the odd numbers from x to y \n"
                            "3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16) \n"
                            "4. Exit the program\n"))
