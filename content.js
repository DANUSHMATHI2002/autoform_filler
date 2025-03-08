fetch("http://localhost:5000/data")
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error("Error fetching data:", data.error);
            return;
        }

        Object.keys(data).forEach(field => {
            let input = document.querySelector(`input[name="${field}"], textarea[name="${field}"]`);
            if (input) {
                input.value = data[field] || "";
            }
        });
    })
    .catch(error => console.error("Error loading data:", error));
