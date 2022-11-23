import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def BitChange(input_file_path, pixel_size):
    img = Image.open(input_file_path)
    img = img.resize((img.size[0] // pixel_size, img.size[1] // pixel_size), Image.NEAREST)
    img = img.resize((img.size[0] * pixel_size, img.size[1] * pixel_size), Image.NEAREST)
    img.show(title=str(pixel_size)+"Bit Image")
    
def GrayScaleToBit():
    bits = [8,16,24]
    imgPath = 'C:/Users/Muhammet/Desktop/foto.jpeg'
    saveImgPath = 'C:/Users/Muhammet/Desktop/grifoto.jpeg'
    Image.open(imgPath).convert('RGB').convert('L').save(saveImgPath)
    for index in range(3):
        BitChange(saveImgPath,bits[index])
    img = Image.open(saveImgPath)
    img.show()
    
GrayScaleToBit()