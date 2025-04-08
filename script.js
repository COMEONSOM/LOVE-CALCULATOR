let button = document.querySelector('button');
let attempts = 0;

button.addEventListener('click', function() {
    attempts++;
    if (attempts <= 3) {
        // Add a class for the button animation
        button.classList.add('button-animate');
        // Disable the button during animation
        button.disabled = true;
        // After 1 second, remove the animation class and enable the button
        setTimeout(function() {
            button.classList.remove('button-animate');
            button.disabled = false;
        }, 1000); // Adjust the time according to your animation duration
    } else {
        // Allow the button to be clicked after 3 attempts
        button.disabled = false;
    }
});

function calculateLove() {
    var yourNameInput = document.getElementById('yourName');
    var partnerNameInput = document.getElementById('partnerName');
    var resultDiv = document.getElementById('result');

    // Check if input fields exist
    if (!yourNameInput || !partnerNameInput || !resultDiv) {
        console.error("Required elements not found.");
        return; // Exit function if elements are missing
    }

    var yourName = yourNameInput.value.trim().toLowerCase();
    var partnerName = partnerNameInput.value.trim().toLowerCase();

    // Check if names are entered
    if (!yourName || !partnerName) {
        resultDiv.innerHTML = "<p>Please enter both names to calculate.</p>";
        return; // Exit function if names are missing
    }

    // Check if names contain special characters or numbers
    var regex = /^[a-zA-Z\s]*$/; // Only allow letters and spaces
    if (!regex.test(yourName) || !regex.test(partnerName)) {
        resultDiv.innerHTML = "<p>Please enter only letters (A-Z) and spaces for names.</p>";
        return; // Exit function if invalid characters are found
    }

    // Check for inappropriate words
    var inappropriateWords = ["badword1", "fuck", "lawde", "harami", "madarchod","bal"]; // Add your list of inappropriate words
    if (containsInappropriateWord(yourName, inappropriateWords) || containsInappropriateWord(partnerName, inappropriateWords)) {
        resultDiv.innerHTML = "<p>One or both names contain inappropriate words. Please enter appropriate names.</p>";
        return; // Exit function if inappropriate words are found
    }

    // Some random calculations
    var lovePercentage = Math.floor(Math.random() * 100) + 1;

    // Display the result
    resultDiv.innerHTML = "<p>According to our complex algorithm...</p>";
    resultDiv.innerHTML += "<p><strong>" + yourName.toUpperCase() + "</strong> and <strong>" + partnerName.toUpperCase() + "</strong> have a love compatibility of <strong>" + lovePercentage + "%</strong>!</p>";

    if (lovePercentage >= 90) {
        resultDiv.innerHTML += "<p>Wow! You two are absolutely perfect for each other! Cherish your love!</p>";
    } else if (lovePercentage >= 80) {
        resultDiv.innerHTML += "<p>Your love is incredibly strong! Keep nurturing it!</p>";
    } else if (lovePercentage >= 70) {
        resultDiv.innerHTML += "<p>You two share a wonderful connection! Keep building on it!</p>";
    } else if (lovePercentage >= 60) {
        resultDiv.innerHTML += "<p>Your relationship has great potential! Keep investing in each other!</p>";
    } else if (lovePercentage >= 50) {
        resultDiv.innerHTML += "<p>You make a lovely couple! Keep enjoying each other's company!</p>";
    } else {
        resultDiv.innerHTML += "<p>Every relationship has its ups and downs. Keep communicating and supporting each other!</p>";
    }
}

// Function to check if a string contains inappropriate words
function containsInappropriateWord(input, inappropriateWords) {
    for (var i = 0; i < inappropriateWords.length; i++) {
        if (input.includes(inappropriateWords[i])) {
            return true; // Return true if an inappropriate word is found
        }
    }
    return false; // Return false if no inappropriate words are found
}
