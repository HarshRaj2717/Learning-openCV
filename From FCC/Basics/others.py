from configparser import Interpolation
import cv2 as cv

# Reading an image
img_location = input("Enter image location : ")
img = cv.imread(img_location)
cv.imshow('image', img)
cv.waitKey(0)

# Grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray_img)
cv.waitKey(0)

# Blur 
blur_img = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur_img)
cv.waitKey(0)

# Canny
canny_img = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny_img)
cv.waitKey(0)

# Dilating the image
dilated_img = cv.dilate(canny_img, (7,7), iterations=3)
cv.imshow('Dilated', dilated_img)
cv.waitKey(0)

# Eroding
eroded_img = cv.erode(dilated_img, (7,7), iterations=3)
cv.imshow('Eroded', eroded_img)
cv.waitKey(0)

# Resize

# interpolation = cv.INTER_AREA for shrinking image
# interpolation = cv.INTER_LINEAR for expanding image
# interpolation = cv.INTER_CUBIC for expanding image ... this is slowest but gives best quality

resized_img = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized_img)
cv.waitKey(0)

# Cropping
cropped_img = img[50:200, 200:400]
cv.imshow('Cropped', cropped_img)
cv.waitKey(0)
