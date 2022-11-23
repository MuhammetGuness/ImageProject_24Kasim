import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Muhammet\Desktop\foto.jpeg")

for gamma in [3.0,4.0,5.0]:
    gamma_apply = np.array(255*(img/255)**gamma, dtype = 'uint8')
    cv2.imshow("Muhammet", gamma_apply)
    cv2.waitKey(0)
cv2.destroyAllWindows()