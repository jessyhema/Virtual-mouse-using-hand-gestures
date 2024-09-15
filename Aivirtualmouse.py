import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize click variables
clicking = False
double_clicking = False
last_click_time = 0

# Initialize hand gesture variables
hand_gesture = None
last_hand_gesture = None

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)

    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates of the index finger tip (landmark 8)
            index_finger_tip = landmarks.landmark[8]
            h, w, c = image.shape
            x = int(index_finger_tip.x * w)
            y = int(index_finger_tip.y * h)

            # Map the finger tip position to the screen resolution
            x = np.clip(x * (screen_width / w), 0, screen_width)
            y = np.clip(y * (screen_height / h), 0, screen_height)

            # Move the mouse cursor
            pyautogui.moveTo(x, y)

            # Check for click
            if index_finger_tip.y < 0.5 and not clicking:
                clicking = True
                current_time = cv2.getTickCount()
                if current_time - last_click_time < 500:
                    double_clicking = True
                else:
                    double_clicking = False
                last_click_time = current_time
            elif index_finger_tip.y >= 0.5:
                clicking = False

            # Perform click action
            if clicking:
                if double_clicking:
                    pyautogui.click(x, y, button='left', clicks=2)
                else:
                    pyautogui.click(x, y, button='left')

            # Check for hand gestures
            thumb_tip = landmarks.landmark[4]
            pinky_tip = landmarks.landmark[20]
            if thumb_tip.y < 0.5 and pinky_tip.y < 0.5:
                hand_gesture = 'C'
            elif thumb_tip.y > 0.5 and pinky_tip.y > 0.5:
                hand_gesture = 'O'
            else:
                hand_gesture = None

            # Perform hand gesture actions
            if hand_gesture == 'C' and last_hand_gesture != 'C':
                # Close the current window
                pyautogui.moveTo(x, y)
                pyautogui.mouseDown()
                time.sleep(0.1)
                pyautogui.mouseUp()
                pyautogui.hotkey('alt', 'f4')
            elif hand_gesture == 'O' and last_hand_gesture != 'O':
                # Open a new window
                pyautogui.hotkey('ctrl', 'n')

            last_hand_gesture = hand_gesture

    # Display the image
    cv2.imshow('Virtual Mouse', image)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
