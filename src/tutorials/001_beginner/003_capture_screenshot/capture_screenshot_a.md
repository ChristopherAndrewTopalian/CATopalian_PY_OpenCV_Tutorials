# OpenCV: Tactical Intel Capture

Streaming an optical feed is only the first step. To train targeting models, identify structural weaknesses, or log perimeter breaches, an operator must be able to capture and save critical data frames directly to local storage.

This script introduces physical data extraction. By mapping a keyboard input to the OpenCV image writer, we can instantly freeze a moment in time and save it as a high-efficiency JPG.

## The Mission

1. Establish the optimized grayscale optical feed.
2. Monitor the keyboard for a specific trigger (The Spacebar).
3. Upon trigger, generate a sequential filename.
4. Write the current visual matrix (the frame) directly to the hard drive.

## Core Concepts

*   **ASCII Key Mapping (32):** Every key on your keyboard has a numeric code. The Spacebar is ASCII 32. By adding `elif key == 32:`, we create a secondary trigger alongside our shutdown sequence.
*   **Dynamic Variables (f-strings):** We use a simple counter (`capture_count`) and inject it directly into the file name using a Python f-string: `f"intel_capture_{capture_count}.jpg"`. This prevents our screenshots from overwriting each other.
*   **cv2.imwrite(filename, image_data):** The powerhouse function of this tutorial. It takes the matrix of numbers we call an image and permanently encodes it onto your hard drive as a standard image file.

## Execution

In our project folder that has this script: We type **cmd** in the address bar and press **Enter**  

This opens the **Command Prompt** of this folder.

In Command Prompt we type:   
**python capture_screenshot.py**  
and press **Enter**

---

## The Reason
We open and run our script using the **cmd** method, because we want the screenshots to be placed in our project folder.

---

Once the grayscale feed is live, press the **SPACEBAR**. Check your terminal, you will see a confirmation message. 

Look inside the folder where your script is located. You will see `intel_capture_1.jpg` sitting right next to your code. Every time you press the Spacebar, a new sequential file is secured.

---

// Dedicated to God the Father  
// Copyright (c) 2026 Christopher Andrew Topalian  
// https://github.com/ChristopherTopalian  
// https://github.com/ChristopherAndrewTopalian  
// https://sites.google.com/view/CollegeOfScripting

