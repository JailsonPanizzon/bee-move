import cv2
import numpy as np
import math
from PIL import Image
import time

def crescimento_regiao(cord,im,lim):
    px=im.load()
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
            if(y < im.size[0] and y>=0):
                for j in (-1,0,1):
                    x=j+actual[1]
                    if(x< im.size[1] and x>=0):
                        if(not([y,x] in reg)):
                            distancia_find = math.sqrt((px[x,y]-px[actual[1],actual[0]])**2)
                            #RGB
                            #distancia= math.sqrt((pow((px[y,x][0])-px[actual[0],actual[1]][0],2)+pow((px[y,x][1])-px[actual[0],actual[1]][1],2)+pow((px[y,x][2])-px[actual[0],actual[1]][2],2)))
                            #distancia_find=math.sqrt((pow((px[cord[0],cord[1]][0])-px[actual[0],actual[1]][0],2)+pow((px[cord[0],cord[1]][1])-px[actual[0],actual[1]][1],2)+pow((px[cord[0],cord[1]][2])-px[actual[0],actual[1]][2],2)))
                            if(distancia_find < lim ):
                               reg.append([y,x])

        cont+=1
    return reg

def passaAlta(im):
    im2 = Image.new('L',im.size,255)
    px = im.load()
    limar= 3


    for i in range(1,im2.size[0]-1,1):
        for j in range(1,im2.size[1]-1,1):
            distancia= math.sqrt((px[i-1,j]-px[i,j])**2)
            distanci= math.sqrt((px[i,j-1]-px[i,j])**2)
            if(distancia>limar or distanci>limar):
                if((px[i,j] - 50)< 50):
                    im2.putpixel([i,j],px[i,j]-20)
                else:
                    im2.putpixel([i,j],px[i,j]+40)
            else:
                im2.putpixel([i,j],px[i,j]+20)

    #im2.show()
    return im2
def binaria(im,reg,red,green,blue,val):

    im2 = Image.new('L',im.size,255)
    px = im.load()
    limiar = (red+green+blue)/3
    limiar+= val+(val//2)
    for i in range(1,im2.size[0]-1,1):
        for j in range(1,im2.size[1]-1,1):
            if px[i,j]< limiar and not([j,i] in reg):
                im.putpixel([i,j],255)


    return im
def niveis_de_cinza(im):

    im2 = Image.new('L',im.size,0)
    px = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            media = ((px[i,j][0])+(px[i,j][1])+(px[i,j][2]))//3
            im2.putpixel([i,j],media)
    return im2

def click(event, x, y, flags, param):
    global point
    if event == cv2.EVENT_LBUTTONDBLCLK:
        point = (y,x)
        print(point)
        print("press c to confirm")

def soma_img(im,frame):
    px = im.load()
    h =int(frame.shape[0]-2)
    l= int(frame.shape[1]-2)
    print('h', h)
    print('l',l)

    for i in range(1,h,1):
        for j in range(1,l,1):
            if px[j,i] == 255:
                frame[i][j][0] = 255
                frame[i][j][1] = 255
                frame[i][j][2] = 255

    return frame
def equaliza(img):
    #equaliza imagens nos canais R,G,B
    b, g, r = cv2.split(img)
    red = cv2.equalizeHist(r)
    green = cv2.equalizeHist(g)
    blue = cv2.equalizeHist(b)
    return cv2.merge((blue, green, red))
def diferenca(im1,im2,im3):
    d1 = cv2.absdiff(im1,im2)
    d2 = cv2.absdiff(im2,im3)
    return cv2.bitwise_and(d1,d2)
siz= [380,200]
video = "teste.mp4"
cap = cv2.VideoCapture(video)
im_name = "download (1).jpg"
while True:
    ret,img = cap.read()
    img = img[int(img.shape[0]*0.02):int(img.shape[0]*1),int(img.shape[1]*0.2):int(img.shape[1]*0.85)]
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click)
    while True:
        cv2.imshow("image", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("c"):
            cv2.destroyWindow('image')
            break
    break
cv2.imwrite("p.png",img)
im =Image.open('p.png')
im = niveis_de_cinza(im)
im = passaAlta(im)
im.save("teste.png")
reg = crescimento_regiao(point,im,13)
color = img[point[0],point[1]]
max_blue = color[1]
min_blue = color[1]
max_green = color[2]
min_green = color[2]
max_red = color[0]
min_red = color[0]
min_x = point[0]
max_x=point[0]
min_y=point[1]
max_y=point[1]
for i in reg:
    #im.putpixel((i[1],i[0]),255)
    color = img[i[0],i[1]]
    img[i[0],i[1]] = (0,255,0)
    if max_blue < color[1]:
        max_blue = color[1]
    elif min_blue > color[1]:
        min_blue = color[1]
    if max_green < color[2]:
        max_green = color[2]
    elif min_green > color[2]:
        min_green = color[2]
    if max_red < color[0]:
        max_red = color[0]
    elif min_red > color[0]:
        min_red = color[0]
    if i[0]> max_x:
        max_x = i[0]
    elif i[0]< min_x:
        min_x = i[0]
    if i[1]> max_y:
        max_y = i[1]
    elif i[1]< min_y:
        min_y = i[1]


t_x = max_x-min_x
t_y = max_y-min_y
t_x*=2
t_y*=2
print(t_x, t_y)
im.save("reg.png")
val = 20
im = binaria(im,reg,max_red,max_green,max_blue,val)
im.save('bg.png')
print(int(max_blue),int(max_green),int(max_red))
print(int(min_blue),int(min_green),int(min_red))

kernel = np.ones((5 , 5), np.uint8)
cap = cv2.VideoCapture(video)
im_points = np.ones((img.shape[0], img.shape[1], 3)) * 255

ant = img[point[0],point[1]]
d=0
cont = 0

while (True):
    ret, frame = cap.read()
    frame = frame[int(frame.shape[0]*0.02):int(frame.shape[0]*1),int(frame.shape[1]*0.2):int(frame.shape[1]*0.85)]
    frame =soma_img(im,frame)
    #print(val)
    #val+=1
    rangomax = np.array([int(max_blue)+val,int(max_green)+val,int(max_red)+val])
    rangomin = np.array([int(min_blue)-val,int(min_green)-val,int(min_red)-val])
    mask = cv2.inRange(frame,rangomin,rangomax)
    # reduce the noise
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    x, y, w, h = cv2.boundingRect(opening)
    if x!=0 or y!=0:
        if w < t_x and h<t_y:
            if cont>0:
                cv2.line(im_points,(ant[0],ant[1]),(x+w//2, y + h//2),0)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.imwrite("pontos.png",im_points)
            cv2.imshow('camera', frame)
            d += math.sqrt((ant[0]-x+w//2)**2+(ant[1]-y+h//2)**2)
            ant = (x+w//2, y+h//2)

    cv2.imshow('camera', frame)
    frame_ant = frame
    frame_ant_ant=frame_ant
    cont+=1
    k = cv2.waitKey(1) & 0xFF
    print("Distancia: ",d)
    if k == 27:
        break
