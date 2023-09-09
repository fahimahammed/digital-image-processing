import os
import cv2

def blurImage(imagePath, outputFolder):
    image = cv2.imread(imagePath, cv2.IMREAD_COLOR)
    if image is None:
        print(f"Unable to read the image: {imagePath}")
        return

    kernelSize = (51, 51)
    blurredImage = cv2.GaussianBlur(image, kernelSize, 0)
    filename, ext = os.path.splitext(os.path.basename(imagePath))
    os.makedirs(outputFolder, exist_ok=True)
    outputPath = os.path.join(outputFolder, filename + "-blur.jpg")
    cv2.imwrite(outputPath, blurredImage)
    
    print(f"Blur image saved as {outputPath}")

imageDir = "photos"
outDir = "output"

imagePaths = [
    os.path.join(imageDir, filename) 
    for filename in os.listdir(imageDir) 
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
]

for imagePath in imagePaths:
    blurImage(imagePath, outDir)
