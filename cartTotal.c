// Shopping Cart Total
// Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the
// four available products and display the total amount that needs to be paid

#include <stdio.h>
#include <string.h>

int main() {

    char headPhone[] = "999";
    char smartWatch[] = "1599";
    char PS5[] = "1299";
    char iPad[] = "599";

    char productName[50];
    printf("Enter Product Name: ");
    scanf("%s", productName);

    char quantity[50];
    printf("Enter the Quantity of the Product: ");
    scanf("%s", quantity);

    char *totalPrice;

    if (strcmp(productName, "headPhone") == 0) {
        totalPrice = headPhone * quantity;
    }
    else if (strcmp(productName, "smartWatch") == 0) {
        totalPrice = headPhone * quantity;
    }
    else if (strcmp(productName, "PS5") == 0) {
        totalPrice = headPhone * quantity;
    }
    else if (strcmp(productName, "iPad") == 0) {
        totalPrice = headPhone * quantity;
    }

    printf("Total Amount To Be Paid: %s\n", totalPrice);

    return 0;
}