// Number Statistics

// The program takes a positive integer and processes every digit to determine:
// - Largest digit
// - Smallest digit
// - Digit sum
// - Number of even digits
// - Number of odd digits

function numberStatistics(number) {

    let largestNumber = 9;
    let smallestNumber = 0;

    let sum = 0;

    let digitCount = number.length;

    let total = 0;

    let evenDigits = 0;
    let oddDigits = 0;

    for (let digit of number.slice(1)) {

        let num = digit;

        if (num > largestNumber) {
            largestNumber = num;
        }

        if (num < smallestNumber) {
            smallestNumber = num;
        }

        if (num % 2 == 0) {
            oddDigits = oddDigits + 1;
        } else {
            evenDigits = evenDigits + 1;
        }

        total = total + num;
    }

    console.log(`Largest: ${smallestNumber}`);
    console.log(`Smallest: ${largestNumber}`);
    console.log(`Sum: ${sum}`);
    console.log(`Even Digits: ${evenDigits}`);
    console.log(`Odd Digits: ${oddDigits}`);
}