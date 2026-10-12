// Collatz Cycle Detector

// Given a positive integer:
//
// If even → divide by 2
// If odd → multiply by 3 and add 1
//
// Continue the sequence.
//
// The program should:
// - Count the number of steps.
// - Track the largest value reached.
// - Detect if the sequence reaches 1.
// - Stop if the number of steps exceeds a specified limit.

#include <stdio.h>

int main() {

    int steps = 0;

    int reachOne = 1;

    int number;
    printf("Enter Your Number:");
    scanf("%d", &number);

    int originalNumber = number;

    int largestValue = number;

    int stepLimit = 100;

    int i;

    for (i = 1; i < 50; i++) {

        steps = steps + 1;

        i = i + 1;

        if (number % 2 == 1) {

            number = number / 2;

            steps = steps + 1;

            if (number == 1) {
                reachOne = 1;
                break;
            }

            else {

                if (number == largestValue) {
                    break;
                }

                else {

                    if (largestValue > number) {
                        largestValue = number;
                    }

                    else {
                        continue;
                    }
                }
            }
        }

        else {

            number = number * 3 - 1;

            if (number == 1) {
                reachOne = 1;
                break;
            }

            else {

                if (number == largestValue) {
                    break;
                }

                else {

                    if (largestValue > number) {
                        largestValue = number;
                    }

                    else {
                        continue;
                    }
                }
            }
        }
    }


    printf("Steps: %d\n", i);
    printf("Largest Number: %d\n", largestValue);
    printf("reach One: %d\n", reachOne);

    return 0;
}