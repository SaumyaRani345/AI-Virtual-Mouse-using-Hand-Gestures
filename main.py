import cv2
import mediapipe as mp
import pyautogui
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            landmarks = hand.landmark

            x = int(landmarks[8].x * frame.shape[1])
            y = int(landmarks[8].y * frame.shape[0])

            screen_x = int(screen_w * landmarks[8].x)
            screen_y = int(screen_h * landmarks[8].y)

            pyautogui.moveTo(screen_x, screen_y)

            thumb_x = int(landmarks[4].x * frame.shape[1])
            thumb_y = int(landmarks[4].y * frame.shape[0])

            distance = np.hypot(x - thumb_x, y - thumb_y)

            if distance < 30:
                pyautogui.click()
                pyautogui.sleep(0.2)

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
