import cv2
# Görüntüyü okuma
import numpy as np

image = cv2.imread('red-mug.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

mask = cv2.inRange(hsv_image,lower_red,upper_red)

red_image = cv2.bitwise_and(image,image,mask=mask)

cv2.imshow('Image',image)
cv2.imshow("Mask",mask)
cv2.imshow("RED_IMAGE",red_image)

cv2.waitKey(0)
cv2.destroyAllWindows()




