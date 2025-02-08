# FingerBot Gesture Control

FingerBot is a web application that detects hand gestures using your webcam and triggers specific system actions based on the number of fingers shown.

Features

Real-time hand gesture detection

System actions triggered by specific gestures:

5 Fingers: Opens Notepad

4 Fingers: Opens Camera

3 Fingers: Opens Command Prompt

2 Fingers: Opens Microsoft Edge

1 Finger: Opens Calendar

## Deployment

The project is deployed and accessible via [your deployed link].

## Usage

Open the application in your browser.

Click on "Start Camera".

Show a gesture with your fingers.

Click "Detect Gesture" to trigger the corresponding action.

## Technologies Used

Python (Flask)

OpenCV

cvzone (HandTrackingModule)

HTML, CSS (Tailwind), JavaScript

## Setup (For Local Development)

Clone the repository: 

    git clone <repository-url>
    cd Finger_Bot
        
Install dependencies:

    pip install -r requirements.txt

Run the Flask app:

    python app.py

Open http://localhost:5000 in your browser.
