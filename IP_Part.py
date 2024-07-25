# PROBLEM STATEMENT: ( in Opencv Python)
# Making a bot which uses a webcam facing the user and moves the bot right or left depending on the motion of the steering .
import cv2
import numpy as np 
import math
import statistics as stat
import serial
ard=serial.Serial('com3',9600)

listi=[]
listj=[]
t=0
t1=2
t2=2
msg='Press Q to quit.Press C to clear screen.'
msg2='Press B to apply brakes. Press A to continue.'

cap=cv2.VideoCapture(0)
# Get the video from Webcam
if cap.isOpened()==False:
# Check whether the video has been detected
# without any error
    print('error opening camera')
cv2.namedWindow('whiteboard',cv2.WINDOW_NORMAL)
cv2.namedWindow('original',cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        l=[]
#    Segmentation
        frame2=cv2.inRange(frame,(0,100,0),(100,255,100))
        frame3=np.full((frame2.shape[0],frame2.shape[1]),255,dtype='uint8')
# to initialise frame4 only once
        if t==0:
             frame4=np.copy(frame3)
             t=t+1
        contour,hierarchy=cv2.findContours(frame2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(contour)):
            area=cv2.contourArea(contour[i])
            l.append(int(area)) 
        #print(l)
# get the contour with max area
        if np.array(l).size>0:
         a=max(l)
         ind=0
# find the index
         for i in range(len(l)):
            if l[i]==a:
                ind=i
         cv2.drawContours(frame3,contour,ind,0,thickness=-1)
# get the max area contour drawn
         pts=np.where(frame3==0)
# take mean of all points which are black
         meani=stat.mean(pts[1])
         meanj=stat.mean(pts[0])
# store the points in the list
         listi.append(meani)
         listj.append(meanj)
        if(len(listi)>=2):
         l3=len(listi)-2
         l4=len(listj)-2
# track the ball movement by drawing lines
         frame4=cv2.line(frame4,(frame4.shape[0]-listi[l3],listj[l4]),(frame4.shape[0]-listi[l3+1],listj[l4+1]),0,thickness=10,lineType=-1)
         if len(listi)>10:
                 if listi[len(listi)-1]>listi[len(listi)-11]+30:
                         if t1==1 or t1==2:
                             frame4=np.full((frame3.shape[0],frame3.shape[1]),255,dtype='uint8')
                             ard.write(str.encode('1'))
                         print('turned left')
                         t1=0
                 if listi[len(listi)-1]<listi[len(listi)-11]-30:
                         if t1==0 or t1==2:
                             frame4=np.full((frame3.shape[0],frame3.shape[1]),255,dtype='uint8')
                             ard.write(str.encode('2'))
                         print('turned right')
                         t1=1
                 #if abs(listi[len(listi)-1]-listi[len(listi)-11])<30:
                         #ard.write(str.encode('0'))
        cv2.imshow('original',cv2.flip(frame,1))
        img=np.copy(frame4)
        img=cv2.putText(img,msg,(0,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
        img=cv2.putText(img,msg2,(0,48),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
        cv2.imshow('whiteboard',img)

        p=cv2.waitKey(1)
# exit
        if p== ord('q')or p == ord('Q') :
         ard.write(str.encode('0'))
         break
# clearscreen
        if p== ord('c') or p == ord('C'):
         frame4=np.full((frame3.shape[0],frame3.shape[1]),255,dtype='uint8')
         listi=[]
         listj=[]
         l=[]
# brake
        if p== ord('b') or p == ord('B'):
            t2=0
            while(1):
                print('brakes applied')
                if(t2==0):
                  ard.write(str.encode('0')) # Halt
                  t2=t2+1
                p=cv2.waitKey(1)
                if(p==ord('a') or p==ord('A')):
                    print('brakes released')
                    break
        cv2.imshow('whiteboard',frame4)
    else:
        break
ard.write(str.encode('3'))  # Stop the operation
cap.release()
cv2.destroyAllWindows
