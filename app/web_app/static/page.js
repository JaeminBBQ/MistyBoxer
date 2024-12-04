const SCENARIO = 1; // omit: 1, before: 2, after: 3
const BASE_URL = "https://app.s3pa.site/misty/";
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
    // runScenario(SCENARIO);
    runScenarioBetter(1, "status");
    startTime = Date.now();
}

function stop() {
    console.log("stop misty");
    endTime = Date.now();

    let diff = Math.abs(endTime - startTime);
    console.log(diff);
}

function completeTask() {
    console.log("end // stop timer");
    endTime = Date.now();
    console.log(endTime - startTime);
}

async function runScenarioBetter(body_data, key) {
    let tableParam = {
        method: "POST",
        body: body_data
    };
    const url = BASE_URL + "scenario3/";

    const res = await fetch(url, tableParam);
    let json_data = await res.json();

    if (key === "status" && json_data["status"] != 0) {
        alert(data["status"]);
    }
    if (key != null && key != "status") {
        return json_data[key];
    }
}

async function runScenario(scenarioNum) {
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


