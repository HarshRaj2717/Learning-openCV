import cv2 as cv
import numpy as np

img = np.zeros((500,500, 3))
cv.imshow("image", img)
cv.waitKey(0)

# 1. Paint the image a certain colour
img[200:300, 300:400] = 0,255,0
cv.imshow('Green', img)
cv.waitKey(0)

# 2. Draw a Rectangle
cv.rectangle(img, (0,0), (img.shape[1]//2, img.shape[0]//2), (0,0, 255), thickness=-1)
cv.imshow('Rectangle', img)
cv.waitKey(0)

# 3. Draw A circle
cv.circle(img, (img.shape[1]//2, img.shape[0]//2), 40, (255,0,0), thickness=-1)
cv.imshow('Circle', img)
cv.waitKey(0)

# 4. Draw a line
cv.line(img, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', img)
cv.waitKey(0)

# 5. Write text
cv.putText(img, 'Hello World!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', img)
cv.waitKey(0)
