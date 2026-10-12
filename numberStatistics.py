# Number Statistics

# The program takes a positive integer and processes every digit to determine:
# - Largest digit
# - Smallest digit
# - Digit sum
# - Number of even digits
# - Number of odd digits



number = input("Enter Your Number:")


largestNumber = 9
smallestNumber = 0

sum = 0

digitCount = len(number)

total = 0

evenDigits = 0
oddDigits = 0


for digit in number[1:]:

    
    num = digit

    
    if num > largestNumber:
        largestNumber = num

    
    if num < smallestNumber:
        smallestNumber = num

    
    if num % 2 == 0:
        oddDigits = oddDigits + 1
    else:
        evenDigits = evenDigits + 1

    
    total = total + num


# Displaying the Results
print(f"Largest: {smallestNumber}")
print(f"Smallest: {largestNumber}")
print(f"Sum: {sum}")
print(f"Even Digits: {evenDigits}")
print(f"Odd Digits: {oddDigits}")