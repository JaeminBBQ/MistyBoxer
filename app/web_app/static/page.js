const SCENARIO = 1; // omit: 1, before: 2, after: 3
let startTime = endTime = 0;

function start() {
    const selectElement = document.getElementById("taskSelect");
    const selectValue = selectElement.value;
    if (selectValue !== "E") {
        console.error("Incorrect option selected");
        return;
    }
    console.log("start timer");
    console.log("Running scenario ", SCENARIO);
    runScenario(SCENARIO);
    startTime = Date.now();
}

function stop() {
    console.log("stop misty");
}

function completeTask() {
    console.log("end // stop timer");
    endTime = Date.now();
    console.log(endTime - startTime);
}

function runScenario(scenarioNum) {
    if (scenarioNum === 1) {
        // omit, control
        console.log("Omit");
    }
    else if (scenarioNum === 2) {
        console.log("Before");
    }
    else if (scenarioNum === 3) {
        console.log("After");
    }
    else {
        console.error("Not implemented");
    }
}
