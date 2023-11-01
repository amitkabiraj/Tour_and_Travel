const menuIcon = document.querySelector(".menu-icon");
const navLinks = document.querySelector(".nav-links");

menuIcon.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});
//car js

    // Get references to the relevant form elements
    const placeSelector = document.getElementById("placeSelector");
    const seatsSelect = document.getElementById("seatsSelect");
    const numMembers = document.getElementById("numMembers");
    const numCars = document.getElementById("numCars");
    const date = document.getElementById("date");

    // Get a reference to the form itself
    const placeForm = document.getElementById("placeForm");

    // Add an event listener to the form's submit button
    placeForm.addEventListener("submit", function (e) {
        // Prevent the default form submission behavior
        e.preventDefault();

        // Get the selected values from the form elements
        const selectedPlace = placeSelector.value;
        // const selectedSeats = seatsSelect.value;
        // const selectedMembers = numMembers.value;
        // const selectedCars = numCars.value;
        // const selectedDate = date.value;

        // Create a URL based on the selected values
        const redirectURL = selectedPlace 
                    // "seats=" + selectedSeats + "&" +
            // "members=" + selectedMembers + "&" +
            // "cars=" + selectedCars + "&" +
            // "date=" + selectedDate;

        // Redirect to the constructed URL
        window.location.href = redirectURL;
    });
// CAR select for place page  javascript

function selectImage(checkboxId) {
  document.getElementById(checkboxId).click();
}


