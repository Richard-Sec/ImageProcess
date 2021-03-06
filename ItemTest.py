
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QBitmap, QTransform, QCursor, QPainter, QPen, QBrush
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QWidget


class myItem(QGraphicsPixmapItem):
    def __init__(self,pix,str):
        super().__init__(pix)
        self.name=str


class myScene(QGraphicsScene):
    #将父控件传给子控件，子控件调整父控件的值完成参数传递
    def __init__(self,MW):
        super().__init__()
        self.nowItem=None
        self.parent=MW


    def mousePressEvent(self, event):
       super().mousePressEvent(event)
       if self.parent.MWUI.GP_base.isChecked():
           self.parent.createMsgBox("请不要在调整过程中切换操作对象！")
       elif self.parent.MWUI.GP_addNoise.isChecked():
           self.parent.createMsgBox("请不要在添加噪声过程中切换操作对象！")
       elif self.mouseGrabberItem()!=None:
           self.nowItem = self.mouseGrabberItem()
           self.parent.MWUI.lineEdit.setText(self.nowItem.name)
           print(self.parent)
           print("Scene focusItem changed:", self.nowItem)


class myMask(QWidget):  # 不规则窗体

    """
    证明蒙版的作用，白色显示当前蒙版遮住的界面（不是gui界面，gui界面就是一个蒙版，可以看到蒙版的颜色是黑色，但可以通过设置界面透明度使黑色变成灰色），黑色遮蔽，mask之外的地方透明
    """

    def __init__(self,MW,pos,img):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''background-color:black; ''')
        self.setWindowOpacity(0.5)  #设置透明度
        self.parent=MW
        # self.pix = QBitmap("Images/mask.png")  # 蒙版
        self.pix =QBitmap("Images/mask.png")  # 蒙版
        self.sw=float(img.width())/self.pix.width()
        self.sh=float(img.height())/self.pix.height()
        print(self.pix.size())
        self.pix=self.pix.transformed(QTransform().scale(self.sw, self.sh))
        self.resize(self.pix.size())  # 设置当前GUI主界面和蒙版图片一致
        print(self.pix.size())
        self.move(pos)
        self.spx=5
        self.spy=5
        self.epx=400
        self.epy=100
        self.startPoint=QPoint(0,0)
        self.endPoint=QPoint(0,0)
        self.m_flag=False
        self.show()

        # 保证边框去除后窗口可以继续接收鼠标事件

    #鼠标点击获取裁剪区的起始位置
    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton and event.pos().x()>5 and event.pos().y()>5
                and event.pos().x()<self.pix.width()-5 and event.pos().y()<self.pix.height()-5):
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            self.startPoint = event.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    #拖拽过程不断改变裁剪区的终点，同时不断重绘蒙版
    def mouseMoveEvent(self, QMouseEvent):
        if (Qt.LeftButton and self.m_flag and QMouseEvent.pos().x()>5 and QMouseEvent.pos().y()>5 and
                QMouseEvent.pos().x()<self.pix.width()-5 and QMouseEvent.pos().y()<self.pix.height()-5):
            self.endPoint=QMouseEvent.pos()
            self.pix = QBitmap("Images/mask.png")  # 蒙版
            self.pix = self.pix.transformed(QTransform().scale(self.sw, self.sh))
            self.update()
            self.update()
            QMouseEvent.accept()
    #鼠标松开则返回裁剪区的位置信息，并调用主窗口的裁剪函数
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.parent.cutSx,self.parent.cutSy=self.startPoint.x(),self.startPoint.y()
        self.parent.cutW,self.parent.cutH=self.endPoint.x(),self.endPoint.y()
        self.setCursor(QCursor(Qt.ArrowCursor))
        self.parent.cutimg()
        self.close()

    def paintEvent(self,event):  # 绘制窗口

        pp = QPainter(self.pix)  # 可以想象为给蒙版 pix 添加画手
        pen = QPen(Qt.white, 1)  # 钢笔
        pp.setPen(pen)  # 可以想象为给画手钢笔
        brush = QBrush(Qt.white)  # 画刷，填充钢笔画的区域，填充白色是因为白色可以使蒙版透明
        pp.setBrush(brush)
        # 画一个矩形，【rectangle矩形】
        pp.drawRect(QRect(self.startPoint, self.endPoint))  # 在蒙版mask上画矩形，
        # 在蒙版mask上画矩形，使矩形以内蒙版是白色（可以说是在蒙版之外，使得gui界面透明了），以外蒙版是黑色
        self.setMask(self.pix)  # 把当前整个GUI界面设置为蒙版



