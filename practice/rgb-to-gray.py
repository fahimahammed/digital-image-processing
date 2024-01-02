import os
import cv2

def rgbToGray(imagePath, outputFolder):
    image = cv2.imread(imagePath, cv2.IMREAD_COLOR)
    if image is None:
        print(f"Unable to read the image: {imagePath}")
        return
        
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print(f"image: {image} and {grayImage}")
    filename, ext = os.path.splitext(os.path.basename(imagePath))
    # print(f"filename: {filename}, ext: {ext}")
    os.makedirs(outputFolder, exist_ok=True)
    outputPath = os.path.join(outputFolder, filename + "-gray.jpg")
    cv2.imwrite(outputPath, grayImage)
    
    print(f"Grayscale image saved as {outputPath}")

imageDir = "photos"
outDir = "output"

imagePaths = [
    os.path.join(imageDir, filename) 
    for filename in os.listdir(imageDir) 
    if filename.lower().endswith((".jpg", ".jpeg", ".png", "webp"))
]

#print(f"image paths: ", imagePaths)

for imagePath in imagePaths[:9]:
    rgbToGray(imagePath, outDir)
