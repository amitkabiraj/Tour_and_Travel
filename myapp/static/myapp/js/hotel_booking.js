function generateFields() {
    const numberOfMembers = parseInt(document.getElementById("numberOfMembers").value);
    const memberFields = document.getElementById("memberFields");

    // Clear previous fields
    memberFields.innerHTML = '';

    for (let i = 0; i < numberOfMembers; i++) {
        const memberDiv = document.createElement("div");
        memberDiv.className = "hotel_book_member-input";

        const nameLabel = document.createElement("label");
        nameLabel.textContent = `Member ${i + 1} Name:`;
        const nameInput = document.createElement("input");
        nameInput.type = "text";
        nameInput.name = `memberName${i + 1}`;
        nameInput.required = true;

        const genderLabel = document.createElement("label");
        genderLabel.textContent = `Member ${i + 1} Gender:`;
        const genderInput = document.createElement("select");
        genderInput.name = `memberGender${i + 1}`;
        genderInput.required = true;
        const genderOptions = ["Select", "Male", "Female", "Other"];
        for (const optionText of genderOptions) {
            const option = document.createElement("option");
            if (optionText === "Male") {
                option.value = "M";
            } else if (optionText === "Female") {
                option.value = "F";
            } else if (optionText === "Other") {
                option.value = "N";
            } else {
                option.value = optionText;
            }
            option.textContent = optionText;
            genderInput.appendChild(option);
        }

        const ageLabel = document.createElement("label");
        ageLabel.textContent = `Member ${i + 1} Age:`;
        const ageInput = document.createElement("input");
        ageInput.type = "number";
        ageInput.name = `memberAge${i + 1}`;
        ageInput.required = true;

        memberDiv.appendChild(nameLabel);
        memberDiv.appendChild(nameInput);
        memberDiv.appendChild(genderLabel);
        memberDiv.appendChild(genderInput);
        memberDiv.appendChild(ageLabel);
        memberDiv.appendChild(ageInput);

        memberFields.appendChild(memberDiv);
    }
}