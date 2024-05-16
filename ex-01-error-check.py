try:
    name = input("Enter your name: ")

    # Check if the name is empty
    if len(name) == 0:
        raise ValueError("Name cannot be empty.")
    # Check if there are numbers in the name
    elif any(char.isdigit() for char in name):
        raise ValueError("Name should not contain numbers.")
    else:
        print("Valid name:", name)
except ValueError as e:
    print(e)

# Ask the user to input their salary value and convert it to float
try:
    salary = float(input("Enter your salary value: "))
    if salary < 0:
        print("Please enter a positive value for the salary.")
except ValueError:
    print("Invalid input for salary. Please enter a number.")

# Ask the user to input the received bonus value and convert it to float
try:
    bonus_received = float(input("Enter the received bonus value: "))
    if bonus_received < 0:
        print("Please enter a positive value for the bonus.")
except ValueError:
    print("Invalid input for bonus. Please enter a number.")

# Assuming a calculation logic for the final bonus and KPI
final_bonus = bonus_received * 1.2  # Example, adjust as needed
kpi = (salary + final_bonus) / 1000  # Simple example of KPI

# Print the information for the user
print(f"Your KPI is: {kpi:.2f}")
print(f"{name}, your salary is ${salary:.2f} and your final bonus is ${final_bonus:.2f}.")
