import cv2

# initialize the camera
cap = cv2.VideoCapture(0)

# check if camera is available
if not cap.isOpened():
    print("Unable to access camera")
    exit()

# read a frame from the camera
ret, frame = cap.read()

# if frame is read correctly, save it to a file
if ret:
    cv2.imwrite("image.jpg", frame)

# release the camera and close the window
cap.release()
cv2.destroyAllWindows()
