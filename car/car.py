import cv2

#img = cv2.imread("car.jpg")
vid = cv2.VideoCapture("car.mp4")
car_cascade = cv2.CascadeClassifier("car.xml")

while 1:
    ret, frame = vid.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    car = car_cascade.detectMultiScale(gray,1.2,3)

    for (x,y,w,h) in car:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow("video",frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()