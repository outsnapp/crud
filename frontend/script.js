async function loadStudents() {

    const response = await fetch(
        "http://127.0.0.1:8000/students"
    );

    const students = await response.json();

    let html = "";

    students.forEach(student => {

        html += `
        <tr>
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>

            <td>
                <button onclick="editStudent(${student.id}, '${student.name}', ${student.age})">
                    Edit
                </button>

                <button onclick="deleteStudent(${student.id})">
                    Delete
                </button>
            </td>
        </tr>
        `;
    });

    document.getElementById("studentList").innerHTML = html;
}


document.getElementById("studentForm").addEventListener("submit", async (e) => {

    console.log("FORM SUBMITTED");

    e.preventDefault();

    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;

    console.log("Name:", name);
    console.log("Age:", age);

    const response = await fetch(
        `http://127.0.0.1:8000/students?name=${name}&age=${age}`,
        {
            method: "POST"
        }
    );

    console.log("Response status:", response.status);

    document.getElementById("studentForm").reset();

    loadStudents();
});


async function editStudent(id, currentName, currentAge) {

    const name = prompt(
        "Enter new name",
        currentName
    );

    const age = prompt(
        "Enter new age",
        currentAge
    );

    if (name === null || age === null) {
        return;
    }

    await fetch(
        `http://127.0.0.1:8000/students/${id}?name=${name}&age=${age}`,
        {
            method: "PUT"
        }
    );

    loadStudents();
}


async function deleteStudent(id) {

    await fetch(
        `http://127.0.0.1:8000/students/${id}`,
        {
            method: "DELETE"
        }
    );

    loadStudents();
}


loadStudents();