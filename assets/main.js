
const slogan = document.querySelector('.slogan')
const textToType = "Welcome to twichiyat where we believe in giving new life to pre-loved treasures.\nTwichiyat where Every Item Tells a Story";
const speed = 30; // Adjust the typing speed (milliseconds per character)

function typeText() {
    console.log('something')
    let i = 0;
    const intervalId = setInterval(() => {
        slogan.textContent += textToType[i];
        i++;
        if (i === textToType.length) {
            clearInterval(intervalId);
        }
        }, speed);
    }

        // Call the function to start typing when the page loads
window.onload = typeText;

function reveal() {
    var reveals = document.querySelectorAll(".reveal");
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 150;
  
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }
  
  window.addEventListener("scroll", reveal);
  
