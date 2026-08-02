# intrusion_detection.py

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

print("Shutter open! Calibrating static background...")
print("Please step out of the frame for 2 seconds...")

# Allow the physical camera sensor to adjust its auto-exposure to the lighting
for i in range(30):
    ret, frame = cap.read()
    time.sleep(0.05)

# 1. Capture the BASELINE frame (The memory of the empty room)
ret, frame = cap.read()
baseline_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

print("Baseline locked. Perimeter secured. Monitoring for intrusions...")
print("Press 'r' to re-calibrate the baseline.")
print("Press 'q' or ESC to shut down safely.")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        time.sleep(0.1)
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Compare the current frame to the memory of the baseline frame
    # This subtracts the two images. Only pixels that have CHANGED will remain.
    delta = cv2.absdiff(baseline_frame, gray)

    # 3. Binarize the difference
    # If a pixel changed by a value of 30 or more, turn it pure white (255). 
    # Otherwise, ignore it and turn it black (0).
    _, thresh = cv2.threshold(delta, 30, 255, cv2.THRESH_BINARY)

    # 4. Find the edges of the changed pixels
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Default State
    status = "PERIMETER SECURE"
    color = (0, 255, 0) # Green

    for contour in contours:
        area = cv2.contourArea(contour)
        
        # EAGLE VISION FILTER: We didn't blur the image. We just tell the math 
        # to ignore any pixel changes smaller than 2000 pixels (dust, shadows).
        if area > 2000:
            status = "WARNING: INTRUSION DETECTED"
            color = (0, 0, 255) # Red
            
            # Draw a targeting box around the intruder
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    # Draw the HUD
    cv2.putText(frame, status, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)
    cv2.imshow("Tactical Feed - Intrusion Alarm (R to Reset, Q to Exit)", frame)

    # Keyboard logic
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break
    elif key == ord('r'):
        print("Re-calibrating baseline memory...")
        # Overwrite the old memory with what the camera sees right now
        baseline_frame = gray
        print("Perimeter re-secured.")

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

