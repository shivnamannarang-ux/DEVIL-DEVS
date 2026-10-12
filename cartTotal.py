# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid



headphone = 999 #Strings were removed as integer values must be stored to calculate the final bill
smartwatch = 1599 #Strings were removed as integer values must be stored to calculate the final bill
PS5 = 1299 #Strings were removed as integer values must be stored to calculate the final bill
ipad = 599 #Strings were removed as integer values must be stored to calculate the final bill


productName = input("Enter Product Name: ").lower().strip()#Unnecessary semicolons were removed due to incorrect syntax
#Enhancing: lower and strip string functions were added to avoid the case sensitivity while taking and storing the input. 


quantity = int(input("Enter the Quantity of the Product: "))#Unnecessary semicolons were removed due to incorrect syntax
#typecasting was done as quantity needed to be in integers in order to calculate the bill. 


if productName == "headphone":
    totalPrice = headphone * quantity #Unnecessary semicolons were removed due to incorrect syntax

elif productName == "smartwatch":
    totalPrice = smartwatch * quantity #Unnecessary semicolons were removed due to incorrect syntax
    #Name correction was done
elif productName == "ps5":
    totalPrice = PS5 * quantity #Unnecessary semicolons were removed due to incorrect syntax
    #Name correction was done
elif productName == "ipad":
    totalPrice = ipad * quantity #Unnecessary semicolons were removed due to incorrect syntax 
    #Name correction was done

print(f"Total Amount To Be Paid: {totalPrice}") 

