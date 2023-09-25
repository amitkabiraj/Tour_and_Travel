const menuIcon = document.querySelector(".menu-icon");
const navLinks = document.querySelector(".nav-links");

menuIcon.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});
// Car js 


document.getElementById("placeForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent the form from submitting normally
  
  // Get the selected place from the dropdown
  var placeSelector = document.getElementById("placeSelector");
  var selectedPlace = placeSelector.options[placeSelector.selectedIndex].value;
  
  // Redirect to the appropriate URL based on the selected place
  if (selectedPlace === "Nadia") {
    window.location.href = "{% url 'nadia_car' %}"; // Replace with your URL for Place A
  } else if (selectedPlace === "Murshidabad") {
    window.location.href = "{% url 'murshidabad_car' %}"; // Replace with your URL for Place B
  }
  alert("JavaScript code is executing!");
});

