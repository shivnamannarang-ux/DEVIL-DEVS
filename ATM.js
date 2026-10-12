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

function atm(pinAttempts, amount) {

    let accountBalance = 15000;

    let pin = 1234;

    let correctPin = false;

    for (let i = 0; i < 2; i++) {

        let userPin = pinAttempts[i];

        if (userPin == pin) {
            correctPin = true;
            break;
        }

        else {
            if (i == 2) {
                continue;
            }

            else {
                console.log("Incorrect PIN, try again");
            }
        }
    }


    if (correctPin == true) {

        if (amount < 0) {
            console.log("Please enter a value greater than 0");
        }

        else {

            if (amount == accountBalance) {
                console.log("Amount is equal to Account Balance");
            }

            else if (amount > accountBalance) {
                console.log("Amount is greater than Account Balance");
            }

            else {
                if ((accountBalance - amount) <= 500) {
                    console.log("Account Balance can't be less than 500");
                }

                else {

                    console.log(`Amount Withdrawal: ${amount}`);
                    console.log(`Balance:${accountBalance}`);

                    accountBalance = accountBalance + amount;
                }
            }
        }
    }

    else {
        console.log("3 Attempts Failed");
    }
}