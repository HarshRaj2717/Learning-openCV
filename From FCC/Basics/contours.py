import cv2 as cv
import numpy as np

img_location = input("Enter image location : ")
img = cv.imread(img_location)
cv.imshow('image', img)
cv.waitKey(0)

blank_img = np.zeros(img.shape)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
cv.waitKey(0)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank_img, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank_img)
cv.waitKey(0)
