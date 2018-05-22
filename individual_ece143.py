import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import numpy as np
from itertools import cycle
import time
'''
Jinbum Park 
ECE 143 
Date : 05-22-2018
Project Name:individual project
FileName : individual_ECE143.py
'''
def drawcanvas():
    '''
    Ask user the width and height of the canvas and
    draw the canvas
    :return: width and height of canvas
    '''
    width = input("what is the width =")
    height = input("what is the height = ")
    return (width, height)

def drawRec(canvasX,canvasY,canvas):
    '''
    draw the rectangle on the canvas with random size at random point
    :param canvasX: width of canvas
    :param canvasY: height of canvas
    :param canvas: canvas
    :return:
    '''
    startX = random.randint(0,canvasX)
    startY = random.randint(0,canvasY)
    width = random.randint(0,canvasX-startX)
    height = random.randint(0,canvasY-startY)
    if (width == 0) or (height == 0):
        return drawRec(canvasX, canvasY, canvas)
    else:
        cycol = ('bgrcmyk')
        color = cycol[(random.randint(0, 6))]
        rectangle = plt.Rectangle((startX,startY),width,height,edgecolor=color, linewidth='3', facecolor=color, alpha=0.1)
        return canvas,startX,startY,width,height,rectangle

    return canvas, startX,startY,width,height,rectangle

def saveRecinfo(x,y,width,height,listRec):
    '''
    save the rectangle information in to the list of rectangles on canvas
    :param x: start x of rec
    :param y: start y or rec
    :param width: width of rec
    :param height: height of rec
    :param listRec: list of rectangles on the canvas
    :return: list of rectangles in the canvas
    '''
    assert isinstance(listRec,list)
    recinfo = [x,y,width,height]
    listRec.append(recinfo)
    return listRec

