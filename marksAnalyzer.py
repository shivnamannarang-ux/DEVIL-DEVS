# Student Marks Analyzer
# Write a program that accepts the marks obtained by a student in five subjects.
# The program should determine the highest marks, lowest marks, and average marks obtained by the student, and display all three results.

# Variables to Store Highest, Lowest and Average Marks
highestMarks = 100 #Unnecessary semicolons were removed due to incorrect syntax #incorrect value was written in the variable it was supposed to be 100 
lowestMarks = 0 #Unnecessary semicolons were removed due to incorrect syntax #incorrect value was written in the variable it was supposed to be 0 


# Taking Marks for Five Subjects as Inputint(
subject1 = int(input("Enter Marks for Subject 1: ")) #Unnecessary semicolons were removed due to incorrect syntax #Typecasting was done to change store the entered value as integer in the variable
subject2 = int(input("Enter Marks for Subject 2: ")) #Unnecessary semicolons were removed due to incorrect syntax #Typecasting was done to change store the entered value as integer in the variable
subject3 = int(input("Enter Marks for Subject 3: ")) #Unnecessary semicolons were removed due to incorrect syntax #Typecasting was done to change store the entered value as integer in the variable
subject4 = int(input("Enter Marks for Subject 4: ")) #Unnecessary semicolons were removed due to incorrect syntax #Typecasting was done to change store the entered value as integer in the variable
subject5 = int(input("Enter Marks for Subject 5: ")) #Unnecessary semicolons were removed due to incorrect syntax #Typecasting was done to change store the entered value as integer in the variable



# Finding the Highest Marks 
#If condition logics were changed as they were wrong for evaluating the highest marks 
if subject1>subject2 and subject1>subject3 and subject1>subject4 and subject1>subject5 :
    print(f"Highest Marks = {subject1}") #Unnecessary semicolons were removed due to incorrect syntax

elif subject2>subject3 and subject2>subject1 and subject2>subject4 and subject2>subject5 :
    print(f"Highest Marks = {subject2}") #Unnecessary semicolons were removed due to incorrect syntax

elif subject3>subject1 and subject3>subject2 and subject3>subject4 and subject3>subject5 :
    print(f"Highest Marks = {subject3}") #Unnecessary semicolons were removed due to incorrect syntax

elif subject4>subject1 and subject4>subject2 and subject4>subject3 and subject4>subject5 :
    print(f"Highest Marks = {subject4}") #Unnecessary semicolons were removed due to incorrect syntax

elif subject5>subject1 and subject5>subject2 and subject5>subject3 and subject5>subject4 :  
    print(f"Highest Marks = {subject5}") #Unnecessary semicolons were removed due to incorrect syntax




# Finding the Lowest Marks
if subject1<subject2 and subject1<subject3 and subject1<subject4 and subject1<subject5 :
    print(f"Lowest Marks = {subject1}") #Unnecessary semicolons were removed due to incorrect syntax

elif subject2<subject3 and subject2<subject1 and subject2<subject4 and subject2<subject5 :
    print(f"Lowest Marks = {subject2}") #Unnecessary semicolons were removed due to incorrect syntax

elif subject3<subject1 and subject3<subject2 and subject3<subject4 and subject3<subject5 :
    print(f"Lowest Marks = {subject3}") #Unnecessary semicolons were removed due to incorrect syntax

elif subject4<subject1 and subject4<subject2 and subject4<subject3 and subject4<subject5 :
    print(f"Lowest Marks = {subject4}") #Unnecessary semicolons were removed due to incorrect syntax

elif subject5<subject1 and subject5<subject2 and subject5<subject3 and subject5<subject4 :  
    print(f"Lowest Marks = {subject5}") #Unnecessary semicolons were removed due to incorrect syntax



# Calculating the Average Marks
avg = (subject1 + subject2 + subject3 + subject4 + subject5) / 5 #Unnecessary semicolons were removed due to incorrect syntax

# Displaying the Results 
print(f"Average: {avg}") #Unnecessary semicolons were removed due to incorrect syntax