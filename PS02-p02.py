#balance = 4773
#annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
pay = 0
remBalance = balance

while remBalance > 0:
    month = 0
    remBalance = balance
    pay += 10
    while month < 12 and remBalance > 0:
        month += 1
        remBalance -= pay
        remBalance += monthlyInterestRate * remBalance


print "Lowest Payment: ", pay
