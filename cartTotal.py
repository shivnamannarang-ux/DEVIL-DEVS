# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid



headphone = 999
smartwatch = 1599
PS5 = 1299
ipad = 599


productName = input("Enter Product Name: ").lower().strip()


quantity = int(input("Enter the Quantity of the Product: "))


if productName == "headphone":
    totalPrice = headphone * quantity

elif productName == "smartwatch":
    totalPrice = smartwatch * quantity

elif productName == "ps5":
    totalPrice = PS5 * quantity

elif productName == "ipad":
    totalPrice = ipad * quantity


print(f"Total Amount To Be Paid: {totalPrice}")