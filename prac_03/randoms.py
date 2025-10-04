"""
CP1404/CP5632 - Practical
Bohong Hu
"""
import random

# help(random.uniform)

"""
Question 1 
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
"""
print(random.randint(5, 20))
# Output:5 13 6 13 17 7 6 15 19 12
# The output is a random integer between 5 and 20, including both 5 and 20.
# But what i got the largest number is 19 and the lowest number is 5

"""
Question 2
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
"""
print(random.randrange(3, 10, 2))
# Output:7 7 5 3 9 5 3 9 3 3
# The output is a random odd integer between 3 and 10 with step of 2, including 3 but not including 10.
# But what i got the largest number is 9 and the lowest number is 3
# No, line 2 could not have produced a 4 because start at 3 and step of 2 will only produce odd numbers.

"""
Question 3
What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
"""
print(random.uniform(2.5, 5.5))
# Output: 2.842017627409588 2.5408758495350066 5.276703081357725 2.79468884166897 4.681220089489852 4.122211715608961
# The output is a random float number between 2.5 and 5.5, including 2.5 but for b it depends on rounding.
# The smallest number i got is 2.5408758495350066 and the largest number is 5.276703081357725.


"""
Question 4
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
print(random.randint(1, 100))