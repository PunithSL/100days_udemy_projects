#welcome line
print("Welcome to the tip calculator.")
#bill

bill = float(input("What was the total bill? $"))
#tip given in percentage
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
#total person spliting the bill
total_persons = int(input("How many people to split the bill? "))

add_tip = bill *(tip/100)
total_bill = add_tip + bill

split_bill = total_bill / total_persons
#round the splited bill to 2 decimal value
print(f"Each person should pay: ${round(split_bill,2)} ")

