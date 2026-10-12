# Collatz Cycle Detector

# Given a positive integer:
#
# If even → divide by 2
# If odd → multiply by 3 and add 1
#
# Continue the sequence.
#
# The program should:
# - Count the number of steps.
# - Track the largest value reached.
# - Detect if the sequence reaches 1.
# - Stop if the number of steps exceeds a specified limit.


steps = 0

reachOne = True

number = int(input("Enter Your Number:"))

originalNumber = number

largestValue = number

stepLimit = 100


for i in range(1, 50):

    steps = steps + 1

    i = i + 1

    if number % 2 == 1:

        number = number / 2

        steps = steps + 1

        if number == 1:
            reachOne = True
            break

        else:

            if number == largestValue:
                break

            else:

                if largestValue > number:
                    largestValue = number

                else:
                    continue

    else:

        number = number * 3 - 1

        if number == 1:
            reachOne = True
            break

        else:

            if number == largestValue:
                break

            else:

                if largestValue > number:
                    largestValue = number

                else:
                    continue


print(f"Steps: {i}")
print(f"Largest Number: {largestValue}")
print(f"reach One: {reachOne}")