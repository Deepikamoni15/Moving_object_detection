import cv2  # OpenCV
#import time  # delay
import imutils  # resize

cam = cv2.VideoCapture(0)  # camera ID
#time.sleep(1)

firstFrame = None
area = 500

while True:
    ret, img = cam.read()  # read from the camera
    if not ret:
        break

    text = "Normal"
    img = imutils.resize(img, width=500)  # resize
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)  # smoothen image

    if firstFrame is None:
        firstFrame = gaussianImg  # capturing the first frame
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg)  # absolute difference
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg, None, iterations=2)  # erosion or closing gaps

    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < area:  # filter small areas
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object Detected"

    print(text)
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("cameraFeed", img)

    key = cv2.waitKey(10)
    if key == ord("q"):  # quit condition
        break

cam.release()
cv2.destroyAllWindows()
