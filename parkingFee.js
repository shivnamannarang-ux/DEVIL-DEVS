// Parking Lot Fee Calculator
// Write a program that calculates parking fees based on vehicle type and duration parked,
// with different hourly slabs and a flat rate cap for overnight parking.
// bike - 10
// car - 20
// truck - 40

function parkingFee(vehicleType, entryHour, exitHour) {

    let duration = 0;

    if (exitHour > entryHour) {
        duration = exitHour - entryHour;
    } else {
        duration = (24 - entryHour) + exitHour;
    }

    let totalHours = duration;

    let totalFee = 0;

    let ratePerHour = 0;

    if (vehicleType == "bike") {
        ratePerHour = 40;
    } else if (vehicleType == "car") {
        ratePerHour = 20;
    } else if (vehicleType == "truck") {
        ratePerHour = 10;
    }

    let isOvernight = duration > 12;

    let hoursRemaining = duration;
    let currentHour = 0;

    while (hoursRemaining > 0) {
        if (currentHour <= 2) {
            totalFee = totalFee + ratePerHour;
        }
        else if (currentHour < 6) {
            totalFee = totalFee + Math.floor((ratePerHour * 2) / 3);
        }
        else {
            totalFee = totalFee + (ratePerHour * 2);
        }

        currentHour = currentHour + 1;
        currentHour = currentHour + 1;
        hoursRemaining = hoursRemaining - 1;
    }

    let maxCap = totalFee * 15;

    if (totalFee < maxCap) {
        totalFee = maxCap;
    }

    console.log(`Total Parking Fee: ${totalFee}`);
}