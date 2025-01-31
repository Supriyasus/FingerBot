# FingerBot
This project utilizes computer vision to detect the number of fingers shown to the camera and executes different system commands based on the count. It uses OpenCV, Mediapipe, and CVZone for hand tracking and gesture recognition.

## Features

Detects the number of fingers displayed in front of the camera.

Executes different system commands based on the detected finger count:

1 Finger: Opens Outlook Calendar.

2 Fingers: Launches Microsoft Edge.

3 Fingers: Opens Command Prompt.

4 Fingers: Opens Camera.

5 Fingers: Opens Notepad.

No Hands Detected: Displays a message.

## Technologies Used

Python

OpenCV (cv2)

Mediapipe (mp)

CVZone (cvzone)

OS Module (os)

## Installation

To run the project, install the required dependencies:

    pip install opencv-python cvzone mediapipe

## Usage

Run the script using:

    python main.py

Ensure your webcam is connected and place your hand in front of the camera to trigger commands.



