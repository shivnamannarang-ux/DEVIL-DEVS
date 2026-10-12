# Student Marks Analyzer
# Write a program that accepts the marks obtained by a student in five subjects.
# The program should determine the highest marks, lowest marks, and average marks obtained by the student, and display all three results.

# Variables to Store Highest, Lowest and Average Marks
highestMarks = 0;
lowestMarks = 100;


# Taking Marks for Five Subjects as Input
subject1 = input("Enter Marks for Subject 1: ");
subject2 = input("Enter Marks for Subject 2: ");
subject3 = input("Enter Marks for Subject 3: ");
subject4 = input("Enter Marks for Subject 4: ");
subject5 = input("Enter Marks for Subject 5: ");



# Finding the Highest Marks
if highestMarks < subject1:
    highestMarks = highestMarks + subject1;

if highestMarks < subject2:
    highestMarks = highestMarks + subject2;

if highestMarks < subject3:
    highestMarks = highestMarks + subject3;

if highestMarks < subject4:
    highestMarks = highestMarks + subject4;

if highestMarks < subject5:
    highestMarks = highestMarks + subject5;




# Finding the Lowest Marks
if lowestMarks < subject1:
    lowestMarks = subject1;

if lowestMarks < subject2:
    lowestMarks = subject2;

if lowestMarks < subject3:
    lowestMarks = subject3;

if lowestMarks < subject4:
    lowestMarks = subject4;

if lowestMarks < subject5:
    lowestMarks = subject5;



# Calculating the Average Marks
avg = subject1 + subject2 + subject3 + subject4 + subject5 / 5;

# Displaying the Results
print(f"Highest: {highestMarks}");
print(f"Lowest: {lowestMarks}");
print(f"Average: {avg}");