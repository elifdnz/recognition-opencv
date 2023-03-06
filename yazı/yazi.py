import cv2
import numpy as ny

ekran = ny.zeros((500,500,3),ny.uint8)*255

text = "Deneme"

color = (0,100,255)

for i in range(7):
    cv2.putText(ekran,text,(30,30+i*35),i,1,color)

cv2.imshow("Ekran",ekran)
cv2.waitKey(0)
cv2.destroyAllWindows()