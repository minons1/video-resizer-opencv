import cv2

cap = cv2.VideoCapture('demo.mp4')

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024*1)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768*1)

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("frame", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cap.release()

cv2.destroyAllWindows()