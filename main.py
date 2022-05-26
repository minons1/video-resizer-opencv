import cv2

cap = cv2.VideoCapture('./vid/demo.mp4') #Video input name
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))

FRAME_WIDTH = 1024
FRAME_HEIGHT= 768

out = cv2.VideoWriter('./vid/demo_1024.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 10, (FRAME_WIDTH,FRAME_HEIGHT)) # Video Output name, codec, fps, res(width,height)

while(True):
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.resize(frame,(FRAME_WIDTH, FRAME_HEIGHT), interpolation = cv2.INTER_CUBIC)

        out.write(frame)
        cv2.imshow("frame", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

out.release()
cap.release()

cv2.destroyAllWindows()