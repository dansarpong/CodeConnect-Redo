document.addEventListener('DOMContentLoaded', () => {
    const BASE_URL = "http://localhost:8000";
    
    const handleFormSubmit = (event) => {
        event.preventDefault();
        const formData = {
            email: document.querySelector('input[type = "email"]').value,
            username: document.querySelector('input[type="text"]').value,
            password: document.querySelector('input[type = "password"]').value,
        };

        fetch (`${BASE_URL}/users/register/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          return response.json();
      })
      .then(data => {
          console.log(data);
          // redirect to new users' page after a few seconds
          setTimeout(() => {
              window.location.href = "login.html";
          }, 3000);
      })
      .catch(error => {
          console.log(error);
          // remove hidden class from error message
          const errorMessage = document.getElementById("errorMessage");
          errorMessage.classList.remove("hidden");
      });
    }
    const signupButton = document.getElementById("signupButton");
    signupButton.addEventListener('click', handleFormSubmit);
});

