import cv2

# Load the image
image = cv2.imread("photos/photo-5.webp")

# Specify the desired width and height
width = 800
height = 600

# Resize the image
resizedImage = cv2.resize(image, (width, height))

# image flip
# Flip the image horizontally (0) or vertically (1)
# flippedHorizontal = cv2.flip(image, 0)  # Horizontal flip
# flippedVertical = cv2.flip(image, 1)    # Vertical flip
imgFlip = cv2.flip(resizedImage, 0)

# Display the resized image
cv2.imshow("Resized Image", imgFlip)
cv2.waitKey(0)
cv2.destroyAllWindows()
