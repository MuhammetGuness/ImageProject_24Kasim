import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Muhammet\Desktop\foto.jpeg")

sharp_filt = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharp_img = cv2.filter2D(img, -1, sharp_filt)

cv2.imshow('İlk', img)
cv2.waitKey(0)
cv2.imshow('Son', sharp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()