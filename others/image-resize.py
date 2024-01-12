import cv2

# Load the image
image = cv2.imread("photos/photo-5.webp")

# Specify the desired width and height
width = 800
height = 600

# Resize the image
resizedImage = cv2.resize(image, (width, height))

# Display the resized image
cv2.imshow("Resized Image", resizedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
