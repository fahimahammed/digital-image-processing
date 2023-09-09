import cv2
import numpy as np 

image = cv2.imread("photos/photo-5.webp")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape)
print(grayImage.shape)

cv2.imshow("Window", grayImage)
cv2.waitKey(0)