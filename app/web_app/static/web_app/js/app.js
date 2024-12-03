
async function post_request( body_data, url, key) {
    let tableParam = {
        method: 'POST',
        body: body_data
    }

    const res = await fetch(url, tableParam);
    let json_data = await res.json();

    if (key == "status" && json_data["status"] != 0) {
        alert(data["status"]);
    }
    if (key != null && key != "status"){
        return json_data[key];
    }
}

let goal_button = document.getElementById("goal_button");

goal_button.onclick = () => {
    console.log("Hello hello");
    post_request(1, "http://localhost:8000/misty/scenario1/");
}