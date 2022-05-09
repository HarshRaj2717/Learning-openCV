import cv2 as cv


def resize_frame(frame, scale):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions)

def image_read():
    img_location = input("Enter image location : ")
    img = cv.imread(img_location)

    scale = float(input("Enter scale : "))
    resized_img = resize_frame(img, scale)

    cv.imshow("image", resized_img)
    cv.waitKey(0)


def video_read():
    vid_location = input("Enter video location : ")
    vid = cv.VideoCapture(vid_location)
    scale = float(input("Enter scale : "))

    # not needed just showing what imread does...
    # print(vid)

    isTrue = True
    isTrue, frame = vid.read()
    while isTrue:
        resized_frame = resize_frame(frame, scale)
        cv.imshow("video", resized_frame)

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