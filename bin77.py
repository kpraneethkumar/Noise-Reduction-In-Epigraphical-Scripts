import numpy as np
import math
import cv2


im = cv2.imread("e.png",0)
h,w = im.shape[:2]

for i in range(2,h-4):
    for j in range(2,w-4):
    
        if(im[i+1][j+1]<127):#black center 
            count=0
            count1=0
            count2=0
            for k in range(0,3):
                for l in range(0,3):
                    if(im[i+k][j+l]<127):
                        count=count+1
            count=count-1
            if(count<=3):
                im[i+1][j+1]=255
            else:
                x=i-1
                y=j-1
                for m in range(0,5):
                    for n in range(0,5):
                        if(im[x+m][y+n]<127):
                            count1=count1+1
                count1=count1-1
                count1=count1-count
                if(count1<=5):
                    im[i+1][j+1]=255
                else:
                    a=i-2
                    b=j-2
                    for m in range(0,7):
                        for n in range(0,7):
                            if(im[a+m][b+n]<127):
                                count2=count2+1
                    count2=count2-1
                    count2=count2-count1-count
                    if(count2<=8):
                        im[i+1][j+1]=255
        
        if(im[i+1][j+1]>127):#white center
            count=0
            count1=0
            count2=0
            for k in range(0,3):
                for l in range(0,3):
                    if(im[i+k][j+l]>127):
                        count=count+1
            count=count-1
            if(count<=3):
                im[i+1][j+1]=0
            else:
                x=i-1
                y=j-1
                for m in range(0,5):
                    for n in range(0,5):
                        if(im[x+m][y+n]>127):
                            count1=count1+1
                count1=count1-1
                count1=count1-count
                if(count1<=5):
                    im[i+1][j+1]=0
                else:
                    a=i-2
                    b=j-2
                    for m in range(0,7):
                        for n in range(0,7):
                            if(im[a+m][b+n]>127):
                                count2=count2+1
                    count2=count2-1
                    count2=count2-count1-count
                    if(count2<=8):
                        im[i+1][j+1]=0
        

print("end of the program")
cv2.imshow("image",im)
cv2.waitKey(0)
cv2.imwrite("im77.png",im)
