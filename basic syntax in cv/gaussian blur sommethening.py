import cv2

# Read the image
img = cv2.imread('new.jpg')

# Apply Gaussian blur with kernel size (41, 41) and sigmaX 50
gaussianimg = cv2.GaussianBlur(img, (41, 41), 50)

# Apply Gaussian blur with kernel size (21, 21) and sigmaX 0
gaussianimg1 = cv2.GaussianBlur(img, (21, 21), 0)

# Display the original image
cv2.imshow("original", img)

# Display the first Gaussian blurred image
cv2.imshow("gaussianblur", gaussianimg)

# Display the second Gaussian blurred image
cv2.imshow("gaussianblur1", gaussianimg1)

# Wait for a key press indefinitely
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()
