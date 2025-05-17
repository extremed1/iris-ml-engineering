document.getElementById("predictionform").addEventListener("submit", async function (e) {
    e.preventDefault();

    // Get the input values
    const sepalLength = parseFloat(document.getElementById("input1").value);
    const sepalWidth = parseFloat(document.getElementById("input2").value);
    const petalLength = parseFloat(document.getElementById("input3").value);
    const petalWidth = parseFloat(document.getElementById("input4").value);

    // Prepare the payload in the expected structure
    const data = {
        sepalLength,
        sepalWidth,
        petalLength,
        petalWidth
    };

    try {
        const response = await fetch("https://irispredictions.redglacier-78667baa.eastus.azurecontainerapps.io/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const result = await response.json();
        const speciesTitleCase = result.species.charAt(0).toUpperCase() + result.species.slice(1).toLowerCase();
        document.getElementById("result").innerText = `🌸 Predicted Species: ${speciesTitleCase}`;
    } catch (error) {
        console.error("Prediction error:", error);
        document.getElementById("result").innerText = "❌ Failed to get prediction. Please check your inputs or try again later.";
    }
});
