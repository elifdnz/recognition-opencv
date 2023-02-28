import cv2   
vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("frontalface.xml")
eye_cascade = cv2.CascadeClassifier("eye.xml")

while 1:
    ret, frame = vid.read()
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(480,360))
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        rgray = gray[y:y+h, x:x+w]
        rframe = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(rgray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(rframe,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    cv2.imshow('eye',frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
