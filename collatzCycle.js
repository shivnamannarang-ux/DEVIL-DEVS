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

function collatzCycle(number) {

    let steps = 0;

    let reachOne = true;

    let originalNumber = number;

    let largestValue = number;

    let stepLimit = 100;

    let i;

    for (i = 1; i < 50; i++) {

        steps = steps + 1;

        i = i + 1;

        if (number % 2 == 1) {

            number = number / 2;

            steps = steps + 1;

            if (number == 1) {
                reachOne = true;
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
                reachOne = true;
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


    console.log(`Steps: ${i}`);
    console.log(`Largest Number: ${largestValue}`);
    console.log(`reach One: ${reachOne}`);
}