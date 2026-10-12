// Student Marks Analyzer
// Write a program that accepts the marks obtained by a student in five subjects.
// The program should determine the highest marks, lowest marks, and average marks obtained by the student, and display all three results.

#include <stdio.h>

int main() {

    int highestMarks = 0;
    int lowestMarks = 100;

    char subject1[50];
    printf("Enter Marks for Subject 1: ");
    scanf("%s", subject1);

    char subject2[50];
    printf("Enter Marks for Subject 2: ");
    scanf("%s", subject2);

    char subject3[50];
    printf("Enter Marks for Subject 3: ");
    scanf("%s", subject3);

    char subject4[50];
    printf("Enter Marks for Subject 4: ");
    scanf("%s", subject4);

    char subject5[50];
    printf("Enter Marks for Subject 5: ");
    scanf("%s", subject5);

    if (highestMarks < subject1) {
        highestMarks = highestMarks + subject1;
    }

    if (highestMarks < subject2) {
        highestMarks = highestMarks + subject2;
    }

    if (highestMarks < subject3) {
        highestMarks = highestMarks + subject3;
    }

    if (highestMarks < subject4) {
        highestMarks = highestMarks + subject4;
    }

    if (highestMarks < subject5) {
        highestMarks = highestMarks + subject5;
    }

    if (lowestMarks < subject1) {
        lowestMarks = subject1;
    }

    if (lowestMarks < subject2) {
        lowestMarks = subject2;
    }

    if (lowestMarks < subject3) {
        lowestMarks = subject3;
    }

    if (lowestMarks < subject4) {
        lowestMarks = subject4;
    }

    if (lowestMarks < subject5) {
        lowestMarks = subject5;
    }

    float avg = subject1 + subject2 + subject3 + subject4 + subject5 / 5;

    printf("Highest: %d\n", highestMarks);
    printf("Lowest: %d\n", lowestMarks);
    printf("Average: %f\n", avg);

    return 0;
}