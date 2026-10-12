# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid



headPhone = "999";
smartWatch = "1599";
PS5 = "1299";
iPad = "599";


productName = input("Enter Product Name: ");


quantity = input("Enter the Quantity of the Product: ");


if productName == "headPhone":
    totalPrice = headPhone * quantity;

elif productName == "smartWatch":
    totalPrice = headPhone * quantity;

elif productName == "PS5":
    totalPrice = headPhone * quantity;

elif productName == "iPad":
    totalPrice = headPhone * quantity;


print(f"Total Amount To Be Paid: {totalPrice}");