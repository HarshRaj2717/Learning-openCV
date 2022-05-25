import cv2 as cv
import numpy as np


def img_gray(img_source):
    img = cv.imread(img_source)
    #########################################
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #########################################
    cv.imshow("output", img)
    cv.waitKey(0)


def img_blur(img_source):
    img = cv.imread(img_source)
    #####################################
    img = cv.GaussianBlur(img, (7, 7), 5)  # The third value (sigma) defines BLUR INTENSITY.
    #####################################
    cv.imshow("output", img)
    cv.waitKey(0)


def img_canny_and_dilate_erode(img_source):
    img = cv.imread(img_source)
    #############################
    # Canny : Used to detect edges.
    img = cv.Canny(img, 150, 200)
    # 100, 100 are threshold values 1 and 2 ... these can be used to change how many edges are needed.
    #############################
    cv.imshow("output_canny", img)
    cv.waitKey(0)
    ########################################
    # Dilation : Used to thicken the edges detected by canny.
    kernel = np.ones((5, 5), np.uint8)
    img = cv.dilate(img, kernel, iterations=1)  # Kernel is a matrix and iterations defines the thickness.
    ##########################################
    cv.imshow("output_dilate", img)
    cv.waitKey(0)
    ##########################################
    # Erosion : Reverse of dilation.
    kernel = np.ones((5, 5), np.uint8)
    img = cv.erode(img, kernel, iterations=1)
    #########################################
    cv.imshow("output_eroded", img)
    cv.waitKey(0)


# img_gray("Resources/Photos/cat.jpg")
img_blur("Resources/Photos/cat.jpg")
# img_canny_and_dilate_erode("Resources/Photos/cat.jpg")
