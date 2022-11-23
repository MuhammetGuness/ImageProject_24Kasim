import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
import os.path

def noise(img):
	row,col = img.shape
	num_pix = random.randint(300, 10000)
	for i in range(num_pix):
		y_coord=random.randint(0, row-1)
		x_coord=random.randint(0, col-1)
		img[y_coord][x_coord] = 255
	num_pix = random.randint(300 , 10000)
	for i in range(num_pix):
		y_coord=random.randint(0, row - 1)
		x_coord=random.randint(0, col - 1)
		img[y_coord][x_coord] = 0
	return img

img = cv2.imread(r"C:\Users\Muhammet\Desktop\foto.jpeg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r"C:\Users\Muhammet\Desktop\foto.jpeg",noise(img))
print(img)
print(img.ravel())
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram')
plt.show()
