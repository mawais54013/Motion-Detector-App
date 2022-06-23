import cv2, time

video=cv2.VideoCapture(1)
# Might need to change above to 0 if you don't have obs installed

a=0

while True:
    a=a+1
    check, frame = video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing",gray)

    key=cv2.waitKey(1)
    print(gray)

    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows