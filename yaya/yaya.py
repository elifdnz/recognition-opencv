import cv2
import imutils as im

resim = cv2.imread("yaya.jpeg")

resim = im.resize(resim,300)

hogd = cv2.HOGDescriptor()
hogd.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cor , _ = hogd.detectMultiScale(resim, winStride = (4,4),padding = (8,8),scale = 1.02)

for (x,y,w,h) in cor:
    cv2.rectangle(resim,(x,y),(x+w,y+h),(0,0,255),5)

cv2.imshow("İmage",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()