import time
import tkinter.filedialog
import cv2
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt, QPoint
from PyQt5.QtGui import QImage, QPixmap, QCursor
from PyQt5.QtWidgets import QWidget, QGraphicsPixmapItem, QGraphicsScene, QGraphicsItem

from UIFile.UIFiles import Ui_MW,Ui_Cam,Ui_MsgBox
from ItemTest import myScene,myItem,myMask
import MethodSet
#提示界面
class MsgBox(QWidget):
    def __init__(self,msg):
        super(MsgBox,self).__init__()
        self.ui=Ui_MsgBox()
        self.ui.setupUi(self)
        self.ui.msgLabel.setText(msg)
        #必须调用，父控件调用或自己调用都可
        self.show()

    @pyqtSlot()
    def on_okBtn_clicked(self):
        #pass
        self.close()

#摄像机界面
class Cam(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.CamUI=Ui_Cam()
        self.CamUI.setupUi(self)
        self.flag=True
        self.show()
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.CamUI.showlabel.setScaledContents(True)
        #self.photographing()



    #将cv2返回的数组转为图片
    def toImage(self, img,wid,hei):
        width = img.shape[1]
        height = img.shape[0]
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        qt_img = QtGui.QImage(img.data, width, height, QtGui.QImage.Format_RGB888)
        n_width = qt_img.width()
        n_height = qt_img.height()
        if n_width / wid >= n_height / hei:
            ratio = n_width / wid
        else:
            ratio = n_height / hei
        new_width = n_width / ratio
        new_height = n_height / ratio
        new_img = qt_img.scaled(new_width, new_height, QtCore.Qt.KeepAspectRatio)
        #self.label.setScaledContents(True)
        return QtGui.QPixmap.fromImage(new_img)

    def photographing(self):
        wid=self.CamUI.showlabel.width()
        hei=self.CamUI.showlabel.height()
        while(self.flag):
            success, img = self.cap.read()
            if success:
                self.CamUI.showlabel.setPixmap(self.toImage(img,wid,hei))
                cv2.waitKey(10)
        self.cap.release()
        #cv2.destroyAllWindows()
        return img



    @pyqtSlot()
    def on_photographBtn_clicked(self):
        self.flag=False

#主界面
class Mwin(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.MWUI=Ui_MW()
        self.MWUI.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.scene = myScene(self)  # 创建场景
        #界面移动相关
        self.m_flag=False
        #旋转角度
        self.rotateAngle=0
        #缩放因子
        self.scaleFactorH=1
        self.scaleFactorV=1
        #临时图元:
        self.tempItem=None
        #裁剪框大小
        self.cutSx,self.cutSy,self.cutH,self.cutW=0,0,0,0

    #消息提示框
    def createMsgBox(self,str):
        self.mb=MsgBox(str)

    #给场景中添加图元
    def createItem(self,img,name,sc=1.0):
        x = img.shape[1]
        y = img.shape[0]
        pix = QPixmap.fromImage(QImage(img, x, y, QImage.Format_RGB888))
        #t_item = QGraphicsPixmapItem(pix)  # 创建像素图元
        t_item=myItem(pix,name)
        t_item.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        t_item.setScale(sc)
        t_item.setPos(0.0,0.0)
        self.scene.addItem(t_item)
        self.MWUI.graphicsView.setScene(self.scene)  # 将场景添加至视图
        print(t_item.pos())

    #打开按钮：从文件夹选取图片
    @pyqtSlot()
    def on_openBtn_clicked(self):
        root = tkinter.Tk()  # 创建一个Tkinter.Tk()实例
        root.withdraw()  # 将Tkinter.Tk()实例隐藏
        fn = tkinter.filedialog.askopenfilename(title='选择一个文件',
                                                filetypes=[('JPG', '.jpg'), ('PNG', '.png'), ('所有文件', '.*')])
        if fn != "":
            name = (fn.split("/")[-1]).split(".")[0]
            #img=cv2.imread(fn)
            img=cv2.cvtColor(cv2.imread(fn),cv2.COLOR_BGR2RGB)
            self.createItem(img,name)
            # x = img.shape[1]
            # y = img.shape[0]
            # pix = QPixmap.fromImage(QImage(img, x, y, QImage.Format_RGB888))
            # self.srcitem = QGraphicsPixmapItem(pix)  # 创建像素图元
            # self.srcitem.setFlags(QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsSelectable)
            # self.srcitem.setScale(5)
            # self.scene.addItem(self.srcitem)
            # self.MWUI.graphicsView.setScene(self.scene)  # 将场景添加至视图

    #拍照按钮：打开摄像机拍照读取图片
    @pyqtSlot()
    def on_photoBtn_clicked(self):
        self.setEnabled(False)
        cam=Cam()
        img=cam.photographing()
        self.setEnabled(True)
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        t=time.localtime(time.time())
        name="photo-{}{}{}".format(t.tm_hour,t.tm_min,t.tm_sec)
        print(name)
        self.createItem(img,name)

    #删除按钮：删除Scene的图片
    @pyqtSlot()
    def on_deleBtn_clicked(self):
        print("dele")
        print(self.scene.nowItem)
        self.scene.removeItem(self.scene.nowItem)
        if  len(self.scene.items())==0:
            self.MWUI.lineEdit.setText("")

    #保存按钮：保存选中的图片
    @pyqtSlot()
    def on_saveBtn_clicked(self):
        if self.MWUI.lineEdit.text()!="":
            root = tkinter.Tk()
            root.withdraw()
            fn = tkinter.filedialog.asksaveasfilename(filetypes=[('输入文件名+.后缀', '如a.jpg')])
            print(fn)
            if fn.split(".")[0]==fn:
                fn+="jpg"
                self.mb=MsgBox("未输入格式名，已默认保存为.jpg格式")
            self.scene.nowItem.pixmap().save(str(fn))
        else :
            #必须加上self.不然窗口会闪退
            self.mb=MsgBox("请先选择一张图片!")

    #拷贝按钮：拷贝选中的图片
    @pyqtSlot()
    def on_copyBtn_clicked(self):
        if self.MWUI.lineEdit.text()!="":
            name=self.scene.nowItem.name+"_copy"
            copyItem=myItem(self.scene.nowItem.pixmap(),name)
            copyItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(copyItem)
        else:
            self.mb=MsgBox("请先选择一张图片")

    #清空按钮：清空场景的所有图片
    @pyqtSlot()
    def on_cleanBtn_clicked(self):
        self.scene=myScene(self)
        self.MWUI.graphicsView.setScene(self.scene)
        self.MWUI.lineEdit.setText("")
        print("clean")

    #关闭按钮：关闭系统
    @pyqtSlot()
    def on_closeBtn_clicked(self):
        self.close()

    #最小化按钮：使系统最小化
    @pyqtSlot()
    def on_miniBtn_clicked(self):
        self.showMinimized()

    #旋转角度:使图片旋转
    @pyqtSlot(int)
    def on_rotateSlider_valueChanged(self,p_int):
        self.MWUI.rotatelabel.setText(str(p_int) + "°")
        self.rotateAngle = p_int

    #垂直缩放因子
    @pyqtSlot(int)
    def on_scaleSliderV_valueChanged(self,p_int):
        self.scaleFactorV=(float)(p_int/10)
        self.MWUI.scalelabelV.setText(str(self.scaleFactorV))

    #水平缩放因子
    @pyqtSlot(int)
    def on_scaleSliderH_valueChanged(self, p_int):
        self.scaleFactorH = (float)(p_int / 10)
        self.MWUI.scalelabelH.setText(str(self.scaleFactorH))

    #几何变换应用按钮
    @pyqtSlot()
    def on_applyBtn_clicked(self):
        pix = self.scene.nowItem
        if pix!=None:
            pix = self.scene.nowItem.pixmap()
            pix=MethodSet.rotate(pix,self.rotateAngle)#传入和返回值都是QPixmap类型
            if self.scaleFactorV!=1 or self.scaleFactorH!=1:
                pix.save("temp.jpg")
                pix = cv2.imread("temp.jpg")
                pix = MethodSet.scale(pix, self.scaleFactorV, self.scaleFactorH)  # 传入和返回值都是narray类型
                pix=cv2.cvtColor(pix,cv2.COLOR_BGR2RGB)
                pix = QPixmap.fromImage(
                    QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            if self.MWUI.checkBox.isChecked():
                pix=MethodSet.MinBox(pix)
                pix =cv2.cvtColor(pix,cv2.COLOR_BGR2RGB)
                pix = QPixmap.fromImage(
                    QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.scene.nowItem.setPixmap(pix)
        else :
            self.mb=MsgBox("请先选择一张图片！")

    #水平镜像按钮
    @pyqtSlot()
    def on_hMirrorBtn_clicked(self):
        if self.MWUI.lineEdit.text()!="":
            pix=self.scene.nowItem.pixmap()
            pix=MethodSet.HMirror(pix)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.scene.nowItem.setPixmap(pix)
        else:
            self.mb=MsgBox("请先选择一张图片")

    #垂直镜像按钮
    @pyqtSlot()
    def on_vMirrorBtn_clicked(self):
        if self.MWUI.lineEdit.text()!="":
            pix=self.scene.nowItem.pixmap()
            pix=MethodSet.VMirror(pix)
            pix=cv2.cvtColor(pix,cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.scene.nowItem.setPixmap(pix)
        else:
            self.mb=MsgBox("请先选择一张图片")

    #几何变换框
    @pyqtSlot(bool)
    def on_GP_transorm_toggled(self,flag):
        #self.MWUI.GP_transform.setChecked(True)
        self.MWUI.GP_imgCut.setChecked(False)
        self.MWUI.GP_mirrorChange.setChecked(True)

    #镜像变换框
    @pyqtSlot(bool)
    def on_GP_mirrorChange_toggled(self, flag):
        #self.MWUI.GP_mirrorChange.setChecked(True)
        self.MWUI.GP_imgCut.setChecked(False)
        self.MWUI.GP_transform.setChecked(True)

    #裁剪变换框
    @pyqtSlot(bool)
    def on_GP_imgCut_toggled(self,flag):
        if self.scene.nowItem!="":
            print(self.scene.nowItem.scenePos(),self.scene.nowItem.scenePos().y(),self.scene.nowItem.scenePos().x(),"hera")
            self.MWUI.GP_transform.setChecked(False)
            self.MWUI.GP_mirrorChange.setChecked(False)

    #裁剪按钮
    def on_cutBtn_clicked(self):
        if self.scene.nowItem!="":
            pos=self.scene.nowItem.scenePos()
            view_pos = self.MWUI.graphicsView.mapFromScene(pos)
            screen_pos = self.MWUI.graphicsView.mapToGlobal(view_pos)
            pix=self.scene.nowItem.pixmap()
            self.mask = myMask(self,screen_pos,pix)

    #裁剪函数
    def cutimg(self):
        if self.scene.nowItem!="":
            pix=self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix=cv2.imread("temp.jpg")
            pix=MethodSet.imgcut(pix,self.cutSx,self.cutSy,self.cutW,self.cutH)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            if self.MWUI.page1_copyBtn.isChecked():
                name = self.scene.nowItem.name + "_cut"
                self.tempItem = myItem(pix, name)
                self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
                self.scene.addItem(self.tempItem)
            elif self.MWUI.page1_changesrcBtn.isChecked():
                self.scene.nowItem.setPixmap(pix)





    #基础调整框
    @pyqtSlot(bool)
    def on_GP_base_toggled(self,flag):
        if self.MWUI.lineEdit.text() != "" and flag:
            name = self.scene.nowItem.name + "_temp"
            self.tempItem = myItem(self.scene.nowItem.pixmap(), name)
            self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(self.tempItem)
            self.V,self.S,self.C,self.H=0,0,0,0
        elif not flag:
            self.tempItem=None
            self.MWUI.GP_base.setChecked(False)
        #elif self.MWUI.lineEdit.text()=="":

        else:
            self.mb = MsgBox("请先选择一张图片")
            self.MWUI.GP_base.setChecked(False)


    #预览图
    def previwofchange(self):
        pix = self.scene.nowItem.pixmap()
        pix = MethodSet.Vchange(pix, self.V)
        pix = MethodSet.Schange(pix,self.S)
        pix = MethodSet.Cchange(pix,self.C)
        pix=MethodSet.Hchange(pix,self.H)
        if self.MWUI.sharpenBox.isChecked():
            idx=self.MWUI.sharpen_comboBox.currentIndex()
            if idx==0:pix=MethodSet.sharpen_Roberts(pix,self.L)
            elif idx==1:pix=MethodSet.sharpen_Prewitt(pix,self.L)
            elif idx==2:pix=MethodSet.sharpen_Sobel(pix,self.L)
            elif idx==3:pix=MethodSet.sharpen_Laplacian(pix,self.L)
        pix = QPixmap.fromImage(
            QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
        self.tempItem.setPixmap(pix)

    # 亮度调整V值
    @pyqtSlot()
    def on_VSlider_sliderReleased(self):
        if self.scene.nowItem != None:
            self.V=self.MWUI.VSlider.value()
            self.MWUI.VlineEdit.setText(str(self.V))
            self.previwofchange()

    # 饱和度调整S值
    @pyqtSlot()
    def on_SSlider_sliderReleased(self):
        if self.scene.nowItem != None:
            self.S = self.MWUI.SSlider.value()
            self.MWUI.SlineEdit.setText(str(self.S))
            self.previwofchange()

    # 对比度调整C值
    @pyqtSlot()
    def on_CSlider_sliderReleased(self):
        if self.scene.nowItem != None:
            self.C = self.MWUI.CSlider.value()
            self.MWUI.ClineEdit.setText(str(self.C))
            self.previwofchange()

    #色相调整H值
    @pyqtSlot()
    def on_HSlider_sliderReleased(self):
        if self.scene.nowItem != None:
            self.H = self.MWUI.HSlider.value()
            self.MWUI.HlineEdit.setText(str(self.H))
            self.previwofchange()

    # 锐化勾选框
    @pyqtSlot(bool)
    def on_sharpenBox_toggled(self,flag):
        self.L=0.05
        self.previwofchange()

    #锐化算子选择框
    @pyqtSlot(str)
    def on_sharpen_comboBox_currentTextChanged(self,p_str):
        self.previwofchange()

    #锐化程度调整L值
    @pyqtSlot()
    def on_LSlider_sliderReleased(self):
        self.L=float(self.MWUI.LSlider.value()/100)
        print(self.L)
        self.MWUI.LlineEdit.setText(str(self.L))
        self.previwofchange()


    #基础调整框确定按钮
    @pyqtSlot()
    def on_baseOk_clicked(self):
        if self.MWUI.page2_copyBtn.isChecked():
            pass
        elif self.MWUI.page2_changesrcBtn.isChecked():
            self.scene.nowItem.setPixmap(self.tempItem.pixmap())
            self.scene.removeItem(self.tempItem)
        self.MWUI.GP_base.setChecked(False)

    #基础调整框取消按钮
    @pyqtSlot()
    def on_baseCancel_clicked(self):
        self.scene.removeItem(self.tempItem)
        self.MWUI.GP_base.setChecked(False)

    #添加噪声框
    @pyqtSlot(bool)
    def on_GP_addNoise_toggled(self,flag):
        if self.MWUI.lineEdit.text() != "" and flag:
            name = self.scene.nowItem.name + "_temp"
            self.tempItem = myItem(self.scene.nowItem.pixmap(), name)
            self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(self.tempItem)
        elif not flag:
            self.tempItem=None
            self.MWUI.GP_addNoise.setChecked(False)
        else:
            self.mb = MsgBox("请先选择一张图片")
            self.MWUI.GP_addNoise.setChecked(False)

    #椒盐噪声snr
    @pyqtSlot()
    def on_SNRSlider_sliderReleased(self):
        if self.scene.nowItem!="":
            v_snr=float(self.MWUI.SNRSlider.value())/100
            print(v_snr)
            self.MWUI.SNRlineEdit.setText(str(v_snr))
            pix=self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix=cv2.imread("temp.jpg")
            pix=MethodSet.noise_SP(pix,v_snr)
            pix=cv2.cvtColor(pix,cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)

    #高斯噪声mu
    @pyqtSlot()
    def on_muSlider_sliderReleased(self):
        if self.scene.nowItem!="":
            mu=self.MWUI.muSlider.value()
            self.MWUI.mulineEdit.setText(str(mu))
            sigma=self.MWUI.sigmaSlider.value()
            self.MWUI.sigmalineEdit.setText(str(sigma))
            pix=self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix=cv2.imread("temp.jpg")
            pix=MethodSet.noise_Gauss(pix,mu,sigma)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix=QPixmap.fromImage(
                QImage(pix,pix.shape[1],pix.shape[0],pix.shape[1]*pix.shape[2],QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)

    #高斯噪声sigma
    @pyqtSlot()
    def on_sigmaSlider_sliderReleased(self):
        if self.scene.nowItem!="":
            mu = self.MWUI.muSlider.value()
            self.MWUI.mulineEdit.setText(str(mu))
            sigma = self.MWUI.sigmaSlider.value()
            self.MWUI.sigmalineEdit.setText(str(sigma))
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            pix = MethodSet.noise_Gauss(pix, mu, sigma)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)


    #随机均匀噪声
    @pyqtSlot()
    def on_rateSlider_sliderReleased(self):
        if self.scene.nowItem!="":
            low = int(self.MWUI.lowlineEdit.text())
            high = int(self.MWUI.highlineEdit.text())
            rate=self.MWUI.rateSlider.value()
            self.MWUI.ratelineEdit.setText(str(rate)+"%")
            rate=float(rate)/100
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            pix = MethodSet.noise_UR(pix,low,high,rate)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)

    #噪声框确定按钮
    @pyqtSlot()
    def on_noiseOk_clicked(self):
        if self.MWUI.page3_copyBtn.isChecked():
            pass
        elif self.MWUI.page3_changesrcBtn.isChecked():
            pix=self.tempItem.pixmap()
            self.scene.nowItem.setPixmap(pix)
            self.scene.removeItem(self.tempItem)
        self.MWUI.GP_addNoise.setChecked(False)

    #噪声框取消按钮
    @pyqtSlot()
    def on_noiseCancel_clicked(self):
        self.scene.removeItem(self.tempItem)
        self.MWUI.GP_addNoise.setChecked(False)

    #均值滤波按钮
    @pyqtSlot()
    def on_meanFilBtn_clicked(self):
        if self.scene.nowItem!="":
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            ks=2*(self.MWUI.kernelSize.currentIndex()+1)+1
            pix = MethodSet.filter_mean(pix, ks)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.scene.nowItem.setPixmap(pix)
        else:
            self.mb=MsgBox("请先选择一张图片")

    #中值滤波按钮
    @pyqtSlot()
    def on_midFilBtn_clicked(self):
        if self.scene.nowItem!="":
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            ks = 2 * (self.MWUI.kernelSize.currentIndex() + 1) + 1
            pix = MethodSet.filter_mid(pix, ks)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.scene.nowItem.setPixmap(pix)
        else:
            self.mb=MsgBox("请先选择一张图片")

    #最大值滤波按钮
    @pyqtSlot()
    def on_maxFilBtn_clicked(self):
        if self.scene.nowItem!="":
            pix = self.scene.nowItem.pixmap()
            pix.save("temp,jpg")
            pix = cv2.imread("temp.jpg")
            ks = 2 * (self.MWUI.kernelSize.currentIndex() + 1) + 1
            pix = MethodSet.filter_max(pix, ks)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.scene.nowItem.setPixmap(pix)
        else:
            self.mb=MsgBox("请先选择一张图片")

    #最小值滤波按钮
    @pyqtSlot()
    def on_minFilBtn_clicked(self):
        if self.scene.nowItem!="":
            pix = self.scene.nowItem.pixmap()
            pix.save("temp,jpg")
            pix = cv2.imread("temp.jpg")
            ks = 2 * (self.MWUI.kernelSize.currentIndex() + 1) + 1
            pix = MethodSet.filter_min(pix, ks)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.scene.nowItem.setPixmap(pix)
        else:
            self.mb=MsgBox("请先选择一张图片")

    #提取轮廓
    @pyqtSlot()
    def on_contourBtn_clicked(self):
        if self.scene.nowItem!="":
            name = self.scene.nowItem.name + "_temp"
            self.tempItem = myItem(self.scene.nowItem.pixmap(), name)
            self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(self.tempItem)
            pix=self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix=cv2.imread("temp.jpg")
            pix=MethodSet.contour_get(pix)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)

    # 浮雕化
    @pyqtSlot()
    def on_cameoBtn_clicked(self):
        if self.scene.nowItem != "":
            name = self.scene.nowItem.name + "_temp"
            self.tempItem = myItem(self.scene.nowItem.pixmap(), name)
            self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(self.tempItem)
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            pix = MethodSet.emboss_get(pix)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)

    #鱼眼效果
    @pyqtSlot()
    def on_fisheyeBtn_clicked(self):
        if self.scene.nowItem != "":
            name = self.scene.nowItem.name + "_temp"
            self.tempItem = myItem(self.scene.nowItem.pixmap(), name)
            self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(self.tempItem)
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            pix = MethodSet.fisheye_get(pix)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)

    # 素描黑白
    @pyqtSlot()
    def on_sketchbkBtn_clicked(self):
        if self.scene.nowItem != "":
            name = self.scene.nowItem.name + "_temp"
            self.tempItem = myItem(self.scene.nowItem.pixmap(), name)
            self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(self.tempItem)
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            pix = MethodSet.sketchbk_get(pix)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)

    # 素描彩色
    @pyqtSlot()
    def on_sketchclBtn_clicked(self):
        if self.scene.nowItem != "":
            name = self.scene.nowItem.name + "_temp"
            self.tempItem = myItem(self.scene.nowItem.pixmap(), name)
            self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(self.tempItem)
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            pix = MethodSet.sketchcl_get(pix)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)

    # 卡通化风格一
    @pyqtSlot()
    def on_cartoon1Btn_clicked(self):
        if self.scene.nowItem != "":
            name = self.scene.nowItem.name + "_temp"
            self.tempItem = myItem(self.scene.nowItem.pixmap(), name)
            self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(self.tempItem)
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            pix = MethodSet.cartoon1_get(pix)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)

    # 卡通化风格二
    @pyqtSlot()
    def on_cartoon2Btn_clicked(self):
        if self.scene.nowItem != "":
            name = self.scene.nowItem.name + "_temp"
            self.tempItem = myItem(self.scene.nowItem.pixmap(), name)
            self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(self.tempItem)
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            pix = MethodSet.cartoon2_get(pix)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)

    # 卡通化风格三
    @pyqtSlot()
    def on_cartoon3Btn_clicked(self):
        if self.scene.nowItem != "":
            name = self.scene.nowItem.name + "_temp"
            self.tempItem = myItem(self.scene.nowItem.pixmap(), name)
            self.tempItem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            self.scene.addItem(self.tempItem)
            pix = self.scene.nowItem.pixmap()
            pix.save("temp.jpg")
            pix = cv2.imread("temp.jpg")
            pix = MethodSet.cartoon3_get(pix)
            pix = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
            pix = QPixmap.fromImage(
                QImage(pix, pix.shape[1], pix.shape[0], pix.shape[1] * pix.shape[2], QImage.Format_RGB888))
            self.tempItem.setPixmap(pix)


    #保证边框去除后窗口可以继续接收鼠标事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))