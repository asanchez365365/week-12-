# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#lists are part of the collections family in Python
# Examples:
my_list = [1,2,3,4,5]
print(my_list) #[1,2,3,4,5]
print(len(my_list)) #5
print(type(my_list)) # <class 'list'>
print(my_list[0]) #1
print(my_list[1:4]) # [2, 3, 4]
print(my_list[1:]) # [2, 3, 4, 5]
print(my_list[:-1]) #[1,2,3,4]
#reverse list
print(my_list[::-1]) #[5,5,3,2,1]
#modifying a list
my_list.append(6) #adds 6 to the end of the list
print(my_list) # [1,2,3,4,5
my_list.extend([7,8])
print(my_list) # [ 1,2,3,4,5]
#remove the last item
my_list.pop()
print(my_list) #[1,2,3,4,5,6,7]

my_list.pop(2) 
print(my_list) #[ 1,2,3,4,5,6,7]

#reverse the list
my_list.reverse()
print (my_list) # [7,6,5,4,3,2,1]
#remove to remove a specific value
my_list.remove(4)
print(my_list) #[7,6,5,2,1]

new_list = list(range (12,320))
print(new_list)
my_list.append(new_list)
print(my_list)

#print every third number
print(my_list [ : : 3])
#remove every third element
del my_list [ : : 3]
print(len(my_list))
print(my_list)

#list functions
#.append() -adds an item to the end of the list
#.extend() - adds multiple items to the end of the list
#.pop() - removes and returns an item at a given index
# ( default is the last item)
#.remove() - removes the first occurance of a specific value
#.sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list
######################################################
#why is a list more useful than a variable?
# a list can hold multiple values,
# while a variable can only hold one value at a time
cakes = ['chocolate', 'vanilla', 'rev velvet', 'carrot']
print(cakes)
#access the first item
print(cakes[0])#chocolate
#access the last item
print(cakes[-1]) #carrot
#want to chocolate cake instead of vanilla
cakes[0] = 'strawberry'
print(cakes) # [ 'strawberry', 'chocolate', 'red velvet', 'carrot',]
#add a new cake to end of the list
print(cakes)
cakes[1] ='chocolate'
print(cakes)
cakes.pop()
print(cakes)
#insert a new cake at index 2
cakes.insert(2,'funfetti')
print(cakes)





my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.
my_list = ['pizza','wings','pasta', 'soup', 'bread']

# # Print the second and last item.
print(my_list[1:4])
# # Add a new item using .append().
my_list.append("hamburger")
print(my_list)
# # Remove the first item using .pop(0).
my_list.pop(1)
print(my_list)
# # Reverse your list using .reverse().
my_list.reverse()
print (my_list)

#sets = {1,2,3}
#sets are unordered collections of unique items
#sets do not suppirt indexing or slicing
# sets are mutable, meaning you can add or remove items
#sets are created using curly braces {}
#Sets do not allow duplicate items
my_set ={1,2,3,4,5}
print(my_set) #{1,2,3,4,5}
print(type(my_set)) #<class 'set'>
#add an item to the set
my_set.add(6)
print(my_set)
#remove an item from the set
my_set.remove(3)
print(my_set)

#check if an item is in the set
print(4 in my_set) #true
print(3 in my_set) # false

#tuples are ordered collections of items
#tuples are immutable, meaning you cannot modify them after creation
#tuples are created using parenthesis()
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(type(my_tuple)) #<class 'tuple'>
print(my_tuple[0]) #1
print(my_tuple[1:4])
