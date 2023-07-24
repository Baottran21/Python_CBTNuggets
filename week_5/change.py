changeAmt = input("what is the customer's change amount?")
changeAmt = int(changeAmt)

numQtrs = changeAmt//25  # Figure out the number of quarters
changeAmt = changeAmt - (numQtrs * 25)
numDimes = changeAmt // 10  # Figure out number of dimes
changeAmt -= (numDimes * 10)
numNickels = changeAmt // 5  # Figure out number of Nickels
changeAmt -= (numNickels * 5)
numPennies = changeAmt // 1  # Figure out number of pennies
changeAmt -= (numPennies * 1)

print('Quarters: ', (numQtrs))
print('Dimes: %s' % numDimes)
print('Nickels: {}'.format(numNickels))
print(f'Pennies: {numPennies}')
