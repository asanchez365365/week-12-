# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output 3
print(b) #output 4
print(a==b) #output false

print(a == b)   #checks for equality # False
print(a != b)   # check if its not equal to another value # True
print(a > b)    # checks for greater than another value # False
print(a < b)    # checks for less than another value # True
print(a >= b)   # checks for greater thajn or equal to # False
print(a <= b)  # checks for less than or equal to # True


#predict the output of the following comparisons:
10 > 5  #output true
7 == 2 * 3 + 1 # output true
8 != 8 #output false
4 <= 2 + 2 #output true

# Write 3 examples that result in True and 3 that result in False.
9 != 9 #output false
10 != 11 #output true
2 > 2 #output flase
2 >= 2 #output true
10 == 4*2+2 #output true
12 == 4*2+3 #output false

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

#asking student for score
score = int(input("what is your score?"))
#make this program for all grading spectrums
#if ths core is between 90-100 .. you got an A
#if the score is between 80-89 -- you got a B
#if the score is between 70-79 -- you got a C
#if the score is between 61-69 .. you got a D
#else you failed
# if score >= 60:
#     print("you passed the test")
# else:
#     print("you didnt pass")

if score >= 90 and score <=100:
    print("you got an A!")

elif score >= 80 and score <=89:
    print("You got a B!")

elif score >= 70 and score<=79:
    print ("you got a C")

elif score >= 60 and score <= 69:
    print("You got a D ")

else:
    print("you failed, come for ACLAB")


# #ask for a password
password = input("what is your password?")
if len(password) >= 8 and any(char.isdigit() for char in password)
    print('Password is valid')
else:
    print("Password is invalid.")
    "It must be atleast 8 characters long and contain at least one digit"

