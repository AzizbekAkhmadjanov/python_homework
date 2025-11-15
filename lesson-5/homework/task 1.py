
# Homework:

# def is_leap(year): """ Determines whether a given year is a leap year.

# A year is a leap year if:
# - It is divisible by 4, and
# - It is NOT divisible by 100, unless it is also divisible by 400.

# Parameters:
# year (int): The year to be checked.

# Returns:
# bool: True if the year is a leap year, False otherwise.
# """
# if not isinstance(year, int):
#     raise ValueError("Year must be an integer.")

# return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# def is_leap(year):
#     """
#     Determines whether a given year is a leap year.

#     A year is a leap year if:
#     - It is divisible by 4, and
#     - It is NOT divisible by 100, unless it is also divisible by 400.

#     Parameters:
#         year (int): The year to be checked.

#     Returns:
#         bool: True if the year is a leap year, False otherwise.
#     """
#     if not isinstance(year, int):
#         raise ValueError("Year must be an integer.")

#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# print(is_leap(2000))
# print(is_leap(2100))
# print(is_leap(2004))

# --------------------------------------------------------------------------------


# 2. Conditional Statements Exercise

# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 <= n <= 100
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0
# 3
# Sample Output 0
# Weird


# def check_weird(n):
#     if n % 2 == 1:
#         return "Weird"
#     else:
#         if 2 <= n <= 5:
#             return "Not Weird"
#         elif 6 <= n <= 20:
#             return "Weird"
#         else:  # n > 20
#             return "Not Weird"


# # Example usage:
# n = int(input())
# print(check_weird(n))

# --------------------------------------------------------------------------------

# 3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.

# Solution 1 with if-else statement.

# Solution 2 without if-else statement.

# # Solution 1
# def even_numbers_if(a, b):
#     if a > b:
#         return []
#     if a % 2 == 0:
#         return [a] + even_numbers_if(a + 2, b)
#     else:
#         return even_numbers_if(a + 1, b)
    
# # Solution 2
# def even_numbers_no_if(a, b):
#     start = a + (a % 2)      # moves to next even number automatically
#     return [] if start > b else [start] + even_numbers_no_if(start + 2, b)

# print(even_numbers_if(3, 12))       # [4, 6, 8, 10, 12]
# print(even_numbers_no_if(3, 12))    # [4, 6, 8, 10, 12]

