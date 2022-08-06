import cv2

capture=cv2.videoCapture("http://192.168.82.15:8080/video")

while(True):
    _, frame = capture.read()
    cv2.imshow('livestream', frame)

    if cv2.waitkey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()