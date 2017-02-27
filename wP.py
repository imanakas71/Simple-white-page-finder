#!/usr/bin/env python
#coding:utf-8

import numpy as np
import re
import cv2
import sys
lineTmp=0
lineBufferY = []
lineBufferX = []
threshold = 232

targetExtention=["jpg","JPG","jpeg","png","PNG"]
def scanImageVertical(filename):
    img = cv2.imread(filename)
    height = img.shape[0]
    width = img.shape[1]
    #print "(width, height) = ", width, height
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    for x in range(width-1):
        lineTmp=0
        for y in range(height-1):
            #print "(x,y) = ", x, y
            grayPixel = gray.item(y,x)
            lineTmp = lineTmp+grayPixel
        average = lineTmp/height
        #print "average = ", average
        lineBufferY.append(average)
        currentIndex = len(lineBufferY)-1
        if currentIndex > 0:
            #print "currentIndex=", currentIndex
            if average < threshold:
                returnValue = -1
                break
            else:
                returnValue = 0
    return(returnValue)

def scanImageHolizontal(filename):
    img = cv2.imread(filename)
    height = img.shape[0]
    width = img.shape[1]
    #print "(width, height) = ", width, height
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    for y in range(height-1):
        lineTmp=0
        for x in range(width-1):
            #print "(x,y) = ", x, y
            grayPixel = gray.item(y,x)
            
            lineTmp = lineTmp+grayPixel
        average = lineTmp/width
        #print "average = ", average
        lineBufferX.append(average)
        currentIndex = len(lineBufferX)-1
        if currentIndex > 0:
            #print "currentIndex=", currentIndex
            if average < threshold:
                returnValue = -1
                break
            else:
                returnValue = 0
    return(returnValue)



def findWhitePapers(fileList):
    numberOfFiles = len(fileList)-1
    #print "number of files = ", numberOfFiles
    for i in range(numberOfFiles):
        index = i+1
        targetFile = fileList[index]
        #print "targetFile = ", targetFile
        for ext in targetExtention:
            if len(re.findall(ext, targetFile))!=0:
                wpy = scanImageVertical(targetFile)
                if (wpy == 0):
                    wpx = scanImageHolizontal(targetFile)
                    if (wpx == 0):
                        print targetFile," is supposed to be a white page."


if __name__ == '__main__':
    print "White page finder"
    args = sys.argv
    findWhitePapers(args)
