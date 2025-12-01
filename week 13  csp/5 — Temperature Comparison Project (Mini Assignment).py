# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temperature= (90)

if temperature <= 20:
    print("its very very cold")
elif 20 < temperature < 50:
        print("It's warm")
else: 
        print("It's hot")

if temperature <= -10:
       print("Extreme Temperature Warning!")

if temperature < -10 or temperature > 110:
        print("Extreme temperature warning!")
