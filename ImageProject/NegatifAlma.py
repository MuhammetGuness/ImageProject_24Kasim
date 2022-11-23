import cv2
import numpy as np
import matplotlib.pyplot as plt

def neg_img(img):
    L=np.max(img)
    negatif=L-img
    return negatif

img = cv2.imread(r"C:\Users\Muhammet\Desktop\foto.jpeg",0)
negatif= neg_img(img)
birlesik = np.hstack((img, negatif))
print("Birleşik:", birlesik.shape)

plt.imshow(birlesik,cmap="gray")
plt.show()