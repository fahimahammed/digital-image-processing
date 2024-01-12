import cv2
import numpy as np 

image = cv2.imread("photos/photo-1.jpeg")

# Split the image into its color channels
imgBlue = image[:, :, 0]
imgGreen = image[:, :, 1]
imgRed = image[:, :, 2]

# Horizontally stack the color channels to create a new image
newImage = np.hstack((imgBlue, imgGreen, imgRed))

# Print the shape of the original image and new image
print("Original Image Shape:", image.shape)
print("New Image Shape:", newImage.shape)

# Display the new image
cv2.imshow("Window", newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
