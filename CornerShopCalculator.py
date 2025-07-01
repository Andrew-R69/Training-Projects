print(f"""Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80
""")
income = 202 + 118 + 2250 + 1680 + 1075 + 80
print(f"Income: ${float(income):.2f}")

staff_expenses = int(input("Enter staff expenses: "))
other_expenses = int(input("Enter other expenses: "))

print(f"Net income: ${float(income - staff_expenses - other_expenses):.2f}")