document.addEventListener("DOMContentLoaded", () => {
    const startCameraBtn = document.getElementById("startCamera");
    const captureBtn = document.getElementById("capture");
    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const resultDiv = document.getElementById("result");

    let stream;

    // Start Camera
    startCameraBtn.addEventListener("click", async () => {
        try {
            stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            video.classList.remove("hidden");
            captureBtn.classList.remove("hidden");
            startCameraBtn.classList.add("hidden");  // Hide Start Camera after activation
        } catch (error) {
            console.error("Error accessing the camera:", error);
            resultDiv.textContent = "Error accessing the camera.";
        }
    });

    // Capture Gesture
    captureBtn.addEventListener("click", () => {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

        const imageData = canvas.toDataURL("image/png");

        // Send captured image to Flask server
        fetch("/detect", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ image: imageData })
        })
        .then(response => response.json())
        .then(data => {
            if (data.result) {
                resultDiv.textContent = `Detected Gesture: ${data.result}`;
            } else {
                resultDiv.textContent = "No gesture detected.";
            }
        })
        .catch(error => {
            console.error("Error:", error);
            resultDiv.textContent = "Error processing gesture.";
        });
    });
});
