
import cv2
import matplotlib
import numpy
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
cam = cv2.VideoCapture(0)
import os
while(True):
    ret, frame = cam.read()
    cv2.imshow('Slient Recorder', frame)
    out.write(frame)
    recording = input("Are you satfisied with the recording? This will close out of the program Y/N")
    if(recording == "Y"):
        break
