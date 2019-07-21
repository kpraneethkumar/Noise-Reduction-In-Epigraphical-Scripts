import numpy as np
import math
import cv2


im = cv2.imread("e.png",0)
h,w = im.shape[:2]

for i in range(0,h-2):
    for j in range(0,w-2):
    
        if(im[i+1][j+1]<127):#balck center 
            count=0
            for k in range(0,3):
                for l in range(0,3):
                    if(im[i+k][j+l]<127):
                        count=count+1
            count=count-1
            if(count<=2):
                im[i+1][j+1]=255
                
                        
        
        if(im[i+1][j+1]>127):#white center
            count=0
            for k in range(0,3):
                for l in range(0,3):
                    if(im[i+k][j+l]>127):
                        count=count+1
            count=count-1
            if(count<=3):
                im[i+1][j+1]=0
                
                
                
        

print("end of the program")
cv2.imshow("image",im)
cv2.waitKey(0)
cv2.imwrite("im33.png",im)
