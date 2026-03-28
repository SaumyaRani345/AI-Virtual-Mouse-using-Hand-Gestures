 AI Virtual Mouse using Hand Gestures
This project implements a virtual mouse system that allows users to control the computer cursor using hand gestures captured via a webcam. It uses Computer Vision and AI-based hand tracking to replace traditional mouse interaction.
________________________________________
 Features
•	 Real-time hand tracking
•	 Cursor movement using index finger
•	 Click action using pinch gesture (thumb + index finger)
•	 Smooth and responsive interaction
•	 Works with standard webcam
________________________________________
 Technology Used
•	Python 3.10
•	OpenCV – for image processing
•	MediaPipe – for hand landmark detection
•	PyAutoGUI – for controlling mouse actions
•	NumPy – for calculations
________________________________________
 How It Works
1.	The webcam captures live video.
2.	MediaPipe detects 21 hand landmarks.
3.	The index finger tip controls cursor movement.
4.	The distance between thumb and index finger is calculated:
o	Small distance → Mouse click
o	Large distance → Only movement
________________________________________
 Controls
Gesture	Action
 Index finger move	Move cursor
 Thumb + index close	 Left click
 No hand	No action
________________________________________
 Run the Project
python main.py
________________________________________
 Requirements
•	Webcam (built-in or external)
•	Good lighting conditions
•	Python 3.10 (recommended for MediaPipe compatibility)
________________________________________
 Limitations
•	Requires stable lighting
•	Performance may vary with camera quality
•	MediaPipe may not support newer Python versions (like 3.13)
________________________________________
 Future Improvements
•	Right-click and scrolling gestures
•	Gesture-based volume control
•	Multi-hand support
•	GUI interface
________________________________________
 Author
•	Saumya Rani
________________________________________

