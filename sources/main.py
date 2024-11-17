import cv2


def get_shape(frame):
    width = int(frame.shape[1])
    height = int(frame.shape[0])
    return (width, height)


def resize_frame(frame, scale=1, width=None, height=None):
    if width and height:
        width = width * scale
        height = height * scale
    else:
        width = frame.shape[1] * scale
        height = frame.shape[0] * scale
    frame = cv2.resize(frame, (width, height))
    return frame


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = resize_frame(frame, 1)
    print(get_shape(frame))
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1) & 0XFF
    if key == ord('n'):
        break
cap.release()
cv2.destroyAllWindows()
