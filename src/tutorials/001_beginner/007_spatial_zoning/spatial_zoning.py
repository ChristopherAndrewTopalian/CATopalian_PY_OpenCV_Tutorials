# spatial_zoning.py

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

print("Shutter open! Engaging Spatial Zoning Grid...")
print("Press the 'q' key or ESC inside the video window to shut down safely.")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        time.sleep(0.1)
        continue

    # Get the dynamic width and height of the camera feed
    height, width, _ = frame.shape
    
    # Define our tactical sectors (Slice the screen into thirds)
    left_boundary = width // 3
    right_boundary = (width // 3) * 2

    # Draw the radar grid lines on the screen (Blue lines)
    cv2.line(frame, (left_boundary, 0), (left_boundary, height), (255, 0, 0), 2)
    cv2.line(frame, (right_boundary, 0), (right_boundary, height), (255, 0, 0), 2)

    # Standard Vision Pipeline
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # TACTICAL UPGRADE: Only track the single largest threat/object on screen
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        if area > 500:
            x, y, w, h = cv2.boundingRect(largest_contour)
            center_x = x + (w // 2)
            center_y = y + (h // 2)

            # Draw the bounding box and crosshair
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.drawMarker(frame, (center_x, center_y), (0, 0, 255), cv2.MARKER_CROSS, 20, 2)

            # SPATIAL LOGIC: Decide what to do based on the target's location
            command = "SEARCHING..."
            color = (255, 255, 255)

            if center_x < left_boundary:
                command = "ACTION: TURN LEFT"
                color = (0, 255, 255)  # Yellow
            elif center_x > right_boundary:
                command = "ACTION: TURN RIGHT"
                color = (0, 255, 255)  # Yellow
            else:
                command = "ACTION: TARGET LOCKED (CENTER)"
                color = (0, 0, 255)    # Red

            # Print the command at the top of the Heads-Up Display
            cv2.putText(frame, command, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    cv2.imshow("Tactical Feed - Spatial Zoning (Press Q to exit)", frame)

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

