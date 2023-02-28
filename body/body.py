import cv2

img = cv2.imread("body.jpg")

body_cascade = cv2.CascadeClassifier("fullbody.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

body = body_cascade.detectMultiScale(gray,1.3,4)

for (x,y,w,h) in body:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow("body",img)
cv2.waitKey(0)
cv2.destroyAllWindows()