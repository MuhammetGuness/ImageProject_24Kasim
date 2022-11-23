import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

img = cv2.imread(r"C:\Users\Muhammet\Desktop\foto.jpeg")
cv2.imshow("İlk",img)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray_img)
img_gaussian = cv2.GaussianBlur(gray_img,(25,25),0)

sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
sobel_img = sobelx + sobely
cv2.imshow("Sobel",sobel_img)

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
img_prewitt = img_prewitty + img_prewittx
cv2.imshow("Prewitt",img_prewitt)

img = cv2.imread(r"C:\Users\Muhammet\Desktop\foto.jpeg",0).astype("float64")
img = img/255.0
roberts_cross_v = np.array([[1, 0 ],[0,-1 ]])
roberts_cross_h = np.array([[ 0, 1 ],[ -1, 0 ]])
vertical = ndimage.convolve( img, roberts_cross_v )
horizontal = ndimage.convolve( img, roberts_cross_h )
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
edged_img*=255
cv2.imshow("Edged",edged_img)

img2 = cv2.imread(r"C:\Users\Muhammet\Desktop\foto.jpeg")
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
cv2.imshow("Blurring",blur)
edges = cv2.Canny(blur,75,75)
cv2.imshow("Edges",edges)