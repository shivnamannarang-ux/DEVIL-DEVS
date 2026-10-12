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

function elevatorController(numberOfRequests, floorRequests) {

    let current_floor = 1;

    let total_distance = 0;

    for (let i = 0; i < numberOfRequests - 1; i++) {

        let requested_floor = floorRequests[i];

        if (requested_floor <= 1 || requested_floor >= 10) {
            console.log("Invalid floor");
            continue;
        }

        current_floor = requested_floor;

        if (requested_floor > current_floor) {
            console.log("Moving DOWN");

            total_distance = current_floor - requested_floor;
        }

        else if (requested_floor < current_floor) {
            console.log("Moving UP");

            total_distance = current_floor - requested_floor;
        }

        else {
            console.log("Already on requested floor");
        }
    }

    console.log("Final floor:", current_floor);

    console.log("Total floors travelled:", total_distance);
}