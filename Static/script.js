async function submitReview() {
  const review = document.getElementById("review").value;

  const response = await fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ review: review })
  });

  const data = await response.json();

  // Use the correct key from the backend response
  document.getElementById("result").innerText = `This review is likely: ${data.prediction}`;
  document.getElementById("result-card").classList.remove("hidden");
}
