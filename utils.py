import cv2
import os
from cvzone.HandTrackingModule import HandDetector

def process_gesture(image_path):
    # Read the uploaded image
    photo = cv2.imread(image_path)
    if photo is None:
        return "Error loading the image."

    detector = HandDetector()

    # Detect hands in the image
    hands = detector.findHands(photo, draw=False)
    if hands and len(hands[0]) > 0:
        hand_info = hands[0][0]  
        fingers = detector.fingersUp(hand_info)

        count = sum(fingers)

        action = {
            5: ("Opening Notepad", "notepad"),
            4: ("Opening Camera", "start microsoft.windows.camera:"),
            3: ("Opening Command Prompt", "start cmd"),
            2: ("Opening Microsoft Edge", "start msedge"),
            1: ("Opening Calendar", "start outlookcal:")
        }

        if count in action:
            message, command = action[count]
            os.system(command)
            return message
        else:
            return "No specific gesture detected."
    else:
        return "No hands detected."
