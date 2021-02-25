import numpy as np
import cv2
import glob
import os

logo = cv2.imread('mylogo.jpg')
h_logo, w_logo, channels = logo.shape

path = glob.glob('Images/*.*')

for path_img in path:

    img = cv2.imread(path_img)
    h_img, w_img, channels = img.shape 
    #print(h_img, w_img) 

    # center of the original image
    center_x = int(w_img / 2)
    center_y = int(h_img / 2)

    top = center_y - int(h_logo / 2)
    left = center_x - int(w_logo / 2)

    bottomY = top + h_logo
    rightX = left + w_logo 

    region = img[top: bottomY, left: rightX]
    result = cv2.addWeighted(region, 1, logo, 0.4, 0)
    img[top: bottomY, left: rightX] = result

    file = os.path.basename(path_img)
    cv2.imwrite('Images/watermark_' + file, img)