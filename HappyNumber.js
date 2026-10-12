// Happy Number Detection

// Given a positive integer:
// Replace the number with the sum of the squares of its digits.
// Repeat.
// If it reaches 1, it is a happy number.
// If the process enters a cycle, it is not.

function happyNumber(number) {

    number = Number(number);

    let attempts = 0;

    let sum = 0;

    while (number != 1) {

        attempts = attempts + 1;

        while (number > 0) {

            let digit = number % 10;

            sum = sum + Digit * 2;

            number = Math.floor(number / 10);
        }

        number = sum;
    }

    if (number == 1) {
        console.log("It has Entered a Loop");
    } else {
        console.log("It is a Happy Number");
    }
}