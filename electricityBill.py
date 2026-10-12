# Electricity Bill Calculator
# Write a program that calculates the electricity bill based on units consumed using different rates for different slabs.

# 100 and below = 3
# 100-200 = 5
# 200-300 = 7
# 300 above = 10


# Taking Units Consumed as Input
units = int(input("Enter Units Consumed: ")) #Unnecessary semicolons were removed due to incorrect syntax #typecasting was done so that the data entered by the user is stored as integer in the variable "units".


# Calculating Bill Based on Slabs
if 0<units<=100: #Upper limit and lower limit was added in the if condition
    totalBill = units * 3 #Unnecessary semicolons were removed due to incorrect syntax

elif 100<units<=200: #Upper limit and lower limit was added in the if condition for the case when the units will lie between 100-200.
    totalBill = 100*3 + (units-100)*5 #Unnecessary semicolons were removed due to incorrect syntax
    #Brackets were added so that the mathematical logic of BODMASS when applied gives accurate output

elif 200<units<300:
    totalBill = 100*3 + 100*5 + (units-200)*7 #Unnecessary semicolons were removed due to incorrect syntax 
    #Brackets were added so that the mathematical logic of BODMASS when applied gives accurate output
else:
    totalBill = 100*3 + 100*5 + 100*7 + (units-300)*10 #Unnecessary semicolons were removed due to incorrect syntax

# Displaying the Final Bill
print(f"Total Electricity Bill: {totalBill}") #Unnecessary semicolons were removed due to incorrect syntax