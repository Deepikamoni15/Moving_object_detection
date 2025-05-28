import cv2

# Read the image
img = cv2.imread('new.jpg')

if img is None:
    print("Error: Could not read the image.")
else:
    # Convert the image to grayscale
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresholdimg = cv2.threshold(grayimg, 180, 255, cv2.THRESH_BINARY)

    # Display the original image
    cv2.imshow("original", img)

    # Display the thresholded image
    cv2.imshow("thresholdimg", thresholdimg)

    # Wait for a key press indefinitely
    cv2.waitKey(0)

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()
