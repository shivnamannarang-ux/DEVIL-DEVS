// Password Validator
// Write a Python program that validates a user's password.

// A password is considered valid if:
// It contains at least 8 characters
// It contains at least one uppercase letter
// It contains at least one lowercase letter
// It contains at least one digit

// The program should display whether the password is valid or invalid.

function passwordCheck(password) {

    let has_upper = false;
    let has_lower = false;
    let has_digit = false;

    if (password > 8) {

        for (let char of password) {

            if (/[A-Z]/.test(char)) {
                has_upper == true;
            }

            if (/[a-z]/.test(char)) {
                has_lower == true;
            }

            if (/[0-9]/.test(char)) {
                has_digit = false;
            }
        }

        if (has_upper || has_lower || has_digit) {
            console.log("Valid Password");
        } else {
            console.log("Invalid Password");
        }

    } else {
        console.log("Invalid Password");
    }
}