#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome to the Tip Calculator!")

bill = float(input("Enter the bill amount:\n"))
numPartiesToSplit = int(input("Enter the number of people to split the bill with:\n"))
tipAmount = int(input("Enter tip percentage amount (e.g. 10, 15, 20):\n"))
tipAsPercent = tipAmount / 100

perPersonBill = round(bill * (1 + tipAsPercent) / numPartiesToSplit, 2)

print("Each person should pay $" + str(perPersonBill))
