balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
paid = 0

monthlyInterestRate = annualInterestRate / 12.0

for month in range(1, 12 + 1):
    minPayment = monthlyPaymentRate * balance
    balance = (balance - minPayment) + monthlyInterestRate * (balance - minPayment)
    paid += minPayment
    print "Month: %d" % month
    print "Minimum monthly payment: %.2f" % minPayment
    print "Remaining balance: %.2f" % balance
    
print "Total paid: %.2f" % paid
print "Remaining balance: %.2f" % balance
