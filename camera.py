import cv2

def take_picture():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        exit()

    ret, frame = cap.read()

    if ret:
        cv2.imwrite("image.jpg", frame)

    cap.release()
    cv2.destroyAllWindows()
