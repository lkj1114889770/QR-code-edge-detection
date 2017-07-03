# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:07:18 2016

@author: 刘凯鉴
"""

import cv2
import numpy as np
from time import clock
def nothing(x):
    pass

#cv2.namedWindow('edges')
#cv2.createTrackbar('canny_min','edges',0,255,nothing)
#cv2.createTrackbar('canny_max','edges',0,255,nothing)

img=cv2.imread('temp.bmp',cv2.IMREAD_GRAYSCALE)
cv2.imshow("img",img)
img_gb = cv2.GaussianBlur(img, (5, 5), 0)
#while(1):
#    k=cv2.waitKey(1)
#    if k==27:
#        break
#    else:
#        cmin=cv2.getTrackbarPos('canny_min','edges')
#        cmax=cv2.getTrackbarPos('canny_max','edges')
#        edges = cv2.Canny(img_gb, cmin , cmax)
#        cv2.imshow("edges", edges)  
start=clock()
edges=cv2.Canny(img_gb,100,150)
cv2.imshow("edges", edges)
finish=clock()
print(finish-start)
image, contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
found=[]
hierarchy = hierarchy[0]
for i in range(len(contours)):
    k = i
    c = 0
    
    while hierarchy[k][2]!=-1:
        k = hierarchy[k][2]
        c = c + 1
    if c >= 5:
        found.append(i)
#img_dc = img.copy()
#for i in found:
#    cv2.drawContours(img_dc, contours, i, (255,0 , 0), 3)
#cv2.imshow('img_dc',img_dc)
draw_img = img.copy()
rects=[]
for i in found:
    rect=cv2.minAreaRect(contours[i])
    rects.append(rect)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(draw_img,[box], 0, (255,0,0), 3)
zuobiao=[]
for r in rects:
    zuobiao.append(r[0])
zuobiao=np.int0(zuobiao)
for i in range(len(zuobiao)):
    j=i+1
    while(j<3):
        cv2.line(draw_img,tuple(zuobiao[i]),tuple(zuobiao[j]),(255,0,0),3)
        j=j+1
print(zuobiao)

cv2.imshow('draw_img',draw_img)
cv2.waitKey(0)  
cv2.destroyAllWindows() 