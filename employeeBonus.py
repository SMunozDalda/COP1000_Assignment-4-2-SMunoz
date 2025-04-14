# Get user input
employee_name = input("Enter Employee Name: ")
shifts = int(input("Enter number of shifts: "))
transactions = int(input("Enter number of transactions: "))
transaction_value = float(input("Enter transactions dollar value: "))

# Calculate productivity score
productivity_score = (transaction_value / transactions) / shifts

# Determine bonus using nested if
if productivity_score <= 30:
    bonus = 50.0
else:
    if productivity_score <= 69:
        bonus = 75.0
    else:
        if productivity_score <= 199:
            bonus = 100.0
        else:
            bonus = 200.0

# Output the result
print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus}")
