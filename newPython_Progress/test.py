import cv2
cap = cv2.VideoCapture(0)

img = cv2.imread('C:/Users/Nana Wartana/OneDrive/Gambar/DSCF9252.JPG')

while True:
    ret, frame = cap.read()
    # cv2.imshow("Image", frame)
    cv2.imshow("Image", cv2.resize(img,(500,500)))

    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()