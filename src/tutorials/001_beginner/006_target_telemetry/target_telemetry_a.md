# OpenCV: Tactical Target Telemetry

Drawing a box around a target is helpful for a human operator, but a machine cannot "see" a green square. If we want a robotic system to autonomously react to a target, the "brain" must extract the raw mathematical coordinates and translate them into a language the motors can understand.

This script demonstrates how to extract the telemetry (the X and Y spatial coordinates) of a target and render a real-time Heads-Up Display (HUD).

## The Mission

1. Localize the target using Edge Detection and Bounding Boxes.
2. Use basic algebra to calculate the exact center point (Center of Mass) of the object.
3. Overlay a tactical targeting crosshair on the center point.
4. Extract the coordinate data and print it directly onto the optical feed.

## Core Concepts

*   **The Coordinate Grid:** In computer vision, the top-left corner of the screen is `X: 0, Y: 0`. As an object moves right, `X` increases. As an object moves down, `Y` increases.
*   **Center of Mass Math:** The `cv2.boundingRect()` function gives us the top-left corner (`x`, `y`), plus the width (`w`) and height (`h`). To find the absolute center of the target, we use simple math:
    *   `center_x = x + (w // 2)`
    *   `center_y = y + (h // 2)`
    *(Note: We use `//` for integer division, because there are no "half pixels" on a screen).*
*   **cv2.putText():** This function allows us to draw dynamic text data directly onto the video frame.

## The "True AI" Takeaway

This is the bridge between Vision and Action. By extracting `center_x` and `center_y`, the Python program now possesses numerical data it can transmit to the physical world. 

If `center_x` is on the far left side of the screen, the program can send a command to a servo motor telling it to turn the camera to the left until the target is perfectly centered at `X: 320`. You have just built the foundational logic for an autonomous tracking turret.

---

// Dedicated to God the Father  
// Copyright (c) 2026 Christopher Andrew Topalian  
// https://github.com/ChristopherTopalian  
// https://github.com/ChristopherAndrewTopalian  
// https://sites.google.com/view/CollegeOfScripting

