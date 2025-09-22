"""
a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100

b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

c. print a number of stars.
Ask the user for a number, then print that many stars (*), all on one line.

d. print lines of increasing stars.
Ask the user for a number of lines, then print lines of increasing stars, starting at 1 with no blank line.
"""
for i in range(1, 21, 2):
    # second choice of solving this issue by using if (if i % 2 != 0:)
    print(i, end=' ')
print()

# question a
# Start 0 included stop 101 excluded step 10
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# question b
# start 20 included stop 0 excluded step -1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# question c
user_input = int(input("please enter a number"))
for i in range(user_input):
    print("*", end='')
print()
# question d
user_input = int(input("please enter a number"))

# Outer loop print row and change line
for row_of_star in range(user_input):
    # Inner loop control the number of stars in each line
    for number_of_star in range(row_of_star + 1):
        print("*", end='')
    print()
