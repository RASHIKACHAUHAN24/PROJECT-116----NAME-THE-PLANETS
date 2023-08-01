import cv2

img = cv2.imread("solar-system.jpg")

sun="SUN"
cv2.putText(img,"sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))

mercury="MERCURY"
cv2.putText(img,"mercury",(120,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))

venus="VENUS"
cv2.putText(img,"venus",(190,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))

earth="EARTH"
cv2.putText(img,"earth",(280,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))

mars="MARS"
cv2.putText(img,"mars",(380,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))

jupiter="JUPITER"
cv2.putText(img,"jupiter",(580,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))
saturn="SATURN"
cv2.putText(img,"saturn",(750,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))

neptune="NEPTUNE"
cv2.putText(img,"neptune",(960,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))

uranus="URANUS"
cv2.putText(img,"uranus",(1110,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))
cv2.imshow("output",img)
print(img)
cv2.waitKey(0)