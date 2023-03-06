import cv2
import imutils as im

# resim = cv2.imread("yaya.jpeg")

# resim = im.resize(resim,300)

vid = cv2.VideoCapture("yayalar.mp4")

while True:
    ret, frame = vid.read()
    if ret == False:
        break
    frame = im.resize(frame,500)
    hogd = cv2.HOGDescriptor()
    hogd.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    cor , _ = hogd.detectMultiScale(frame, winStride = (4,4),padding = (2,2),scale = 1.5)
    for (x,y,w,h) in cor:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)

    cv2.imshow("İmage",frame)
    if cv2.waitKey(5) & 0xFF ==ord('q'):
        break


vid.release()
cv2.destroyAllWindows()