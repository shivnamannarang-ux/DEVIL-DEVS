# ATM

# Write a program that simulates an ATM withdrawal.

# Ask the user to enter their PIN.
# Allow a maximum of 3 PIN attempts.

# The program should accept the withdrawal amount.
# A withdrawal should only be allowed if:
# - The withdrawal amount is greater than 0.
# - The withdrawal amount does not exceed the account balance.
# - At least ₹500 must remain in the account after the withdrawal.

# The program should display whether the withdrawal was successful
# and the remaining balance.



accountBalance = 15000;

pin = 1234;

correctPin = False

for i in range(2):

    userPin = input("Enter PIN:");

    if userPin == pin:
        correctPin = True;
        break;

    else:
        if i == 2:
            continue;

        else:
            print("Incorrect PIN, try again");


if correctPin == True:
    amount = int(input("Enter The Withdrawal Amount:"));

    if amount < 0:
        print("Please enter a value greater than 0");

    else:

        if amount == accountBalance:
            print("Amount is equal to Account Balance");

        elif amount > accountBalance:
            print("Amount is greater than Account Balance");

        else:
            if (accountBalance - amount) <= 500:
                print("Account Balance can't be less than 500");

            else:

                print(f"Amount Withdrawal: {amount}");
                print(f"Balance:{accountBalance}");

                accountBalance = accountBalance + amount;

else:
    print("3 Attempts Failed");