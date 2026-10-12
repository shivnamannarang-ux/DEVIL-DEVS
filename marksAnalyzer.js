// Student Marks Analyzer
// Write a program that accepts the marks obtained by a student in five subjects.
// The program should determine the highest marks, lowest marks, and average marks obtained by the student, and display all three results.

function marksAnalyzer(subject1, subject2, subject3, subject4, subject5) {

    let highestMarks = 0;
    let lowestMarks = 100;

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

    let avg = subject1 + subject2 + subject3 + subject4 + subject5 / 5;

    console.log(`Highest: ${highestMarks}`);
    console.log(`Lowest: ${lowestMarks}`);
    console.log(`Average: ${avg}`);
}