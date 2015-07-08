"""
Instructions go here
"""

import time
start = time.clock()
####################
balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
lowBound = balance / 12
upBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
guess = (upBound - lowBound) / 2.0
tempBalance = balance
epsilon = 0.02

while True:
    guess = (upBound + lowBound) / 2.0
    tempBalance = balance
    for month in range(12):
        tempBalance -= guess
        interest = monthlyInterestRate * tempBalance
        tempBalance += interest
    
    if tempBalance > epsilon:
        lowBound = guess
        
    elif tempBalance < - epsilon:
        upBound = guess
        
    else:
        guess = str(round(guess, 2))
        break

print "Lowest Payment: ", guess


####################
end = time.clock()
print 'elapsed time:', end - start
