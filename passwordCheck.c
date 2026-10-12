// Password Validator
// Write a Python program that validates a user's password.

// A password is considered valid if:
// It contains at least 8 characters
// It contains at least one uppercase letter
// It contains at least one lowercase letter
// It contains at least one digit

// The program should display whether the password is valid or invalid.

#include <stdio.h>
#include <ctype.h>

int main() {

    char password[100];
    printf("Enter password: ");
    scanf("%s", password);

    int has_upper = 0;
    int has_lower = 0;
    int has_digit = 0;

    if (password > 8) {

        for (int i = 0; password[i] != '\0'; i++) {

            char char = password[i];

            if (isupper(char)) {
                has_upper == 1;
            }

            if (islower(char)) {
                has_lower == 1;
            }

            if (isdigit(char)) {
                has_digit = 0;
            }
        }

        if (has_upper || has_lower || has_digit) {
            printf("Valid Password\n");
        } else {
            printf("Invalid Password\n");
        }

    } else {
        printf("Invalid Password\n");
    }

    return 0;
}