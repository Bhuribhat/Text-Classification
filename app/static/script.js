function submitText() {
    const textArea = document.getElementById('text');
    const text = textArea.value;
    console.log(text);

    // Serialize the input as JSON
    const payload = JSON.stringify({ 'text': text });

    // Create a new request
    const xhr = new XMLHttpRequest();

    // Set the request URL and method
    xhr.open('POST', '/predict');

    // Set the request headers
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Define the callback function when the request completes
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            const result = document.querySelector('.result');

            // Update the result element
            if (result) {
                result.innerHTML = `
                    <h3>Detected Language:</h3>
                    <p>${response.language}</p>
                `;

                // Enable or disable the classify button based on the language
                const classifyButton = document.getElementById('classifyButton');
                if (response.language === 'English') {
                    classifyButton.disabled = false;
                } else {
                    classifyButton.disabled = true;
                }
            }
        } else {
            console.error(xhr.status);
        }
    }

    // Send the request with the serialized payload
    xhr.send(payload);
};


function classifyText() {
    const textArea = document.getElementById('text');
    const text = textArea.value;
    console.log(text);

    // Serialize the input as JSON
    const payload = JSON.stringify({ 'text': text });

    // Create a new request
    const xhr = new XMLHttpRequest();

    // Set the request URL and method
    xhr.open('POST', '/classify');

    // Set the request headers
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Define the callback function when the request completes
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            const result = document.querySelector('.classificationResult');
            console.log(response.prediction);

            // Update the result element
            if (result) {
                result.innerHTML = `
                    <h3>Classification:</h3>
                    <p>${response.prediction}</p>
                `;
            }
        } else {
            console.error(xhr.status);
        }
    };

    // Send the request with the serialized payload
    xhr.send(payload);
};