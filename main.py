from black import NothingChanged
import cv2
from cv2 import GaussianBlur
from cv2 import namedWindow
from numpy import empty


cap = cv2.VideoCapture(0)

namedWindow("checkbar")

cv2.createTrackbar("height","checkbar",0,100,empty)
cv2.createTrackbar("width","checkbar",0,100,empty)
cv2.createTrackbar("sigmaX","checkbar",0,100,empty)
cv2.createTrackbar("sigmaY","checkbar",0,100,empty)

while(True):
    ret, frame = cap.read()

    height_value = cv2.getTrackbarPos("height","checkbar")
    width_value = cv2.getTrackbarPos("width","checkbar")
    sigmaX_value = cv2.getTrackbarPos("sigmaX","checkbar")
    sigmaY_value = cv2.getTrackbarPos("sigmaY","checkbar")
  
    k_width = width_value *2 + 1
    k_height = height_value *2 + 1

    frame2 = cv2.GaussianBlur(frame,(k_width,k_height),sigmaX_value,sigmaY_value)

    modified = cv2.addWeighted(frame, 1.5, frame2, -0.5, 0) 

    cv2.namedWindow("origin",0)
    cv2.namedWindow("blurred",0)
    cv2.namedWindow("sharpen",0)
    cv2.resizeWindow("origin",640,360)
    cv2.resizeWindow("blurred",640,360)
    cv2.resizeWindow("sharpen",640,360)     

    cv2.imshow("origin",frame)
    cv2.imshow("blurred",frame2)
    #cv2.imshow('modified', frame2)
    cv2.imshow('sharpen', modified)
    
    
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()