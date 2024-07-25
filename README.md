# virtual-steering
Making a bot which uses a webcam facing the user and moves the bot right or left depending on the motion of the steering . 
This task is developed using OpenCV-Python and Arduino IDE (Python Version- 3.6.9 OpenCV Version-4.5.1 Arduino IDE Version-1.8.13).The first part developed in Python captures video of  steering wheel rotating in front of webcam of the laptop. The code is written to track the direction of movement of steering wheel. It comprises of- 
<br>1)Frame extraction from the video. 
<br>2)Color based image segmentation to detect the steering wheel.
<br>3)Finding the contour with maximum area.
<br>4)Comparison between plotted points in the consecutive frames to decide the direction of movement of the steering wheel.
<br>5)Plotting the mean position of all pixels in the contour with maximum area.
<br><br>The second part of the task is developed using Arduino IDE in order to control movement of bot depending on direction of steering. To enable serial communication between Python and Arduino pySerial library in python is used. Arduino IDE is used to communicate with Arduino UNO and control the ON/OFF of motors connected to the left and right whhels of the bot.
When the motor connected to left wheel is OFF and motor connected to right wheel is ON bot turns in right direction and vice-versa.
<br> When user inputs 'B' key brakes are applied and both motors are turned OFF through Arduino IDE.
<br><br>The second part of the task is developed using Arduino IDE in order to control movement of bot depending on direction of steering. To enable serial communication between Python and Arduino pySerial library in python is used. Arduino IDE is used to communicate with Arduino UNO and control the ON/OFF of motors connected to the left and right wheels of the bot.
When the motor connected to the left wheel is OFF and the motor connected to the right wheel is ON, bot turns towards right direction and vice-versa.
<br> When user inputs 'B' key,the brakes are applied and both the motors are turned OFF through Arduino IDE.
