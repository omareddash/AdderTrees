'''this function will lay out the basis of filter computation for image filters and such.
The flow will start by reading image and applying a simple sobel filter to track the mathematical data flow


'''
import csv
import pandas as pd
import numpy
from numpy import zeros

sobelx = [[1,0,-1],[2,0,-2],[1,0,-1]]
sobely = [[1,2,1],[0,0,0],[-1,-2,-1]]
F1 = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
F2 = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9,1/9, 1/9]]

def LoadImageData(fil):
    image1 = pd.read_csv("Image4.csv", index_col=None, header=None)
    img = numpy.array(image1)
    subimg = img[0:3,0:3]
    #print(image1)
    #print(subimg)
    #print (image1[63][63])
    #image = csv.reader('Lenna.csv',delimiter=',')
    #print('image')
    #print(image)
    w = len(fil)
    h = len(fil[1])
    wi = len(image1)
    hi = len(image1[0])
    map = [x[:] for x in [[0] * hi] * wi]
    imedged = [x[:] for x in [[0] * (hi-(h-1))] * (wi-(w-1))]
    add = zeros([hi-(h-1),wi-(w-1),h*w*w])
    for x in range (0,wi-w+1):
        for y in range (0,hi-h+1):
            n = 0
            subimg = img[x:x+w,y:y+h]
            for xf in range (0,w):
                for yf in range(0,h):
                    for k in range(0,h):
                        element = (subimg[xf][k])*(fil[k][yf])
                        #print(element)
                        add[x,y,n] = element
                        n = n+1
                        imedged[x][y] = imedged[x][y] + element
    #for i in range (0,len(imedged)-1):
    #    print(imedged[i])
    #print(len(imedged))

    #print(add.shape)
    #print(add)
    return add
LoadImageData(F2)