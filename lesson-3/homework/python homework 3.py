
# Homework: List and Tuple Exercises

# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.

# fruits = ['Apple', 'Pear', 'Strawberry', 'Peach', 'Banana']

# print(f"The third fruit is: {fruits[2]}")


# --------------------------------------------------------------------------------
# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.

# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 3, 6, 7, 8, 13]
# my_list= list1 + list2

# print(my_list)


# --------------------------------------------------------------------------------
# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
# numbers = [10, 20, 30, 40, 50, 60, 70]

# first = numbers[0]
# middle = numbers[len(numbers)//2]
# last = numbers[-1]

# new_list = [first, middle, last]
# print(new_list)

# --------------------------------------------------------------------------------
# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

# movies_list= ['Avengers', 'Sherlock Holmes', 'Spiderman', 'Doctor Strange', 'IronMan']
# print(movies_list)
# print(type(movies_list))

# my_tuple= tuple(movies_list)
# print(my_tuple)
# print(type(my_tuple))


# --------------------------------------------------------------------------------
# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.

# cities= ['Berlin', 'New York', 'London', 'Istanbul', 'Paris', 'Moscow', 'Madrid']

# if "Paris" in cities:
#     print("'Paris' is included in the cities list.")
# else:
#     print("'Paris' is not included in the cities list.")


# --------------------------------------------------------------------------------
# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

# num_list= [1, 2, 3, 4, 5, 6, 7, 8]
# num_list+=num_list

# print(num_list)


# --------------------------------------------------------------------------------
# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.

# numbers = [19, 25, 3, 14, 52, 7, 90, 12]
# print(numbers)

# numbers[0], numbers[-1] = numbers[-1], numbers[0]
# print(numbers)


# --------------------------------------------------------------------------------
# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# # Slice from index 3 to 7 (index 7 is excluded)
# sliced = numbers[3:8]
# print(sliced)


# --------------------------------------------------------------------------------
# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

# colours= ['red','yellow', 'blue', 'yellow','yellow', 'blue', 'green', 'blue','yellow', 'blue', 'black', 'blue', 'white', 'blue',]

# print(f"The color 'blue' appears {colours.count('blue')} times in the list.")

# --------------------------------------------------------------------------------
# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

# tuple_animals = ('bear', 'tiger', 'panda', 'lion', 'monkey', 'snake', 'volf')

# # Find index directly from tuple
# index_lion = tuple_animals.index('lion')
# print(index_lion)

# --------------------------------------------------------------------------------
# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.

# tuple1= (1, 2, 3, 4, 5, 6, 7, 8)
# tuple2= (2, 4, 3, 12, 18)

# tuple3= tuple1 + tuple2

# print(tuple3)


# --------------------------------------------------------------------------------
# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

# given_list= [1, 2, 3, 4, 5, 6, 7]
# given_tuple= (1, 2, 3, 4, 5, 6)

# print(f"The length of the given list: {len(given_list)}")
# print(f"The length of the given tuple: {len(given_tuple)}")


# --------------------------------------------------------------------------------
# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.

# my_tuple= (1, 2, 3, 4, 5)
# print(my_tuple)
# print(type(my_tuple))

# my_list= list(my_tuple)
# print(my_list)
# print(type(my_list))


# --------------------------------------------------------------------------------
# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

# given_tuple = (4, 2, 329, 120, 548, 74, 89)

# max_num = max(given_tuple)
# min_num = min(given_tuple)

# print(f"The maximum value: {max_num}")
# print(f"The minimum value: {min_num}")


# --------------------------------------------------------------------------------
# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.

# str_tuple = ('car', 'laptop', 'screen', 'lion', 'elephant')

# # Reverse tuple using slicing
# reversed_tuple = str_tuple[::-1]
# print(reversed_tuple)

