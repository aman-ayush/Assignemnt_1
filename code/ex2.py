gross_income = input(" enter gross income ")
dependent = input(" no of dependents ")
tax_rate = 20
standard_deduction = 10000
dependent_deduction = 3000*dependent
taxable_income = gross_income - standard_deduction - dependent_deduction
tax = taxable_income*.20
print(" payable tax ",tax)
