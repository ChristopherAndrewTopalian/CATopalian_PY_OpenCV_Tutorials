# capture_screenshot.py

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

print("Shutter open! Launching native video window...")
print("Press SPACEBAR to capture intel (save screenshot).")
print("Press the 'q' key or ESC to shut down safely.")

# We create a simple counter to name our files in order
capture_count = 0

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        time.sleep(0.1)
        continue

    # Convert to tactical grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Tactical Feed (SPACE to capture, Q to exit)", gray)

    # Check for keyboard inputs
    key = cv2.waitKey(1) & 0xFF

    # If 'q' (ASCII 113) or ESC (ASCII 27) is pressed -> Break loop
    if key == ord('q') or key == 27:
        break

    # If Spacebar (ASCII 32) is pressed -> Save the image to the hard drive
    elif key == 32:
        capture_count += 1
        
        # Format the file name dynamically (e.g., intel_capture_1.jpg)
        filename = f"intel_capture_{capture_count}.jpg"
        
        # cv2.imwrite saves the matrix data as a physical image file
        cv2.imwrite(filename, gray)
        print(f"[SUCCESS] Intel secured: {filename}")

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

