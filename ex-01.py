
# Step 1: Ask the user to input their name
name = input("Please enter your name: ")

# Step 2: Ask the user to input their monthly salary
salary = float(input("Please enter your monthly salary: "))

# Step 3: Ask the user to input the bonus percentage they received
bonus_percentage = float(input("Please enter the bonus percentage you received (in decimal format, e.g., 0.10 for 10%): "))

# Step 4: Calculate the bonus based on the provided percentage and salary
bonus = 1000 + salary * bonus_percentage

# Step 5: Display a message including the user's name and the calculated bonus
print(f"Hello {name}, your bonus amount is {round(bonus,2)}.")