monthly_incom = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_incom - monthly_expenses
annual_saving = monthly_savings * 12
projected_savings = (annual_saving + (monthly_savings * 12 * 0.05))
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
