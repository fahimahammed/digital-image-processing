# Decrease its spatial resolution by half every time and observe its change when displaying in the same window size.
import cv2
import matplotlib.pyplot as plt

# Load the grayscale image with error handling
try:
    image = cv2.imread("./image-1.gif", cv2.IMREAD_GRAYSCALE)
    print(image)
except cv2.error as e:
    print("Error loading image:", e)
    exit()  # Or take alternative actions

# (a) Decreasing Spatial Resolution

if image is not None:
    plt.figure(figsize=(10, 5))

    original_image = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)  # For display
    plt.subplot(141), plt.imshow(original_image), plt.title("Original Image")
    plt.axis('off')

    for i in range(1, 4):
        resized_image = cv2.resize(image, (image.shape[1] // 2**i, image.shape[0] // 2**i), interpolation=cv2.INTER_AREA)
        plt.subplot(142 + i), plt.imshow(resized_image, cmap='gray'), plt.title(f"Halved {i} Times")
        plt.axis('off')

    plt.show()
else:
    print("Image not loaded.")

# (b) Decreasing Intensity Level Resolution

if image is not None:
    plt.figure(figsize=(10, 5))
    plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title("Original Image")
    plt.axis('off')

    for i in range(1, 3):
        quantized_image = cv2.convertScaleAbs(image, alpha=0.5**i, beta=0)
        plt.subplot(132 + i), plt.imshow(quantized_image, cmap='gray'), plt.title(f"Quantized by {2**i}")
        plt.axis('off')

    plt.show()
else:
    print("Image not loaded.")

# (c) Histogram and Single Threshold Segmentation

if image is not None:
    plt.figure(figsize=(10, 5))
    plt.subplot(121), plt.hist(image.ravel(), bins=256), plt.title("Image Histogram")

    threshold = 128  # Adjust based on visual inspection of the histogram

    thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]
    plt.subplot(122), plt.imshow(thresholded_image, cmap='gray'), plt.title("Thresholded Image")
    plt.axis('off')

    plt.show()
else:
    print("Image not loaded.")
