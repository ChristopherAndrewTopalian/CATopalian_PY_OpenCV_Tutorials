import cv2
import time

print("Bypassing Windows Media Foundation (Using DirectShow)...")

# The cv2.CAP_DSHOW flag forces OpenCV to talk directly to the hardware driver!
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Give the physical sensor 1 second to warm up its shutter
time.sleep(1)

print("Checking sensor connection...")

if not cap.isOpened():
    print("WARNING: Index 0 failed. Attempting Camera Index 1...")
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Could not connect to camera.")
    print("Check if another app (Zoom, Browser) is using the webcam.")
    print("Check Windows Settings -> Privacy -> Camera -> Allow desktop apps access.")
    exit()

print("Shutter open! Launching native video window...")
print("Press the 'q' key or ESC inside the video window to shut down safely.")

while True:
    ret, frame = cap.read()

    # If the camera drops a frame, don't crash, just warn and continue
    if not ret or frame is None:
        print("Dropped frame from sensor...")
        time.sleep(0.1)
        continue

    # Display instantly in a native operating system window
    cv2.imshow("Tactical Feed - DirectShow (Press Q to exit)", frame)

    # Check every 1ms if the user pressed 'q' (ASCII 113) or ESC (ASCII 27)
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

import cv2
import time

print("Bypassing Windows Media Foundation (Using DirectShow)...")

# The cv2.CAP_DSHOW flag forces OpenCV to talk directly to the hardware driver
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Give the physical sensor 1 second to warm up its shutter
time.sleep(1)

print("Checking sensor connection...")

if not cap.isOpened():
    print("WARNING: Index 0 failed. Attempting Camera Index 1...")
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Could not connect to camera.")
    print("Check if another app (Zoom, Browser) is using the webcam.")
    print("Check Windows Settings -> Privacy -> Camera -> Allow desktop apps access.")
    exit()

print("Shutter open! Launching native video window...")
print("Press the 'q' key or ESC inside the video window to shut down safely.")

while True:
    ret, frame = cap.read()

    # If the camera drops a frame, don't crash, just warn and continue
    if not ret or frame is None:
        print("Dropped frame from sensor...")
        time.sleep(0.1)
        continue

    # Convert RGB to Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display instantly in a native operating system window
    cv2.imshow("Tactical Feed - DirectShow (Press Q to exit)", gray)

    # Check every 1ms if the user pressed 'q' (ASCII 113) or ESC (ASCII 27)
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

