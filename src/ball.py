#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import cv
import sys

#import serial
 
class RobotVision:
    #size = None
    #cvImage hsv_frame, thresholded, thresholded2
    #cvScalar hsv_min, hsv_max, hsv_min2, hsv_max2
    #cvCapture capture;
 
    if __name__ == '__main__':
        
        #globals size,  hsv_frame, thresholded, thresholded2, hsv_min, hsv_max, hsv_min2, hsv_max2, capture
        print "Initializing ball Tracking"
        size = cv.Size(640, 480)
        hsv_frame = cv.CreateImage(size, cv.IPL_DEPTH_8U, 3)
        thresholded = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
        thresholded2 = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
 
        hsv_min = cv.Scalar(0, 50, 170, 0)
        hsv_max = cv.Scalar(10, 180, 256, 0)
        hsv_min2 = cv.Scalar(170, 50, 170, 0)
        hsv_max2 = cv.Scalar(256, 180, 256, 0)
 
        storage = cv.CreateMemStorage(0)
 
        # start capturing form webcam
        capture = cv.CreateCameraCapture(0)
 
        if not capture:
            print "Could not open webcam"
            sys.exit(1)
 
        #CV windows
        cv.NamedWindow( "Camera", cv.CV_WINDOW_AUTOSIZE );
 
        #globals size,  hsv_frame, thresholded, thresholded2, hsv_min, hsv_max, hsv_min2, hsv_max2, capture
        while True:
            # get a frame from the webcam
            frame = cv.QueryFrame(capture)
 
            if frame is not None: 
                # convert to HSV for color matching
                # as hue wraps around, we need to match it in 2 parts and OR together
                cv.CvtColor(frame, hsv_frame, cv.CV_BGR2HSV)
                cv.InRangeS(hsv_frame, hsv_min, hsv_max, thresholded)
                cv.InRangeS(hsv_frame, hsv_min2, hsv_max2, thresholded2)
                cv.Or(thresholded, thresholded2, thresholded)
 
                # pre-smoothing improves Hough detector
                cv.Smooth(thresholded, thresholded, cv.CV_GAUSSIAN, 9, 9)
                circles = cv.HoughCircles(thresholded, storage, cv.CV_HOUGH_GRADIENT, 2, thresholded.height/4, 100, 40, 20, 200)
 
                # find largest circle
                maxRadius = 0
                x = 0
                y = 0
                found = False
                for i in range(circles.total):
                    circle = circles[i]
                    if circle[2] > maxRadius:
                        found = True
                        maxRadius = circle[2]
                        x = circle[0]
                        y = circle[1]
 
                cv.ShowImage( "Camera", frame );
 
                if found:
                    print "ball detected at position:",x, ",", y, " with radius:", maxRadius
 
                else:
                    print "no ball"
                    
                    
                    