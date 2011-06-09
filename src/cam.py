'''
Created on 7 juin 2011

@author: Alex
'''
import cv

src = 0
image = 0
dest = 0
element_shape = cv.CV_SHAPE_RECT

def Opening(pos):
    element = cv.CreateStructuringElementEx(pos*2+1, pos*2+1, pos, pos, element_shape)
    cv.Erode(src, image, element, 1)
    cv.Dilate(image, dest, element, 1)
    cv.ShowImage("Opening & Closing", dest)
def Closing(pos):
    element = cv.CreateStructuringElementEx(pos*2+1, pos*2+1, pos, pos, element_shape)
    cv.Dilate(src, image, element, 1)
    cv.Erode(image, dest, element, 1)
    cv.ShowImage("Opening & Closing", dest)
def Erosion(pos):
    element = cv.CreateStructuringElementEx(pos*2+1, pos*2+1, pos, pos, element_shape)
    cv.Erode(src, dest, element, 1)
    cv.ShowImage("Erosion & Dilation", dest)
def Dilation(pos):
    element = cv.CreateStructuringElementEx(pos*2+1, pos*2+1, pos, pos, element_shape)
    cv.Dilate(src, dest, element, 1)
    cv.ShowImage("Erosion & Dilation", dest)

if __name__ == "__main__":
    
    capture = cv.CaptureFromCAM(0)
    cv.NamedWindow("Camera", 1)
    cv.NamedWindow("Mask", 1)
    cv.CreateTrackbar("Open", "Camera", 0, 10, Opening)
    cv.CreateTrackbar("Close", "Camera", 0, 10, Closing)
    
    src = cv.QueryFrame(capture)
    hsv_frame = cv.CreateImage(src.getSize(), cv.IPL_DEPTH_8U, 3)
    thresholded = cv.CreateImage(src.getSize(), cv.IPL_DEPTH_8U, 1)
    thresholded2 = cv.CreateImage(src.getSize(), cv.IPL_DEPTH_8U, 1)
        
    storage = cv.CreateMemStorage(0)
    
    while True:
        src = cv.QueryFrame(capture)
        #image = cv.CloneImage(src)
        #dest = cv.CloneImage(src)
        #hsv = cv.CloneImage(src)
        
        # convert to HSV for color matching
        cv.CvtColor(image, hsv, cv.CV_BGR2HSV)
        
        mask = cv.CreateImage(cv.GetSize(image), 8, 1);
        cv.InRangeS(hsv, cv.Scalar(0, 50, 170, 0), cv.Scalar(30, 255, 255, 0), mask);
        
        cv.ShowImage("Camera", hsv)
        cv.ShowImage("Mask", mask)
        
        if cv.WaitKey(10) == 27:
            break
        
    cv.DestroyWindow("camera")
