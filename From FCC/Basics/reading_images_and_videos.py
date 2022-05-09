import cv2 as cv


def image_read():
    img_location = input("Enter image location : ")
    img = cv.imread(img_location)

    # not needed just showing what imread does...
    # print(img_matrix)

    cv.imshow("image", img)

    cv.waitKey(0)


def video_read():
    vid_location = input("Enter video location : ")
    vid = cv.VideoCapture(vid_location)

    # not needed just showing what imread does...
    # print(vid)

    isTrue = True
    isTrue, frame = vid.read()
    while isTrue:
        cv.imshow("video", frame)

        if cv.waitKey(20) and 0xFF == ord("q"):
            break

        isTrue, frame = vid.read()

    vid.release()
    cv.destroyAllWindows()


def main():
    ask = input("Want to read an image/video ? :")

    if ask.lower() == "image":
        image_read()

    elif ask.lower() == "video":
        video_read()

    else:
        print("Invalid Input.")


main()