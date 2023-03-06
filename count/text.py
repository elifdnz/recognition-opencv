import cv2
import numpy as np

vide = cv2.VideoCapture("video.mp4")
backs = cv2.createBackgroundSubtractorMOG2()
c = 0

while True:
    ret,frame = vide.read()
    if ret:
        gmask = backs.apply(frame)
        cv2.line(frame,(30,0),(30,200),(0,255,0),2)
        cv2.line(frame,(50,0),(50,200),(0,255,0),2)

        contors , hiyeras = cv2.findContours(gmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try : hiyeras = hiyeras[0]
        except : hiyeras = []

        for cont,hier in zip(contors,hiyeras):
            (x,y,w,h) = cv2.boundingRect(cont)
            if w>30 and h>30 :
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                if x>30 and x<50:
                    c+=1


        cv2.putText(frame,"car:"+str(c),(90,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2,cv2.LINE_AA)
        cv2.imshow("car",frame)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

vide.release()
cv2.destroyAllWindows()
