import cv2   
#img = cv2.imread("face.png")
#vid = cv2.VideoCapture("faces.mp4")
vid = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("frontalface.xml")

while 1:
    a, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(gray, 1.3, 7)
    
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.imshow('face',frame)
    if cv2.waitKey(5) & 0xFF == 'q':
        break


vid.release()
cv2.destroyAllWindows()