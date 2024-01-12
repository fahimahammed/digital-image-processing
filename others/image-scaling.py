import cv2

# Load the image
image = cv2.imread("photos/photo-1.jpeg")

# Specify the newWidth and newHeight
newWidth = 400
newHeight = 300

# Resize the image
scaledImage = cv2.resize(image, (newWidth, newHeight))

# Display the original and scaled images
cv2.imshow("Original Image", image)
cv2.imshow("Scaled Image", scaledImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
