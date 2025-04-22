async function submitReview() {
    const review = document.getElementById("review").value;
    const response = await fetch("/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ review: review })
    });
  
    const data = await response.json();
    document.getElementById("result").innerText = data.result;
    document.getElementById("result-card").classList.remove("hidden");
  }
  