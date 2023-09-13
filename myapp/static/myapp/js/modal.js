var modal = document.getElementById("myModal");

// Get the image and description elements within the modal
var modalImage = document.getElementById("modalImage");
var modalTitle = document.getElementById("modalTitle");
var modalDescription = document.getElementById("modalDescription");

// Get all container elements with class "container"
var containers = document.querySelectorAll(".container");

// Loop through containers and attach click event
containers.forEach(function(container) {
  container.addEventListener("click", function() {
    modal.style.display = "block";
    modalImage.src = this.querySelector("img").src;
    modalTitle.textContent = this.querySelector("h2").textContent;
    modalDescription.textContent = this.querySelector(".description p").textContent;
  });
});

// Get the close button element
var closeButton = document.getElementsByClassName("close")[0];

// Close the modal when the close button is clicked
closeButton.addEventListener("click", function() {
  modal.style.display = "none";
});