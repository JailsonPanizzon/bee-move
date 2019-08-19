import cv2
from PIL import Image
import math
import numpy as np
import time

def click(event, x, y, flags, param):
    global point
    if event == cv2.EVENT_LBUTTONDBLCLK:
        point = (y,x)
        print(point)
        print("press c to confirm")

def crescimento_regiao(cord,im):
    cont=0
    reg=[]
    reg.append(cord)
    actual=[]
    actual.append(cord[0])
    actual.append(cord[1])
    while(cont<len(reg)):
        actual[0]=reg[cont][0]
        actual[1]=reg[cont][1]
        for i in (-1,0,1):
            y=i+actual[0]
            if(y < im.shape[1] and y>=0):
                for j in (-1,0,1):
                    x=j+actual[1]
                    if(x< im.shape[0] and x>=0):
                        if(not([y,x] in reg)):
                            distancia_find = math.sqrt((im[x,y]-im[actual[1],actual[0]])**2)

                            #distancia= math.sqrt((pow((px[y,x][0])-px[actual[0],actual[1]][0],2)+pow((px[y,x][1])-px[actual[0],actual[1]][1],2)+pow((px[y,x][2])-px[actual[0],actual[1]][2],2)))
                            #distancia_find=math.sqrt((pow((px[cord[0],cord[1]][0])-px[actual[0],actual[1]][0],2)+pow((px[cord[0],cord[1]][1])-px[actual[0],actual[1]][1],2)+pow((px[cord[0],cord[1]][2])-px[actual[0],actual[1]][2],2)))
                            if(distancia_find < 3 ):
                               reg.append([y,x])

        cont+=1
    return reg

def equaliza(img):
    #equaliza imagens nos canais R,G,B
    b, g, r = cv2.split(img)
    red = cv2.equalizeHist(r)
    green = cv2.equalizeHist(g)
    blue = cv2.equalizeHist(b)
    blue=b
    return cv2.merge((blue, green, red))

def passaAlta(im):
    im2 = im.copy()
    limar= 1
    i= 0
    while i< im.shape[0]-1:
        j=0
        while j < im2.shape[1]-1:
            distancia= math.sqrt((im[i-1,j]-im[i,j])**2)
            distanci= math.sqrt((im[i,j-1]-im[i,j])**2)
            if(distancia>limar or distanci>limar):
                if((im[i,j])< 70):
                    im2[i,j] = im[i,j]-20
                else:
                    im2[i,j] = im[i,j]+40
            else:
                im2[i,j] = im[i,j]+20
            j+=1
        i+=1
    return im2
siz= [380,240]
cap = cv2.VideoCapture("bee2.avi")
while True:
    ret,img = cap.read()
    #img = cv2.imread('images.jpg')
    img = cv2.resize(img,(siz[0],siz[1]))
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click)
    while True:
        cv2.imshow("image", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("c"):
            cv2.destroyWindow('image')
            break

    img = equaliza(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img=passaAlta(img)
    cv2.imwrite('teste.png',img)
    reg = crescimento_regiao(point,img)
    maiorx=reg[0][1]
    maiory=reg[0][0]
    menorx=reg[0][1]
    menory=reg[0][0]
    for i in reg:
        if(maiorx<i[1]):
            maiorx=i[1]
        if(maiory<i[0]):
            maiory=i[0]
        if(menorx>i[1]):
            menorx=i[1]
        if(menory>i[0]):
            menory=i[0]
    cv2.rectangle(img, (menorx-10,menory-10),(maiorx+10, maiory+10), (255,0,0),2)
    cv2.namedWindow("image")
    cv2.imwrite("reg.png",img)
    break;
centro = (maiory-(maiory-menory),menorx+(maiorx-menorx))
cap = cv2.VideoCapture("bee2.avi")
cont = 0
while True:
    cont+=1
    ret,img = cap.read()
    img = cv2.resize(img,(siz[0],siz[1]))
    img = equaliza(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img=passaAlta(img)
    reg = crescimento_regiao(point,img)
    maiorx=reg[0][1]
    maiory=reg[0][0]
    menorx=reg[0][1]
    menory=reg[0][0]
    for i in reg:
        if(maiorx<i[1]):
            maiorx=i[1]
        if(maiory<i[0]):
            maiory=i[0]
        if(menorx>i[1]):
            menorx=i[1]
        if(menory>i[0]):
            menory=i[0]
    cv2.rectangle(img, (menorx-10,menory-10),(maiorx+10, maiory+10), (255,0,0),2)
    cv2.imwrite("nic/"+str(cont)+".png",img)
    cv2.imshow("im", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.realese()
cv2.destroyAllWindows

cv2.inR
