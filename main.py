import cv2   
img = cv2.imread("face.png")
cascade = cv2.CascadeClassifier("frontalface.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = cascade.detectMultiScale(gray, 1.3, 7)
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow('face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()