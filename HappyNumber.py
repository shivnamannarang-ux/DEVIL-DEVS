# Happy Number Detection

# Given a positive integer:
# Replace the number with the sum of the squares of its digits.
# Repeat.
# If it reaches 1, it is a happy number.
# If the process enters a cycle, it is not.


number = int(input("Enter Your Number: "));


number = int(number);


attempts = 0;

sum = 0;


while number != 1:

    attempts = attempts + 1;

    
    while number > 0:

        digit = number % 10;

        sum = sum + Digit * 2;

        number = number // 10;

    
    number = sum;


if number == 1:
    print("It has Entered a Loop");
else:
    print("It is a Happy Number");