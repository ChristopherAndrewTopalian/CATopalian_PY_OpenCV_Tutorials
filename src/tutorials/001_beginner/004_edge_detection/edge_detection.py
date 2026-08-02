# edge_detection.py

import cv2
import time

print("Bypassing Windows Media Foundation, Using DirectShow")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
time.sleep(1)

print("Checking sensor connection...")
if not cap.isOpened():
    print("WARNING: Index 0 failed. Attempting Camera Index 1...")
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Could not connect to camera.")
    exit()

print("Shutter open! Engaging structural edge detection...")
print("Press the 'q' key or ESC inside the video window to shut down safely.")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        time.sleep(0.1)
        continue

    # Convert to grayscale (Edge detection requires a single-channel image)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply the Canny Edge Detection algorithm
    # The numbers 50 and 150 are the lower and upper thresholds.
    # Any pixel intensity change greater than 150 is guaranteed to be an edge.
    edges = cv2.Canny(gray, 50, 150)

    # Display the geometric structural feed
    cv2.imshow("Tactical Feed - Edge Radar (Press Q to exit)", edges)

    # Check for shutdown command
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

print("Releasing hardware sensor and closing windows...")
cap.release()
cv2.destroyAllWindows()
print("Clean shutdown complete.")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2026-present
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

