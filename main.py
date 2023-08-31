import cv2
from pylsd.lsd import lsd
import numpy as np
import os

def get_absolute_paths(directory_path):#If you want to analyze multiple images
    return [os.path.abspath(os.path.join(directory_path, filename)) for filename in os.listdir(directory_path)]


def func_lsd(img_path):
    r = img_path[img_path.rfind('/') + 1:] # Extract onle the name of the image
    img_name = r[:r.find('.')]

    img = cv2.imread(img_path)#import a image
    img = cv2.resize(img, (600, 300))

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# Convert the color image to grayscale.
    gray = cv2.GaussianBlur(gray,(5,5),5)# Apply Gaussian blur to the grayscale image.
    linesL = lsd(gray)# Apply LSD line detector on grayscale image 'gray'
    num_all_lines = len(linesL)
    num_long_lines = 0
    print(num_all_lines,"all lines")# Print the number of detected lines
    img3 = img.copy()# Copy the original image 'img'
    img4 = img.copy()
    for line in linesL:# Iterate over each detected line
        x1, y1, x2, y2 = map(int,line[:4])# Extract start and end points of the line
        img3 = cv2.line(img3, (x1,y1), (x2,y2), (0,0,255), 3)# Draw the line on the copied image 'img3'
        if (x2-x1)**2 + (y2-y1)**2 > 1000:# Draw line on 'img4' if line's length squared is over 1000.
            img4 = cv2.line(img4, (x1,y1), (x2,y2), (0,0,255), 3)
            num_long_lines += 1
    print(num_long_lines,"long lines")# Print the number of detected long lines
    # cv2.imwrite(os.path.join(dir_path, f'r3_all_lins_{img_name}.jpg') ,img3)# Save the image if you want
    # cv2.imwrite(os.path.join(dir_path, f'r3_long_lines_{img_name}.jpg') ,img4)# Save the image if you want


#If you want to analyze multiple images
#Save the images in a directory named city_pic and then
# list_images = get_absolute_paths('city_pic')#dir containing the images that you want to analyze
# for i in list_images:
#     # print(i)
#     img_name = i[i.rfind('/') + 1:] # Extract onle the name of the image
#     print(img_name)
#     func_lsd(i)

# If you want to analyze a single image
img = 'city.jpg'
func_lsd(img)