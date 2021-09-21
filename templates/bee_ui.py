# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bee.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import math
from PIL import Image
import cv2
from PyQt5.QtGui import QIcon, QPixmap, QImage
import time
from PyQt5.Qt import *

global video
global point
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
    limiar += val*3
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

def carrega_video(name):
    global video
    cap = cv2.VideoCapture(name)
    ret, img = cap.read()
    video = cap
    return cap

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
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1073, 584)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 791, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(809, 9, 241, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(809, 129, 241, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 50, 181, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 30, 23))
        self.label_5.setObjectName("label")
        self.label_55 = QtWidgets.QLabel(self.groupBox_2)
        self.label_55.setGeometry(QtCore.QRect(30, 110, 30, 23))
        self.label_55.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 80, 140, 23))
        self.lineEdit_2.setObjectName("lineEdit")
        self.lineEdit_200 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_200.setGeometry(QtCore.QRect(70, 110, 140, 23))
        self.lineEdit_200.setObjectName("lineEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 140, 231, 81))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 10, 181, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(990, 410, 47, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(830, 340, 221, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(840, 410, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(990, 410, 47, 20))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(840, 440, 111, 16))
        self.label_6.setObjectName("label_5")
        self.vlc = QtWidgets.QLabel(Form)
        self.vlc.setGeometry(QtCore.QRect(990, 440, 47, 13))
        self.vlc.setObjectName("vlc")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(840, 470, 121, 16))
        self.label_7.setObjectName("label_7")
        self.tmpcam = QtWidgets.QLabel(Form)
        self.tmpcam.setGeometry(QtCore.QRect(990, 470, 47, 13))
        self.tmpcam.setObjectName("tmpcam")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(840, 500, 111, 16))
        self.label_9.setObjectName("label_9")
        self.tempdesc = QtWidgets.QLabel(Form)
        self.tempdesc.setGeometry(QtCore.QRect(990, 500, 47, 13))
        self.tempdesc.setObjectName("tempdesc")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(840, 530, 111, 16))
        self.label_11.setObjectName("label_11")
        self.tempestaci = QtWidgets.QLabel(Form)
        self.tempestaci.setGeometry(QtCore.QRect(990, 530, 47, 13))
        self.tempestaci.setObjectName("tempestaci")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(30, 20, 151, 16))
        self.label_12.setObjectName("label_6")
        self.altura = QtWidgets.QLineEdit(self.groupBox_2)
        self.altura.setGeometry(QtCore.QRect(150, 20, 71, 20))
        self.altura.setObjectName("altura")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.groupBox.setTitle(_translate("Form", "Carregar Video"))
        self.label.setText(_translate("Form", "Nome ou diretório do video"))
        self.pushButton.setText(_translate("Form", "Carregar"))
        self.groupBox_2.setTitle(_translate("Form", "Selecionar abelha"))
        self.pushButton_2.setText(_translate("Form", "Selecionar abelha"))
        self.pushButton_3.setText(_translate("Form", "Iniciar"))
        self.pushButton_4.setText(_translate("Form", "Selecionar novamente"))
        self.label_3.setText(_translate("Form", "Distancia percorrida"))
        self.label_4.setText(_translate("Form", "0.0"))
        self.groupBox_2.setTitle(_translate("Form", "GroupBox"))
        self.label_5.setText('limiar')
        self.label_55.setText('limiar video')
        self.label_6.setText('velocidade media')
        self.lineEdit.setText("teste.mp4")
        self.lineEdit_2.setText('40')
        self.lineEdit_200.setText('20')
        self.pushButton.clicked.connect(self.carregarvideo)
        self.pushButton_2.clicked.connect(self.selecionar)
        self.pushButton_3.clicked.connect(self.avaliar)
        self.label_3.setText(_translate("Form", "Distancia percorrida"))
        self.label_4.setText(_translate("Form", "0.0"))
        self.vlc.setText(_translate("Form", "0.0"))
        self.label_7.setText(_translate("Form", "Tempo de caminhamento"))
        self.tmpcam.setText(_translate("Form", "0.0"))
        self.label_9.setText(_translate("Form", "Tempo de descanço"))
        self.tempdesc.setText(_translate("Form", "0.0"))
        self.label_11.setText(_translate("Form", "Tempo estacionario"))
        self.tempestaci.setText(_translate("Form", "0.0"))
        self.label_12.setText(_translate("Form", "Altura da area do video"))
    def carregarvideo(self):
        global point
        ca = carrega_video(self.lineEdit.text())
        ret, img = ca.read()
        img = img[int(img.shape[0]*0.02):int(img.shape[0]*1),int(img.shape[1]*0.2):int(img.shape[1]*0.85)]
        cv2.imwrite("imcut.png",img)
        img = cv2.imread('imcut.png')
        cv2.resize(img,(791,561))
        cv2.imwrite("cut.png",img)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qimg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qimg)
        self.label_2.setPixmap(pixmap)
        point = (-1,-1)
    def selecionar(self):
        global video, point, t_x, t_y, im, max_blue, min_blue, max_green, min_green, max_red, min_red
        while True:
            ret,img = video.read()
            img = img[int(img.shape[0]*0.02):int(img.shape[0]*1),int(img.shape[1]*0.2):int(img.shape[1]*0.85)]
            cv2.imwrite("imcut.png",img)
            img = cv2.imread('imcut.png')
            cv2.resize(img,(791, 561))
            #img = cv2.imread(im_name)
            cv2.namedWindow("De duplo click na abelha e tecle c ")
            cv2.setMouseCallback("De duplo click na abelha e tecle c ", click)
            while True:
                cv2.imshow("De duplo click na abelha e tecle c ", img)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("c"):
                    cv2.destroyWindow('De duplo click na abelha e tecle c ')
                    if(point[0]!= -1 and point[1]!=-1):
                        print("selecionado")

                    break
            break
        cv2.imwrite("p.png", img)
        im =Image.open('p.png')
        im = niveis_de_cinza(im)
        im = passaAlta(im)
        reg = crescimento_regiao(point,im,20)
        color = img[point[0],point[1]]
        max_blue = color[1]
        min_blue = color[1]
        max_green = color[2]
        min_green = color[2]
        max_red = color[0]
        min_red = color[0]
        max_x= point[1]
        max_y= point[0]
        min_x=point[1]
        min_y=point[0]
        for i in reg:
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
            if max_x < i[0]:
                max_x=i[0]
            elif min_x> i[0]:
                min_x=i[0]
            if max_y< i[1]:
                max_y=i[1]
            elif min_y> i[1]:
                min_y=i[1]
        cv2.rectangle(img, (min_x, min_y), ((max_x-min_x),(max_y-min_y)), (0, 255, 0), 3)
        t_x = max_x-min_x
        t_y = max_y-min_y
        t_x*=2
        t_y*=2
        im.save("reg.png")
        val = int(self.lineEdit_2.text())
        t=20
        im = binaria(im,reg,max_red,max_green,max_blue,int(self.lineEdit_2.text()))
        im.save('bg.png')
        cv2.imwrite("imcut.png",img)
        img = cv2.imread('imcut.png')
        img = soma_img(im,img)
        cv2.resize(img,(791, 561))
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qimg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qimg)
        self.label_2.setPixmap(pixmap)

        cv2.imwrite('te.png',img)
        self.label_2
        print(int(max_blue),int(max_green),int(max_red))
        print(int(min_blue),int(min_green),int(min_red))
        im.save("reg.png")

    def avaliar(self):
        if(self.altura.text() == ''):
            self.w = MyPopup()
            self.w.setGeometry(QRect(100, 100, 400, 200))
            self.w.show()
            self.pushButton_2.setEnabled(False)
        else:
            global video, point, max_blue, min_blue, max_green, min_green, max_red, min_red
            altr = float(self.altura.text())
            kernel = np.ones((5 , 5), np.uint8)
            ret, frame = video.read()
            alti = frame.shape[0]
            proporcao = altr/alti
            frame = frame[int(frame.shape[0]*0.02):int(frame.shape[0]*1),int(frame.shape[1]*0.2):int(frame.shape[1]*0.85)]
            cv2.imwrite("imcut.png",frame)
            frame = cv2.imread('imcut.png')
            cv2.resize(frame,(791,561))
            im_points = np.ones((frame.shape[0], frame.shape[1], 3)) * 255
            val = int(self.lineEdit_200.text())
            val2 =val
            ant = frame[point[0],point[1]]
            ant = point
            d=0
            l = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            cont = 5
            inicio = time.time()
            tempocaminhamento = 0
            tempodescanco = 0
            newT = time.time()
            while (cont<l):
                ret, frame = video.read()
                frame = frame[int(frame.shape[0]*0.02):int(frame.shape[0]*1),int(frame.shape[1]*0.2):int(frame.shape[1]*0.85)]
                cv2.imwrite("imcut.png",frame)
                frame = cv2.imread('imcut.png')
                cv2.resize(frame,(791,561))
                frame =soma_img(im,frame)
                #frame = cv2.imread(im_name)
                #print(val)
                #val+=1
                rangomax = np.array([int(max_blue)+val,int(max_green)+val,int(max_red)+val])
                rangomin = np.array([int(min_blue)-val2,int(min_green)-val2,int(min_red)-val2])
                mask = cv2.inRange(frame,rangomin,rangomax)
                opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

                x, y, w, h = cv2.boundingRect(opening)
                if x!=0 or y!=0:
                    if w < t_x and h<t_y:
                        if cont>4:
                            dant = math.sqrt((ant[0]-x+w//2)**2+(ant[1]-y+h//2)**2)
                            tempoAdd = time.time() - newT
                            if(dant>10 or dant>10):
                                tempocaminhamento += tempoAdd
                                self.tmpcam.setText(str(tempocaminhamento))
                            else:
                                tempodescanco+= tempoAdd
                                self.tempdesc.setText(str(tempodescanco))
                            newT = time.time()
                            cv2.line(im_points,(ant[0],ant[1]),(x+w//2, y + h//2),0)
                            d += dant
                            self.label_4.setText(str(d*proporcao))
                            fim = time.time()
                            self.vlc.setText(str((d*proporcao)/(fim-inicio)))

                            ant = (x+w//2, y+h//2)
                        cv2.rectangle(frame, (x, y), (x+w, y + h), (0, 255, 0), 3)
                        cv2.imwrite("point_ui.png",im_points)
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qimg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qimg)
                self.label_2.setPixmap(pixmap)

                #time.sleep(1)
                self.progressBar.setProperty("value", (cont*100)/l)
                cont+=1
                ret, frame = video.read()
                k = cv2.waitKey(1) & 0xFF
                print(d)
                if k == 27:
                    break

            cv2.imwrite(str(self.lineEdit.text())+"_pontos.png",im_points)
            pixmap = QPixmap(str(self.lineEdit.text())+"_pontos.png")
            self.label_2.setPixmap(pixmap)

class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