def trimRec(listRec,canvas):
    '''

    :param listRec:
    :param canvas:
    :return:
    '''

    if len(listRec) ==1 :
        pass

    idxLast = len(listRec)-1
    lastX = listRec[idxLast][0]
    lastY = listRec[idxLast][1]
    lastWidth = listRec[idxLast][2]
    lastHeight = listRec[idxLast][3]
    Point3 = [lastX,lastY]
    Point4 = [lastX+lastWidth, lastY+lastHeight]
    #max_Area include data of [Area,index.1st of 2nd rectnagle]
    max_Area = [0,0,0]
    newRec =[0,0,0,0]
    for i in range(len(listRec)-1):
        currX = listRec[i][0]
        currY = listRec[i][1]
        currWidth = listRec[i][2]
        currHeight = listRec[i][3]
        maxX = currX + currWidth
        maxY = currY + currHeight
        Point1 = [currX,currY]
        Point2 = [maxX,maxY]
        #check the corrupt of rectangle
        if((Point1[0] <Point3[0]) and(Point2[0] <Point4[0]) and (Point1[1] > Point3[1]) and (Point2[1] > Point4[1])):
            print("Case of 1 - right lower - 2rec")
            firstArea = (Point4[0]-Point2[0])*lastHeight
            secondArea = (Point1[1] - Point3[1])*lastWidth
            if (max(firstArea, secondArea) >= max_Area[0]):
                if (firstArea > secondArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point2[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point4[0] - Point2[0]
                    newRec[3] = lastHeight
                else:
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point1[1] - Point3[1]

        elif((Point1[0] > Point3[0]) and (Point2[0] > Point4[0]) and (Point1[1] > Point3[1]) and (Point2[1] > Point4[1])):
            print("Case of 2- left lower - 2rec")
            firstArea =(Point1[0]-Point3[0])*lastHeight
            secondArea = (Point1[1] - Point3[1])*lastWidth
            if (max(firstArea, secondArea) >= max_Area[0]):
                if (firstArea > secondArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point1[0] - Point3[0]
                    newRec[3] = lastHeight
                else:
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point1[1] - Point3[1]

        elif((Point1[0] < Point3[0]) and(Point2[0] < Point4[0])and (Point1[1] < Point3[1]) and (Point2[1] < Point4[1])):
            print("Case of 3 - right upper - 2rec")
            firstArea = (Point4[1] - Point2[1])*lastWidth
            secondArea = (Point4[0]-Point2[0]) * lastHeight
            if (max(firstArea, secondArea) >= max_Area[0]):
                if (firstArea > secondArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point3[0]
                    newRec[1] = Point2[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point4[1] - Point2[1]
                else:
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point2[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point4[0]-Point2[0]
                    newRec[3] = lastHeight

        elif((Point1[0] > Point3[0]) and (Point2[0] > Point4[0]) and (Point1[1] < Point3[1]) and (Point2[1] < Point4[1])):
            print("Case of 4 - left upper - 2rec")
            firstArea = (Point1[0] - Point3[0])*lastHeight
            secondArea = (Point4[1] - Point2[1])*lastWidth
            if (max(firstArea, secondArea) >= max_Area[0]):
                if (firstArea > secondArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point1[0] - Point3[0]
                    newRec[3] = lastHeight
                else:
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point3[0]
                    newRec[1] = Point2[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point4[1] - Point2[1]

        elif ((Point1[0] > Point3[0]) and (Point2[0] > Point4[0]) and (Point1[1] < Point3[1]) and (Point2[1] > Point4[1])):
            print("Case of 5 - Paralel left - 1 rec")
            firstArea = (Point1[0]-Point3[0])*lastHeight
            if (firstArea >= max_Area[0]):
                max_Area[0] = firstArea
                max_Area[1] = i
                max_Area[2] = 0
                newRec[0] = Point3[0]
                newRec[1] = Point3[1]
                newRec[2] = Point1[0] - Point3[0]
                newRec[3] = lastHeight

        elif ((Point1[0] < Point3[0]) and (Point2[0] < Point4[0]) and (Point1[1] < Point3[1]) and (Point2[1] > Point4[1])):
            print("Case of 6 - Parallel right - 1 rec")
            firstArea = (Point4[0]-Point2[0])*lastHeight
            if (firstArea >= max_Area[0]):
                max_Area[0] = firstArea
                max_Area[1] = i
                max_Area[2] = 0
                newRec[0] = Point2[0]
                newRec[1] = Point3[1]
                newRec[2] = Point4[0] - Point2[0]
                newRec[3] = lastHeight

        elif ((Point1[0] < Point3[0]) and (Point2[0] > Point4[0]) and (Point1[1] > Point3[1]) and (Point2[1] > Point4[1])):
            print("Case of 7 - Parallel down - 1 rec")
            firstArea = (Point1[1]-Point3[1])*lastWidth
            if (firstArea >= max_Area[0]):
                max_Area[0] = firstArea
                max_Area[1] = i
                max_Area[2] = 0
                newRec[0] = Point3[0]
                newRec[1] = Point3[1]
                newRec[2] = lastWidth
                newRec[3] = Point1[1]-Point3[1]

        elif ((Point1[0] < Point3[0]) and (Point2[0] > Point4[0]) and (Point1[1] < Point3[1]) and (Point2[1] > Point4[1])):
            print("Case of 8 - parallel up - 1 rec")
            firstArea = (Point4[1]-Point2[1])*lastWidth
            if (firstArea >= max_Area[0]):
                max_Area[0] = firstArea
                max_Area[1] = i
                max_Area[2] = 0
                newRec[0] = Point3[0]
                newRec[1] = Point2[1]
                newRec[2] = lastWidth
                newRec[3] = Point4[1]-Point2[1]

        elif ((Point1[0] > Point3[0]) and (Point2[0] < Point4[0]) and (Point1[1] > Point3[1]) and (Point2[1] < Point4[1])):
            print("Case of 9 - Totally outside - 4 rec")
            firstArea =(Point4[1] - Point2[1]) * lastWidth
            secondArea =(Point1[1] - Point3[1])*lastWidth
            thirdArea = (Point1[0]-Point3[0])*lastHeight
            fourthArea = (Point4[0] - Point2[0])*lastHeight
            if(max(firstArea,secondArea,thirdArea,fourthArea) >= max_Area[0]):
                if (max(firstArea,secondArea,thirdArea,fourthArea) == firstArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point3[0]
                    newRec[1] = Point2[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point4[1] - Point2[1]
                elif(max(firstArea,secondArea,thirdArea,fourthArea) == secondArea):
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point1[1] - Point3[1]
                elif(max(firstArea,secondArea,thirdArea,fourthArea) == thirdArea):
                    max_Area[0] = thirdArea
                    max_Area[1] = i
                    max_Area[2] = 2
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point1[0]-Point3[0]
                    newRec[3] = lastHeight
                else:
                    max_Area[0] = fourthArea
                    max_Area[1] = i
                    max_Area[2] = 3
                    newRec[0] = Point2[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point4[0] - Point2[0]
                    newRec[3] = lastHeight

        elif ((Point1[0] < Point3[0]) and (Point2[0] > Point4[0]) and (Point1[1] < Point3[1]) and (Point2[1] > Point4[1])):
            print("Case of 10 - Totally inside - no rec")
            newRec[0] = lastX
            newRec[1] = lastY
            newRec[2] = lastWidth
            newRec[3] = lastHeight
        elif ((Point1[0] > Point3[0]) and (Point2[0] < Point4[0]) and (Point1[1] < Point3[1]) and (Point2[1] > Point4[1])):
            print("Case of 11 - long Parallel - 2 rec right and left")
            firstArea = (Point1[0] - Point3[0])*lastHeight
            secondArea = (Point4[0] - Point2[0])*lastHeight
            if (max(firstArea, secondArea) >= max_Area[0]):
                if (firstArea > secondArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point1[0] - Point3[0]
                    newRec[3] = lastHeight
                else:
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point2[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point4[0] - Point2[0]
                    newRec[3] = lastHeight

        elif ((Point1[0] < Point3[0]) and (Point2[0] > Point4[0]) and (Point1[1] > Point3[1]) and (Point2[1] < Point4[1])):
            print("Case of 12 - tall Parallel - 2 rec up and down")
            firstArea = (Point4[1] - Point2[1])*lastWidth
            secondArea = (Point1[1] - Point3[1])*lastWidth
            if (max(firstArea, secondArea) >= max_Area[0]):
                if (firstArea > secondArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point4[1] - Point2[1]
                else:
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point2[0]
                    newRec[1] = Point3[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point1[1] - Point3[1]

        elif ((Point1[0] > Point3[0]) and (Point2[0] < Point4[0]) and (Point1[1] > Point3[1]) and (Point2[1] > Point4[1])):
            print("Case of 13 - Supper down - 3rec ")
            firstArea = (Point1[0] - Point3[0])*lastHeight
            secondArea = (Point1[1] - Point3[1])*lastWidth
            thirdArea = (Point4[0]-Point2[0])*lastHeight
            if(max(firstArea,secondArea,thirdArea) > max_Area[0]):
                if(max(firstArea,secondArea,thirdArea) == firstArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point1[0] - Point3[0]
                    newRec[3] = lastHeight
                elif(max(firstArea,secondArea,thirdArea) == secondArea):
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point1[1] - Point3[1]
                else:
                    max_Area[0] = thirdArea
                    max_Area[1] = i
                    max_Area[2] = 2
                    newRec[0] = Point2[0]
                    newRec[1] = Point3[1]
                    newRec[2] =Point4[0]-Point2[0]
                    newRec[3] = lastHeight

        elif ((Point1[0] > Point3[0]) and (Point2[0] < Point4[0]) and (Point1[1] < Point3[1]) and (Point2[1] < Point4[1])):
            print("Case of 14 - Supper up - 3rec ")
            firstArea = (Point1[0] - Point3[0]) * lastHeight
            secondArea = (Point4[1] - Point2[1]) * lastWidth
            thirdArea = (Point4[0] - Point2[0]) * lastHeight
            if (max(firstArea, secondArea, thirdArea) > max_Area[0]):
                if (max(firstArea, secondArea, thirdArea) == firstArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point1[0] - Point3[0]
                    newRec[3] = lastHeight
                elif (max(firstArea, secondArea, thirdArea) == secondArea):
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point3[0]
                    newRec[1] = Point2[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point4[1] - Point2[1]
                else:
                    max_Area[0] = thirdArea
                    max_Area[1] = i
                    max_Area[2] = 2
                    newRec[0] = Point2[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point4[0] - Point2[0]
                    newRec[3] = lastHeight

        elif ((Point1[0] < Point3[0]) and (Point2[0] < Point4[0]) and (Point1[1] > Point3[1]) and (Point2[1] < Point4[1])):
            print("Case of 15 -Supper right - 3rec")
            firstArea = (Point1[1] - Point3[1]) * lastWidth
            secondArea = (Point4[0] - Point2[0]) * lastHeight
            thirdArea = (Point4[1] - Point2[1]) * lastWidth
            if (max(firstArea, secondArea, thirdArea) > max_Area[0]):
                if (max(firstArea, secondArea, thirdArea) == firstArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point1[1] - Point3[1]
                elif (max(firstArea, secondArea, thirdArea) == secondArea):
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point2[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point4[0] - Point2[0]
                    newRec[3] = lastHeight
                else:
                    max_Area[0] = thirdArea
                    max_Area[1] = i
                    max_Area[2] = 2
                    newRec[0] = Point3[0]
                    newRec[1] = Point2[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point4[1] - Point2[1]


        elif ((Point1[0] > Point3[0]) and (Point2[0] > Point4[0]) and (Point1[1] > Point3[1]) and (Point2[1] < Point4[1])):
            print("Case of 16 - Supper left - 3rec ")
            firstArea = (Point1[1] - Point3[1]) * lastWidth
            secondArea = (Point1[0] - Point3[0]) * lastHeight
            thirdArea = (Point4[1] - Point2[1]) * lastWidth
            if (max(firstArea, secondArea, thirdArea) > max_Area[0]):
                if (max(firstArea, secondArea, thirdArea) == firstArea):
                    max_Area[0] = firstArea
                    max_Area[1] = i
                    max_Area[2] = 0
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point1[1] - Point3[1]
                elif (max(firstArea, secondArea, thirdArea) == secondArea):
                    max_Area[0] = secondArea
                    max_Area[1] = i
                    max_Area[2] = 1
                    newRec[0] = Point3[0]
                    newRec[1] = Point3[1]
                    newRec[2] = Point1[0] - Point3[0]
                    newRec[3] = lastHeight
                else:
                    max_Area[0] = thirdArea
                    max_Area[1] = i
                    max_Area[2] = 2
                    newRec[0] = Point3[0]
                    newRec[1] = Point2[1]
                    newRec[2] = lastWidth
                    newRec[3] = Point4[1] - Point2[1]
        else:
            print("rectangle not corrupted")
            newRec[0] = lastX
            newRec[1] = lastY
            newRec[2] = lastWidth
            newRec[3] = lastHeight
    p = patches.Rectangle((listRec[idxLast][0],listRec[idxLast][1]),listRec[idxLast][2],listRec[idxLast][3],fill=False,edgecolor="none")
    listRec[idxLast] = newRec
    print(listRec[idxLast])
    cycol = ('bgrcmyk')
    color = cycol[(random.randint(0, 6))]
    rectangle = plt.Rectangle((newRec[0], newRec[1]), newRec[2], newRec[3], edgecolor=color, linewidth='3', facecolor=color,alpha=0.1)
    return listRec,rectangle,p

def gettotalsurface(listRec):
    '''
    sum of all the recatangle surfaces in the canvas
    :param listRec: list of rectangles in the canvas with rectangle information
    :return: totalArea:
    '''
    totalArea = 0

    for i in range(len(listRec)):
        width_i = listRec[i][2]
        height_o = listRec[i][3]
        totalArea = totalArea + (width_i*height_o)

    return totalArea


def main(canvasX,canvasY):
    '''
    main function draw the rectangle as much as we can draw, and if it is over the max
    surface area amount(width x he
    :param canvasX: width of the canvas,input by the user at the beginning
    :param canvasY: height of the canvas,input by the user at the beginnig
    :return: canvas,
    '''

    canvas = plt.figure()        # draw the canvas
    ax =canvas.add_subplot(111)  # setting for the canvas add_subplot
    plt.xlim(0,canvasX)          # x limit of canvas
    plt.ylim(0,canvasY)          # y limit of canvas
    listRec = []                 # empty list for rectangles

    # draw first rectangle on the canvas
    [canvas, x, y, width, height, rectangle] = drawRec(canvasX, canvasY, canvas)
    ax.add_patch(rectangle)
    saveRecinfo(x, y, width, height, listRec)   # save rectangle information on the list

    #print(listRec)

    canvasArea = canvasX*canvasY # total area of canvas
    totalArea = 0                # total area parameter for rectangles sum
    recCnt = 1                   # we don't trim the first rectangle so counter start with 1

    #  while loop, we draw and trim the rectangle till...
    #  the sum of surface of rectangles goes over than total canvas area
    while(totalArea<=canvasArea):
        print("before add rectangle")
        print(totalArea)
        [canvas, x, y, width, height, rectangle] = drawRec(canvasX, canvasY, canvas)
        ax.add_patch(rectangle)
        saveRecinfo(x, y, width, height, listRec)
        [listRec, rectangle,p] = trimRec(listRec, canvas)
        totalArea = gettotalsurface(listRec)
        #print(totalArea)
        print(listRec)
        ax.add_patch(p)
        ax.add_patch(rectangle)
    #remove the last item of the rectangle which makes it over the canvas Area
    listRec.pop()
    num_rec = len(listRec)
    finalArea = gettotalsurface(listRec)
    plt.show()

    return  canvas,finalArea,num_rec
'''

'''
trialcycle = input("How many cycle you want to run :")
canvasX = input("What is the x limit of canvas :")
canvasY = input("what is the y limit of canvas :")
canvasSurface = canvasX*canvasY
avg_surface = 0
avg_num_rec = 0
for i in range(trialcycle):
    [canvas,finalArea,num_rec] = main(canvasX,canvasY)

    avg_num_rec= avg_num_rec + num_rec
    avg_surface = avg_surface + finalArea

avg_num_rec = float(avg_num_rec/trialcycle)
avg_surface = float(avg_surface/trialcycle)


print ("There are average {} of rectangle communication boxes covering {}% of the Surface.").format(avg_num_rec,float(100.*((avg_surface)/(canvasSurface))))


