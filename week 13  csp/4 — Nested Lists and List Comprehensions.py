# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.
list1 =[1, 2, 3]
list2= [4, 5, 6]
nested_list= [list1, list2]
print(nested_list)


# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]

for row in matrix:
    print(row[0])
print(first_col)

# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the first list.
print(matrix[0])

# Print the second item from the third list.
print(matrix[2][1])

# Use a list comprehension to extract the last item from each sub-list.
last_items = [row[-1] for row in matrix]
print(last_items)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.

squares= [x**2 for x in range(1, 11)]
for x in range(1, 11):
    print(x**2)

print(squares)
