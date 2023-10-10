const menuIcon = document.querySelector(".menu-icon");
const navLinks = document.querySelector(".nav-links");

menuIcon.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});
// Car js 


// document.getElementById("placeForm").addEventListener("submit", function(event) {
//   event.preventDefault(); // Prevent the form from submitting normally
  
//   // Get the selected place from the dropdown
//   var placeSelector = document.getElementById("placeSelector");
//   var selectedPlace = placeSelector.options[placeSelector.selectedIndex].value;
  
//   // Redirect to the appropriate URL based on the selected place
//   if (selectedPlace === "Nadia") {
//     window.location.href = "{% url 'nadia_car' %}"; // Replace with your URL for Place A
//   } else if (selectedPlace === "Murshidabad") {
//     window.location.href = "{% url 'murshidabad_car' %}"; // Replace with your URL for Place B
//   }
//   // alert("JavaScript code is executing!");
// });

 // Get the form and its elements
 const placeForm = document.getElementById('placeForm');
 const placeSelector = document.getElementById('placeSelector');
 const numMembers = document.getElementById('numMembers');
 const numCars = document.getElementById('numCars');
 const numSeats = document.getElementById('numSeats');
 
 // Add an event listener to the form submission
 placeForm.addEventListener('submit', function (event) {
   event.preventDefault(); // Prevent the form from actually submitting
   
   // Get the selected option's value and other input values
   const selectedPage = placeSelector.value;
   const selectedMembers = numMembers.value;
   const selectedCars = numCars.value;
   const selectedSeats = numSeats.value;
   
   // Construct the URL based on the selectedPage
   let redirectURL = '';
   switch (selectedPage) {
     case 'nadia':
     redirectURL = 'nadia_car.html';
     break;
     case 'Murshidabad':
     redirectURL = 'murshidabad_car.html';
     break;
     default:
     // Handle any other cases or provide a default action
     break;
   }
   
   // Append query parameters to the URL
   redirectURL += `?members=${selectedMembers}&cars=${selectedCars}&seats=${selectedSeats}`;
   
   // Redirect to the constructed URL
   window.location.href = redirectURL;
 });


