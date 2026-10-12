// ATM
// Write a program that simulates an ATM withdrawal.

// Ask the user to enter their PIN.
// Allow a maximum of 3 PIN attempts.

// The program should accept the withdrawal amount.
// A withdrawal should only be allowed if:
// - The withdrawal amount is greater than 0.
// - The withdrawal amount does not exceed the account balance.
// - At least ₹500 must remain in the account after the withdrawal.

// The program should display whether the withdrawal was successful
// and the remaining balance.

#include <stdio.h>

int main() {

    int accountBalance = 15000;

    int pin = 1234;

    int correctPin = 0;

    char userPin[50];

    for (int i = 0; i < 2; i++) {

        printf("Enter PIN:");
        scanf("%s", userPin);

        if (userPin == pin) {
            correctPin = 1;
            break;
        }

        else {
            if (i == 2) {
                continue;
            }

            else {
                printf("Incorrect PIN, try again\n");
            }
        }
    }


    if (correctPin == 1) {

        int amount;
        printf("Enter The Withdrawal Amount:");
        scanf("%d", &amount);

        if (amount < 0) {
            printf("Please enter a value greater than 0\n");
        }

        else {

            if (amount == accountBalance) {
                printf("Amount is equal to Account Balance\n");
            }

            else if (amount > accountBalance) {
                printf("Amount is greater than Account Balance\n");
            }

            else {
                if ((accountBalance - amount) <= 500) {
                    printf("Account Balance can't be less than 500\n");
                }

                else {

                    printf("Amount Withdrawal: %d\n", amount);
                    printf("Balance:%d\n", accountBalance);

                    accountBalance = accountBalance + amount;
                }
            }
        }
    }

    else {
        printf("3 Attempts Failed\n");
    }

    return 0;
}