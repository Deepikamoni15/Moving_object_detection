import cv2
import imutils
img=cv2.imread('new.jpg')
resizedimg=imutils.resize(img,width=100)
cv2.imshow('original.jpg',img)
cv2.imshow('resized.jpg',resizedimg)
cv2.imwrite('resized .jpg',resizedimg)
