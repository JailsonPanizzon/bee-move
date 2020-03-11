

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import math
from PIL import Image
import cv2
from PyQt5.QtGui import QIcon, QPixmap, QImage
import time
from PyQt5.Qt import *
import os.path

global video
global point
global stop
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
        print("press c to confirm")
def soma_img(im,frame):
    px = im.load()
    h =int(frame.shape[0]-2)
    l= int(frame.shape[1]-2)


    for i in range(1,h,1):
        for j in range(1,l,1):
            if px[j,i] == 255:
                frame[i][j][0] = 255
                frame[i][j][1] = 255
                frame[i][j][2] = 255

    return frame

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1185, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1181, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gridLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelNome = QtWidgets.QLabel(self.groupBox_2)
        self.labelNome.setObjectName("labelNome")
        self.gridLayout_3.addWidget(self.labelNome, 0, 0, 1, 1)
        self.carregar = QtWidgets.QPushButton(self.groupBox_2)
        self.carregar.setObjectName("carregar")
        self.gridLayout_3.addWidget(self.carregar, 0, 2, 1, 1)
        self.diretorio = QtWidgets.QLineEdit(self.groupBox_2)
        self.diretorio.setText("")
        self.diretorio.setObjectName("diretorio")
        self.gridLayout_3.addWidget(self.diretorio, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Limiarmascara = QtWidgets.QLineEdit(self.groupBox_2)
        self.Limiarmascara.setText("")
        self.Limiarmascara.setObjectName("Limiarmascara")
        self.gridLayout_2.addWidget(self.Limiarmascara, 3, 1, 1, 1)
        self.labelLimiarmascara = QtWidgets.QLabel(self.groupBox_2)
        self.labelLimiarmascara.setObjectName("labelLimiarmascara")
        self.gridLayout_2.addWidget(self.labelLimiarmascara, 3, 0, 1, 1)
        self.labelAltura = QtWidgets.QLabel(self.groupBox_2)
        self.labelAltura.setObjectName("labelAltura")
        self.gridLayout_2.addWidget(self.labelAltura, 1, 0, 1, 1)
        self.alturavideo = QtWidgets.QLineEdit(self.groupBox_2)
        self.alturavideo.setText("")
        self.alturavideo.setObjectName("alturavideo")
        self.gridLayout_2.addWidget(self.alturavideo, 1, 1, 1, 1)
        self.limiarcor = QtWidgets.QLineEdit(self.groupBox_2)
        self.limiarcor.setText("")
        self.limiarcor.setObjectName("limiarcor")
        self.gridLayout_2.addWidget(self.limiarcor, 2, 1, 1, 1)
        self.labelLimiarcor = QtWidgets.QLabel(self.groupBox_2)
        self.labelLimiarcor.setObjectName("labelLimiarcor")
        self.gridLayout_2.addWidget(self.labelLimiarcor, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.selecionarAelha = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selecionarAelha.sizePolicy().hasHeightForWidth())
        self.selecionarAelha.setSizePolicy(sizePolicy)
        self.selecionarAelha.setObjectName("selecionarAelha")
        self.verticalLayout_2.addWidget(self.selecionarAelha)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.iniciar = QtWidgets.QPushButton(self.groupBox_2)
        self.iniciar.setObjectName("iniciar")
        self.verticalLayout_2.addWidget(self.iniciar)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labeltempcaminhamento = QtWidgets.QLabel(self.groupBox_2)
        self.labeltempcaminhamento.setObjectName("labeltempcaminhamento")
        self.gridLayout_4.addWidget(self.labeltempcaminhamento, 2, 0, 1, 1)
        self.tempoestacionario = QtWidgets.QLabel(self.groupBox_2)
        self.tempoestacionario.setObjectName("tempoestacionario")
        self.gridLayout_4.addWidget(self.tempoestacionario, 8, 1, 1, 1)
        self.labeltempodescanco = QtWidgets.QLabel(self.groupBox_2)
        self.labeltempodescanco.setObjectName("labeltempodescanco")
        self.gridLayout_4.addWidget(self.labeltempodescanco, 7, 0, 1, 1)
        self.labeldistanciapercorrida = QtWidgets.QLabel(self.groupBox_2)
        self.labeldistanciapercorrida.setObjectName("labeldistanciapercorrida")
        self.gridLayout_4.addWidget(self.labeldistanciapercorrida, 0, 0, 1, 1)
        self.labeltempoestacionario = QtWidgets.QLabel(self.groupBox_2)
        self.labeltempoestacionario.setObjectName("labeltempoestacionario")
        self.gridLayout_4.addWidget(self.labeltempoestacionario, 8, 0, 1, 1)
        self.tempodescanco = QtWidgets.QLabel(self.groupBox_2)
        self.tempodescanco.setObjectName("tempodescanco")
        self.gridLayout_4.addWidget(self.tempodescanco, 7, 1, 1, 1)
        self.distaciaPercrrida = QtWidgets.QLabel(self.groupBox_2)
        self.distaciaPercrrida.setObjectName("distaciaPercrrida")
        self.gridLayout_4.addWidget(self.distaciaPercrrida, 0, 1, 1, 1)
        self.velocidademedia = QtWidgets.QLabel(self.groupBox_2)
        self.velocidademedia.setObjectName("velocidademedia")
        self.gridLayout_4.addWidget(self.velocidademedia, 5, 1, 1, 1)
        self.tempocaminhamento = QtWidgets.QLabel(self.groupBox_2)
        self.tempocaminhamento.setObjectName("tempocaminhamento")
        self.gridLayout_4.addWidget(self.tempocaminhamento, 2, 1, 1, 1)
        self.labelvelocidademedia = QtWidgets.QLabel(self.groupBox_2)
        self.labelvelocidademedia.setObjectName("labelvelocidademedia")
        self.gridLayout_4.addWidget(self.labelvelocidademedia, 5, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout.addWidget(self.groupBox_2)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1185, 21))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Configurações"))
        self.labelNome.setText(_translate("MainWindow", "Nome ou diretório do video:"))
        self.carregar.setText(_translate("MainWindow", "Carregar"))
        self.labelLimiarmascara.setText(_translate("MainWindow", "Limiar de mascarade ruidos"))
        self.labelAltura.setText(_translate("MainWindow", "Altura do video"))
        self.labelLimiarcor.setText(_translate("MainWindow", "Limiar de cor"))
        self.selecionarAelha.setText(_translate("MainWindow", "Selecionar abelha"))
        self.iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.labeltempcaminhamento.setText(_translate("MainWindow", "Tempo de caminhamento"))
        self.tempoestacionario.setText(_translate("MainWindow", "0.0"))
        self.labeltempodescanco.setText(_translate("MainWindow", "Tempo de descanço"))
        self.labeldistanciapercorrida.setText(_translate("MainWindow", "Distancia Percorrida"))
        self.labeltempoestacionario.setText(_translate("MainWindow", "Tempo estacionário"))
        self.tempodescanco.setText(_translate("MainWindow", "0.0"))
        self.distaciaPercrrida.setText(_translate("MainWindow", "0.0"))
        self.velocidademedia.setText(_translate("MainWindow", "0.0"))
        self.tempocaminhamento.setText(_translate("MainWindow", "0.0"))
        self.labelvelocidademedia.setText(_translate("MainWindow", "Velocidade média"))
        self.pushButton.setText(_translate("MainWindow", "Parar"))
        self.carregar.clicked.connect(self.carregarvideo)
        self.selecionarAelha.clicked.connect(self.selecionar)
        self.iniciar.clicked.connect(self.avaliar)
        self.selecionarAelha.setDisabled(True)
        self.pushButton.clicked.connect(self.Parar)
        self.iniciar.setDisabled(True)
        self.progressBar.setVisible(False)
    def carregarvideo(self):
        global point
        if (os.path.isfile(self.diretorio.text())):
            ca = carrega_video(self.diretorio.text())
            ret, frame = ca.read()
            frame = frame[int(frame.shape[0]*0.0):int(frame.shape[0]*1),int(frame.shape[1]*0.10):int(frame.shape[1]*0.90)]
            img = frame
            img = cv2.resize(img,(406,280))
            cv2.imwrite("cut.png",img)
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qimg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qimg)
            self.label.setPixmap(pixmap)
            point = (-1,-1)
            self.selecionarAelha.setEnabled(True)
        else:
            print("Diretório não existe")

    def selecionar(self):
        global video, point, t_x, t_y, im, max_blue, min_blue, max_green, min_green, max_red, min_red
        if(self.limiarcor.text() != '' and self.Limiarmascara.text() != '' and self.alturavideo.text() != ''):
            while True:
                ret,frame = video.read()
                frame = frame[int(frame.shape[0]*0.0):int(frame.shape[0]*1),int(frame.shape[1]*0.10):int(frame.shape[1]*0.90)]
                cv2.imwrite("imcut.png",frame)
                img = cv2.imread('imcut.png')
                img = cv2.resize(img,(406,280))
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
            t_x = max_x-min_x
            t_y = max_y-min_y
            t_x*=2
            t_y*=2
            im.save("reg.png")
            val = int(self.Limiarmascara.text())
            t=20
            im = binaria(im,reg,max_red,max_green,max_blue,int(self.Limiarmascara.text()))
            im.save('bg.png')
            cv2.imwrite("imcut.png",img)
            img = cv2.imread('imcut.png')
            img = soma_img(im,img)
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qimg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qimg)
            self.label.setPixmap(pixmap)

            cv2.imwrite('te.png',img)
    
            im.save("reg.png")
            self.iniciar.setEnabled(True)
        else:
            print("Informe todos os valores ")
    def avaliar(self):
        global stop
        if(self.alturavideo.text() == ''):
            self.w = MyPopup()
            self.w.setGeometry(QRect(100, 100, 400, 200))
            self.w.show()
            self.avaliar.setEnabled(False)

        else:
            stop = True
            self.iniciar.setDisabled(True)
            self.pushButton.setEnabled(True)
            self.progressBar.setProperty("value", 0)
            self.progressBar.setVisible(True)
            global video, point, max_blue, min_blue, max_green, min_green, max_red, min_red
            altr = float(self.alturavideo.text())
            kernel = np.ones((5 , 5), np.uint8)
            ret, frame = video.read()
            alti = frame.shape[0]
            proporcao = altr/alti
            frame = frame[int(frame.shape[0]*0.0):int(frame.shape[0]*1),int(frame.shape[1]*0.10):int(frame.shape[1]*0.90)]
            cv2.imwrite("imcut.png",frame)
            frame = cv2.imread('imcut.png')
            frame = cv2.resize(frame,(406,280))
            im_points = np.ones((frame.shape[0], frame.shape[1], 3)) * 255
            val = int(self.limiarcor.text())
            val2 =val
            ant = [point[1],point[0]]
            d=0
            l = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            cont = 5
            inicio = time.time()
            tempocaminhamento = 0
            tempodescanco = 0
            newT = time.time()
            pasta = "Resultados"
            if(not os.path.isdir(pasta)):
                os.mkdir(pasta)
            pasta= pasta + "/" + str(self.diretorio.text())
            if(not os.path.isdir(pasta)):
                os.mkdir(pasta)
            tempoinitial = time.time()
            if(self.limiarcor.text() != ''):
                    val = int(self.limiarcor.text())
            print(l)
            while (cont<(l/2)-5 and stop):
                print(cont)
                ret, frame = video.read()
                frame = frame[int(frame.shape[0]*0.0):int(frame.shape[0]*1),int(frame.shape[1]*0.10):int(frame.shape[1]*0.90)]
                cv2.imwrite("imcut.png",frame)
                frame = cv2.imread('imcut.png')
                frame = cv2.resize(frame,(406,280))
                frame =soma_img(im,frame)
                #frame = cv2.imread(im_name)
                #print(val)
                
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
                                self.tempocaminhamento.setText(str(tempocaminhamento))
                            else:
                                tempodescanco+= tempoAdd
                                self.tempodescanco.setText(str(tempodescanco))
                            newT = time.time()
                            cv2.line(im_points,(ant[0],ant[1]),(x+w//2, y + h//2),0)
                            d += dant
                            self.distaciaPercrrida.setText(str(d*proporcao))
                            fim = time.time()
                            self.velocidademedia.setText(str((d*proporcao)/(fim-inicio)))

                            ant = (x+w//2, y+h//2)
                        cv2.rectangle(frame, (x, y), (x+w, y + h), (0, 255, 0), 3)
                        cv2.imwrite(pasta+"/point_ui.png",im_points)
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qimg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qimg)
                self.label.setPixmap(pixmap)

                #time.sleep(1)
                self.progressBar.setProperty("value", (cont*100)/((l/2)-10))
                cont+=1
                ret, frame = video.read()
                k = cv2.waitKey(1) & 0xFF
                if k == 27:
                    break
            print("ahhhhh")
            tempofinalfinal = time.time() - tempoinitial
            cv2.imwrite(pasta+"/pontos.png", im_points)
            print(tempofinalfinal)
            pixmap = QPixmap(pasta +"/pontos.png")
            self.label.setPixmap(pixmap)
            arquivo = open(pasta+'/resultados.txt', 'w')
            arquivo.write('Distancia Percorrida : '+ self.distaciaPercrrida.text())
            arquivo.write('\nTempo de caminhamento : ' +self.tempocaminhamento.text())
            arquivo.write('\nVelocidade média : ' + self.velocidademedia.text())
            arquivo.write('\nTempo de descanço : ' + self.tempodescanco.text())
            arquivo.write('\nTempo estacionario : ' + self.tempoestacionario.text())
            arquivo.write('\nTempo de processamento : ' + str(tempofinalfinal))
            arquivo.close()
    def Parar(self):
        global stop
        stop = False

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
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


