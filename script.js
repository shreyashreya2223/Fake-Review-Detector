function submitReview() {
    const reviewText = document.getElementById("review").value;
  
    fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ review: reviewText })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").textContent = `Prediction: ${data.prediction}`;
      document.getElementById("result-card").classList.remove("hidden");
    })
    .catch(error => {
      document.getElementById("result").textContent = "Error analyzing review.";
      document.getElementById("result-card").classList.remove("hidden");
    });
  }
  