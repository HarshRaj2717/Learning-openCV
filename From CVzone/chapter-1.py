import cv2 as cv


def read_img(img_source):
    img = cv.imread(img_source)
    cv.imshow("Output", img)
    cv.waitKey(0)


def read_vid(vid_source):
    vid = cv.VideoCapture(vid_source)
    vid.set(3, 1000)
    vid.set(4, 1000)
    is_on, img = vid.read()
    while is_on:
        cv.imshow("Output", img)
        is_on, img = vid.read()
        if cv.waitKey(1) and 0xFF == ord("k"):
            break


def read_webcam():
    read_vid(0)


if __name__ == "__main__":
    # read_img("Resources/Photos/cat.jpg")
    # read_vid("Resources/Videos/dog.mp4")
    read_webcam()
