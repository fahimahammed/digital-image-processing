import cv2
import numpy as np 

image = cv2.imread("photos/photo-5.webp")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# image[:, :, 0]=0 // blue = 0

print(image.shape)
print(grayImage.shape)

cv2.imshow("Window", grayImage)
cv2.waitKey(0)