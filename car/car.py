import cv2

img = cv2.imread("car.jpg")
car_cascade = cv2.CascadeClassifier("car.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

car = car_cascade.detectMultiScale(gray,1.1,1)

for (x,y,w,h) in car:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("car",img)
cv2.waitKey(0)
cv2.destroyAllWindows()