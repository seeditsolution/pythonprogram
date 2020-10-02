
import cv2

cap = cv2.VideoCapture(0)

img = 0

while True:
    ret, frame = cap.read()
    cv2.imshow("Image", frame)
    k = cv2.waitKey(1)
    if k == 27:
        # ESC pressed
        print("Closing the window...")
        break
    elif k == 32:
        # Press SPACE to click picture
        img_name = "opencv_frame.jpg".format(img)
        cv2.imwrite(img_name, frame)
        print(format(img_name))
        img += 1

cap.release()

cv2.destroyAllWindows()
