# bounding_box.py

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

print("Shutter open! Engaging Object Localization (Bounding Boxes)...")
print("Press the 'q' key or ESC inside the video window to shut down safely.")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        time.sleep(0.1)
        continue

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract edges (The eagle vision)
    edges = cv2.Canny(gray, 50, 150)

    # Find the groupings of edges (Contours)
    # RETR_EXTERNAL tells the engine to only look at the outside edges of objects
    # CHAIN_APPROX_SIMPLE compresses the geometry data to save memory
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a Bounding Box around the largest edge groupings
    for contour in contours:
        # Calculate the area of the grouping
        area = cv2.contourArea(contour)
        
        # Only target groupings larger than 500 pixels (Ignore dust and static)
        if area > 500: 
            # The C++ Engine performs the Extreme Search (minX, minY, maxX, maxY)
            x, y, w, h = cv2.boundingRect(contour)
            
            # Draw a tactical green box on the ORIGINAL color frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the live feed with active targeting boxes overlay
    cv2.imshow("Tactical Feed - Bounding Box (Press Q to exit)", frame)

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

