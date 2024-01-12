import cv2
import matplotlib.pyplot as plt

# Load the grayscale image with error handling
try:
    image = cv2.imread("photos/photo-5.webp", 0)
    print("Image loaded: ", image)
except cv2.error as e:
    print("Error loading image:", e)
    exit()  # Or take alternative actions



