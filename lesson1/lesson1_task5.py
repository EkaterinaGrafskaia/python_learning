income = int(input("Enter your income: "))
expenses = int(input("Enter your expenses: "))
if income > expenses:
    print(f"Excellent job! Your earn {income - expenses}.")
    profit_margin = ((income - expenses) / income) * 100
    print(f"Your profit margin is {profit_margin:.0f}%.")
    employee = int(input("Enter number of employees: "))
    profit_per_employee = (income - expenses) / employee
    print(f"Your profit per employee is {profit_per_employee:.2f}.")
elif income == expenses:
    print("Good job! Your income equals the expenses.")
else:
    print(f"Unfortunatelly, you lost {expenses - income}.")
