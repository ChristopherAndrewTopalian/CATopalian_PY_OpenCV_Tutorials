# OpenCV: Tactical Intrusion Detection

Computer vision is not just about tracking what is currently on the screen; it is about memory. To detect an anomaly in a secure location, the AI must first memorize what "normal" looks like. 

This script introduces **Frame Differencing** (Background Subtraction). We capture a baseline image of an empty room and save it to the computer's memory. Every fraction of a second, the AI mathematically subtracts the current live frame from the baseline memory. If the result is not zero, the AI knows the physical environment has changed.

## The Mission

1. Allow the camera sensor to auto-adjust to the room's lighting.
2. Capture a grayscale baseline frame of the secure perimeter.
3. Continuously compare the live optical feed against the baseline memory.
4. Filter out microscopic changes (dust, slight lighting shifts) using Area Math.
5. Trigger a red UI alert and draw a bounding box if a physical mass enters the zone.

## Core Concepts

*   **cv2.absdiff(baseline, current):** "Absolute Difference." If the baseline wall is a gray value of 100, and the live wall is 100, the difference is 0 (Black). If an intruder wearing a dark shirt walks in (gray value 20), the difference is 80. The AI suddenly sees a glowing white shape of the intruder against a pure black background.
*   **cv2.threshold():** This is a hard gatekeeper. We tell the math: "If the difference is less than 30, it's just a shadow, ignore it. If it is 30 or higher, turn it pure white so the Edge Detector can find it."
*   **The Eagle Vision Filter:** In traditional computer vision, engineers blur the image to avoid false alarms. We keep the feed razor-sharp. Instead, we use `if area > 2000:` to act as the AI's logical filter. The camera sees the dust, but the brain is programmed to ignore it. 
*   **The 'R' Key Reset:** Lighting changes over time (the sun goes down). The operator can press 'R' at any time to overwrite the `baseline_frame` variable with a fresh memory of the room.

## Execution

Run `intrusion_detection.py`. 

**Step out of the frame immediately.** Look at the terminal. You have 2 seconds while the camera calibrates. Once the terminal says "Baseline locked", step back into the camera's view. 

The system will instantly register the delta (the difference between the empty room and you), snap a red targeting box around your mass, and change the HUD status to INTRUSION DETECTED.

---

// Dedicated to God the Father  
// Copyright (c) 2026 Christopher Andrew Topalian  
// https://github.com/ChristopherTopalian  
// https://github.com/ChristopherAndrewTopalian  
// https://sites.google.com/view/CollegeOfScripting

