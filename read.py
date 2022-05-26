import cv2

cap = cv2.VideoCapture('demo_1024.mp4')
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(True):
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow("frame", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()