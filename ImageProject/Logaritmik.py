import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Muhammet\Desktop\foto.jpeg")

x = 255/np.log(1+np.max(img))
log_img = x * (np.log(img+1))
log_img = np.array(log_img, dtype = np.uint8)

plt.imshow(img)
plt.show()
plt.imshow(log_img)
plt.show()