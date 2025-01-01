function classifyText() {
    const inputText = document.getElementById('inputText').value.trim();
    const resultDiv = document.getElementById('result');
    resultDiv.innerText = ""; // Clear previous results

    if (!inputText) {
        resultDiv.innerHTML = '<span class="error">Please enter some text to classify!</span>';
        return;
    }

    fetch('/classify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: 'input_text=' + encodeURIComponent(inputText)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = `<span class="error">${data.error}</span>`;
        } else {
            resultDiv.innerHTML = `
                <strong>Naive Bayes:</strong> ${data['Naive Bayes Prediction']}<br>
                <strong>SVM:</strong> ${data['SVM Prediction']}<br>
                <strong>Complement Naive Bayes:</strong> ${data['Complement Naive Bayes Prediction']}
            `;
        }
    })
    .catch(error => {
        resultDiv.innerHTML = `<span class="error">An error occurred: ${error.message}</span>`;
    });
}
