// Elevator Floor Tracker

// Write a program that simulates the movement of an elevator in a building with 10 floors.

// The elevator initially starts at floor 1.
// Ask the user how many floor requests need to be processed.
// For each request, ask the user to enter the desired floor.
// If the requested floor is outside the range 1–10, display "Invalid floor" and ignore that request.
// If the requested floor is above the elevator's current floor, display "Moving UP".
// If the requested floor is below the current floor, display "Moving DOWN".
// If the elevator is already on the requested floor, display "Already on requested floor".
// After processing a valid request, update the elevator's current floor.
// Keep track of the total number of floors travelled throughout all valid requests.
// At the end, display:
// The elevator's final floor.
// The total number of floors travelled.

#include <stdio.h>

int main() {

    int current_floor = 1;

    int total_distance = 0;

    int number_of_requests;
    printf("Enter number of requests: ");
    scanf("%d", &number_of_requests);

    char requested_floor[50];

    for (int i = 0; i < number_of_requests - 1; i++) {

        printf("Enter requested floor: ");
        scanf("%s", requested_floor);

        if (requested_floor <= 1 || requested_floor >= 10) {
            printf("Invalid floor\n");
            continue;
        }

        current_floor = requested_floor;

        if (requested_floor > current_floor) {
            printf("Moving DOWN\n");

            total_distance = current_floor - requested_floor;
        }

        else if (requested_floor < current_floor) {
            printf("Moving UP\n");

            total_distance = current_floor - requested_floor;
        }

        else {
            printf("Already on requested floor\n");
        }
    }

    printf("Final floor: %d\n", current_floor);

    printf("Total floors travelled: %d\n", total_distance);

    return 0;
}