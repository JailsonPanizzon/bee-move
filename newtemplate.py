

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

def fix_Ilumination(img1):
    a = np.double(img1)
    b = a + 25
    img2 = np.uint8(b)
    return img2

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
            if(y < im.size[1] and y>=0):
                for j in (-1,0,1):
                    x=j+actual[1]                  
                    if(x< im.size[0] and x>=0):
                        if(not([y,x] in reg)):
                            distancia_find = math.sqrt((px[x,y]-px[actual[1],actual[0]])**2)
                            #distancia= math.sqrt((pow((px[y,x][0])-px[actual[0],actual[1]][0],2)+pow((px[y,x][1])-px[actual[0],actual[1]][1],2)+pow((px[y,x][2])-px[actual[0],actual[1]][2],2)))
                            #distancia_find=math.sqrt((pow((px[cord[0],cord[1]][0])-px[actual[0],actual[1]][0],2)+pow((px[cord[0],cord[1]][1])-px[actual[0],actual[1]][1],2)+pow((px[cord[0],cord[1]][2])-px[actual[0],actual[1]][2],2)))
                            if(distancia_find < lim ):
                               reg.append([y,x])
                            if(len(reg) > (im.size[0]*im.size[1])/20):
                                return reg

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

    limiar = (int(red)+int(green)+int(blue))/12
    limiar += val
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
        self.diretorio.setText("(1).mp4")
        self.diretorio.setObjectName("diretorio")
        self.gridLayout_3.addWidget(self.diretorio, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Limiarmascara = QtWidgets.QLineEdit(self.groupBox_2)
        self.Limiarmascara.setText("100")
        self.Limiarmascara.setObjectName("Limiarmascara")
        self.gridLayout_2.addWidget(self.Limiarmascara, 3, 1, 1, 1)
        self.labelLimiarmascara = QtWidgets.QLabel(self.groupBox_2)
        self.labelLimiarmascara.setObjectName("labelLimiarmascara")
        self.gridLayout_2.addWidget(self.labelLimiarmascara, 3, 0, 1, 1)
        self.labelDuracaoVideo = QtWidgets.QLabel(self.groupBox_2)
        self.labelDuracaoVideo.setObjectName("labelDuracaoVideo")
        self.gridLayout_2.addWidget(self.labelDuracaoVideo, 4, 0, 1, 1)
        self.minDuracao = QtWidgets.QLineEdit(self.groupBox_2)
        self.minDuracao.setText("10")
        self.minDuracao.setObjectName("minDuracao")
        self.gridLayout_2.addWidget(self.minDuracao, 4, 1, 1, 1)
        self.secDuracao = QtWidgets.QLineEdit(self.groupBox_2)
        self.secDuracao.setText("00")
        self.secDuracao.setObjectName("secDuracao")
        self.gridLayout_2.addWidget(self.secDuracao, 4, 2, 1, 1)
        self.gridLayout_2.addWidget(self.labelLimiarmascara, 3, 0, 1, 1)
        self.labelCorSelecao = QtWidgets.QLabel(self.groupBox_2)
        self.labelCorSelecao.setObjectName("labelCorSelecao")
        self.gridLayout_2.addWidget(self.labelCorSelecao, 0, 0, 1, 1)
        self.corSelecaoAbelha = QtWidgets.QLineEdit(self.groupBox_2)
        self.corSelecaoAbelha.setText("20")
        self.corSelecaoAbelha.setObjectName("corSelecaoAbelha")
        self.gridLayout_2.addWidget(self.corSelecaoAbelha, 0, 1, 1, 1)
        self.labelAltura = QtWidgets.QLabel(self.groupBox_2)
        self.labelAltura.setObjectName("labelAltura")
        self.gridLayout_2.addWidget(self.labelAltura, 1, 0, 1, 1)
        self.alturavideo = QtWidgets.QLineEdit(self.groupBox_2)
        self.alturavideo.setText("9")
        self.alturavideo.setObjectName("alturavideo")
        self.gridLayout_2.addWidget(self.alturavideo, 1, 1, 1, 1)
        self.limiarcor = QtWidgets.QLineEdit(self.groupBox_2)
        self.limiarcor.setText("50")
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
        #self.tempoestacionario = QtWidgets.QLabel(self.groupBox_2)
        #self.tempoestacionario.setObjectName("tempoestacionario")
        #self.gridLayout_4.addWidget(self.tempoestacionario, 8, 1, 1, 1)
        self.labeltempodescanco = QtWidgets.QLabel(self.groupBox_2)
        self.labeltempodescanco.setObjectName("labeltempodescanco")
        self.gridLayout_4.addWidget(self.labeltempodescanco, 6, 0, 1, 1)
        self.labeldistanciapercorrida = QtWidgets.QLabel(self.groupBox_2)
        self.labeldistanciapercorrida.setObjectName("labeldistanciapercorrida")
        self.gridLayout_4.addWidget(self.labeldistanciapercorrida, 0, 0, 1, 1)
        #self.labeltempoestacionario = QtWidgets.QLabel(self.groupBox_2)
        #self.labeltempoestacionario.setObjectName("labeltempoestacionario")
        #self.gridLayout_4.addWidget(self.labeltempoestacionario, 8, 0, 1, 1)
        self.tempodescanco = QtWidgets.QLabel(self.groupBox_2)
        self.tempodescanco.setObjectName("tempodescanco")
        self.gridLayout_4.addWidget(self.tempodescanco, 6, 1, 1, 1)
        self.distaciaPercrrida = QtWidgets.QLabel(self.groupBox_2)
        self.distaciaPercrrida.setObjectName("distaciaPercrrida")
        self.gridLayout_4.addWidget(self.distaciaPercrrida, 0, 1, 1, 1)
        self.velocidademedia = QtWidgets.QLabel(self.groupBox_2)
        self.velocidademedia.setObjectName("velocidademedia")
        self.gridLayout_4.addWidget(self.velocidademedia, 1, 1, 1, 1)
        self.tempocaminhamento = QtWidgets.QLabel(self.groupBox_2)
        self.tempocaminhamento.setObjectName("tempocaminhamento")
        self.gridLayout_4.addWidget(self.tempocaminhamento, 2, 1, 1, 1)
        self.tempovideo = QtWidgets.QLabel(self.groupBox_2)
        self.tempovideo.setObjectName("tempovideo")
        self.gridLayout_4.addWidget(self.tempovideo, 7, 1, 1, 1)
        self.labeltempovideo = QtWidgets.QLabel(self.groupBox_2)
        self.labeltempovideo.setObjectName("labeltempovideo")
        self.gridLayout_4.addWidget(self.labeltempovideo, 7, 0, 1, 1)
        self.labelvelocidademedia = QtWidgets.QLabel(self.groupBox_2)
        self.labelvelocidademedia.setObjectName("labelvelocidademedia")
        self.gridLayout_4.addWidget(self.labelvelocidademedia, 1, 0, 1, 1)
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
        self.labelDuracaoVideo.setText(_translate("MainWindow", "Duração do vídeo"))
        self.labelAltura.setText(_translate("MainWindow", "Altura do video"))
        self.labelCorSelecao.setText(_translate("MainWindow", "Limiar de cor de seleção da abelha"))
        self.labelLimiarcor.setText(_translate("MainWindow", "Limiar de cor"))
        self.selecionarAelha.setText(_translate("MainWindow", "Selecionar abelha"))
        self.iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.labeltempcaminhamento.setText(_translate("MainWindow", "Tempo de caminhamento"))
        #self.tempoestacionario.setText(_translate("MainWindow", "0.0"))
        self.labeltempodescanco.setText(_translate("MainWindow", "Tempo de descanço"))
        self.labeldistanciapercorrida.setText(_translate("MainWindow", "Distancia Percorrida"))
        #self.labeltempoestacionario.setText(_translate("MainWindow", "Tempo estacionário"))
        self.labeltempovideo.setText(_translate("MainWindow", "Tempo do video:"))
        self.tempodescanco.setText(_translate("MainWindow", "0.0"))
        self.distaciaPercrrida.setText(_translate("MainWindow", "0.0"))
        self.velocidademedia.setText(_translate("MainWindow", "0.0"))
        self.tempocaminhamento.setText(_translate("MainWindow", "0.0"))
        self.tempovideo.setText(_translate("MainWindow", "0.0"))
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
        global video, point, t_x, t_y, im, max_blue, min_blue, max_green, min_green, max_red, min_red, media_green, media_red, media_blue
        if(self.corSelecaoAbelha.text() != '' and self.limiarcor.text() != '' and self.Limiarmascara.text() != '' and self.alturavideo.text() != '' and self.minDuracao.text() != '' and self.secDuracao.text() != ''):
            while True:
                ret, frame = video.read()
                frame = frame[int(frame.shape[0]*0.0):int(frame.shape[0]*1),int(frame.shape[1]*0.10):int(frame.shape[1]*0.90)]
                frame = fix_Ilumination(frame)
                cv2.imwrite("imcut.png", frame)
                img = cv2.imread('imcut.png')
                img = cv2.resize(img, (406,280))
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
            reg = crescimento_regiao(point, im, int(self.corSelecaoAbelha.text()))
            if len(reg) < 2:
                print("O ponto informado e limiares fornecidos não foram suficientes para demarcar a área da abelha")
            else:
                max_blue = img[point[0], point[1]][1]
                min_blue = img[point[0], point[1]][1]
                max_green = img[point[0], point[1]][2]
                min_green = img[point[0], point[1]][2]
                max_red = img[point[0], point[1]][0]
                min_red = img[point[0], point[1]][0]
                max_x = 0
                max_y = 0
                min_x = 10000000000
                min_y = 10000000000
                soma_red = int(img[point[0], point[1]][0])
                soma_blue = int(img[point[0], point[1]][1])
                soma_green = int(img[point[0], point[1]][2])
                total = 1
                for i in reg:
                    color = img[i[0], i[1]]
                    soma_red += int(color[0])
                    soma_blue += int(color[1])
                    soma_green += int(color[2])
                    total += 1
                    if max_blue < color[1]:
                        max_blue = color[1]
                    if min_blue > color[1] and color[1] > 0:
                        min_blue = color[1]
                    if max_green < color[2]:
                        max_green = color[2]
                    if min_green > color[2] and color[2] > 0:
                        min_green = color[2]
                    if max_red < color[0]:
                        max_red = color[0]
                    if min_red > color[0] and color[0] > 0:
                        min_red = color[0]
                    if max_x < i[0]:
                        max_x = i[0]
                    if min_x > i[0]:
                        min_x = i[0]
                    if max_y < i[1]:
                        max_y = i[1]
                    if min_y > i[1]:
                        min_y = i[1]
                    img[i[0], i[1]] = (0, 255, 0)
                media_green = soma_green / total
                media_red = soma_red / total
                media_blue = soma_blue / total
                t_x = max_x-min_x
                t_y = max_y-min_y
                t_x *= 2
                t_y *= 2
                im.save("reg.png")
                val = int(self.Limiarmascara.text())
                t = 20
                im = binaria(im, reg, max_red, max_green, max_blue, val)
                im.save('bg.png')
                cv2.imwrite("imcut.png", img)
                img = cv2.imread('imcut.png')
                img = soma_img(im, img)
                height, width, channel = img.shape
                bytesPerLine = 3 * width
                qimg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qimg)
                self.label.setPixmap(pixmap)

                cv2.imwrite('te.png', img)
        
                im.save("reg.png")
                time.sleep(1)
                self.iniciar.setEnabled(True)
        else:
            print("Informe todos os valores ")

    def avaliar(self):
        global stop
        stop = True
        tempoReal = (int(self.minDuracao.text()) * 60) + (int(self.secDuracao.text()))
        if self.alturavideo.text() == '' and tempoReal > 10:
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
            kernel = np.ones((5, 5), np.uint8)
            ret, frame = video.read()
            alti = frame.shape[0]
            proporcao = altr/alti
            frame = frame[int(frame.shape[0]*0.0):int(frame.shape[0]*1),int(frame.shape[1]*0.10):int(frame.shape[1]*0.90)]
            cv2.imwrite("imcut.png", frame)
            frame = cv2.imread('imcut.png')
            frame = cv2.resize(frame, (406,280))
            im_points = np.ones((frame.shape[0], frame.shape[1], 3)) * 255
            ant = [point[1], point[0]]
            d = 0
            l = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            cont = 1
            tempocaminhamento = 1
            tempodescanco = 1
            pasta = "Resultados"
            if(not os.path.isdir(pasta)):
                os.mkdir(pasta)
            pasta= pasta + "/" + str(self.diretorio.text())
            if(not os.path.isdir(pasta)):
                os.mkdir(pasta)
            tempoinitial = time.time()
            val = int(self.limiarcor.text())
            max_colors = [245, 245, 245]
            min_colors = [1, 1, 1]
            if media_blue + val < 245:
                max_colors[0] = int(media_blue) + val
            if media_green + val < 245:
                max_colors[1] = int(media_green) + val
            if media_red + val < 245:
                max_colors[2] = int(media_red) + val
            if media_blue - val > 1:
                min_colors[0] = int(media_blue) - val
            if media_green - val > 1:
                min_colors[1] = int(media_green) - val
            if media_red - val > 1:
                min_colors[2] = int(media_red) - val
            rangomax = np.array(max_colors)
            rangomin = np.array(min_colors)
            tempoFrame = tempoReal/l
            passo = 5
            cachetempo = 0
            op = 0
            while(op < passo and ret):
                op += 1
                ret, frame = video.read()
            while (ret and stop):
                frame = frame[int(frame.shape[0]*0.0):int(frame.shape[0]*1),int(frame.shape[1]*0.10):int(frame.shape[1]*0.90)]
                #cv2.imwrite("imcut.png",frame)
                #frame = cv2.imread('imcut.png')
                frame = cv2.resize(frame,(406,280))
                frame = fix_Ilumination(frame)
                frame = soma_img(im,frame)
                mask = cv2.inRange(frame, rangomin, rangomax)
                opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                x, y, w, h = cv2.boundingRect(opening)
                cachetempo += passo
                cv2.rectangle(frame, (x, y), (x+w, y + h), (255, 0, 0), 2)
                if x!= 0 or y != 0:
                    if w < t_x and h < t_y:
                        if cont > 4:
                            dx = ant[0] - (x + (w // 2))
                            dy = ant[1] - (y + (h // 2))
                            dant = math.sqrt((dx ** 2) + (dy ** 2))
                            if(dant > 0.5 * passo):
                                tempocaminhamento += cachetempo
                                cachetempo = 0
                                minvideocam = int((tempocaminhamento * tempoFrame) // 60)
                                secvideocam = int((tempocaminhamento * tempoFrame) % 60)
                                self.tempocaminhamento.setText(str(minvideocam) + ":" + str(secvideocam))
                                d += dant
                                self.distaciaPercrrida.setText(str(d*proporcao))
                            else:
                                tempodescanco += cachetempo
                                cachetempo = 0
                                minvideodesc = int((tempodescanco * tempoFrame) // 60)
                                secvideodesc = int((tempodescanco * tempoFrame) % 60)
                                self.tempodescanco.setText(str(minvideodesc) + ":" + str(secvideodesc))
                            self.velocidademedia.setText(str((d * proporcao) / (tempocaminhamento * tempoFrame)))
                        cv2.line(im_points, (ant[0], ant[1]), (x + (w // 2), y + (h // 2)), 0)
                        ant = [x + (w // 2), y + (h // 2)]
                        cv2.imwrite(pasta+"/point_ui.png", im_points)
                        cv2.rectangle(frame, (x, y), (x+w, y + h), (0, 255, 0), 2)
                        
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qimg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qimg)
                self.label.setPixmap(pixmap)
                cont += passo
                minvideo = int((cont * tempoFrame) // 60)
                secvideo = int((cont * tempoFrame) % 60)
                self.tempovideo.setText(str(minvideo) + ":" + str(secvideo))
                self.progressBar.setProperty("value", (cont*100)/(l-10))
                op = 0
                while(op < passo and ret):
                    op += 1
                    ret, frame = video.read()
                k = cv2.waitKey(1) & 0xFF
                if k == 27:
                    break
            tempofinalfinal = time.time() - tempoinitial
            cv2.imwrite(pasta+"/pontos.png", im_points)
            pixmap = QPixmap(pasta +"/pontos.png")
            self.label.setPixmap(pixmap)

            arquivo = open(pasta+'/resultados.txt', 'w')
            arquivo.write('Distancia Percorrida : ' + self.distaciaPercrrida.text() + '   (um)')
            arquivo.write('\nTempo de caminhamento : ' + self.tempocaminhamento.text() + '   (MM:SS)')
            arquivo.write('\nVelocidade média : ' + self.velocidademedia.text() + '   (um/s)')
            arquivo.write('\nTempo de descanço : ' + self.tempodescanco.text() + '   (MM:SS)')
            arquivo.write('\nTempo de processamento : ' + str(tempofinalfinal) + '   (SS)')
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


