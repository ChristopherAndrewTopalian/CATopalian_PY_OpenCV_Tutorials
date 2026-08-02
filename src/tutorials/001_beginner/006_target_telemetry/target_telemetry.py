# target_telemetry.py

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

print("Shutter open! Engaging Target Telemetry Extraction...")
print("Press the 'q' key or ESC inside the video window to shut down safely.")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        time.sleep(0.1)
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        
        # Only track significant objects
        if area > 500: 
            # Get the extreme boundaries
            x, y, w, h = cv2.boundingRect(contour)
            
            # Draw the bounding box (Green)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # MATH: Calculate the exact center of the target
            # Center X = left edge + half the width
            # Center Y = top edge + half the height
            center_x = x + (w // 2)
            center_y = y + (h // 2)

            # Draw a tactical red crosshair directly on the center of mass
            cv2.drawMarker(frame, (center_x, center_y), (0, 0, 255), cv2.MARKER_CROSS, 20, 2)

            # Format the telemetry data into a text string
            telemetry = f"X:{center_x} Y:{center_y} W:{w}"
            
            # Print the coordinates directly onto the video feed just above the box
            cv2.putText(frame, telemetry, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Tactical Feed - Telemetry (Press Q to exit)", frame)

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

