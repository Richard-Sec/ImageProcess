from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MsgBox(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(354, 200)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.msgLabel = QtWidgets.QLabel(Form)
        self.msgLabel.setScaledContents(False)
        self.msgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.msgLabel.setObjectName("msgLabel")
        self.verticalLayout.addWidget(self.msgLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okBtn = QtWidgets.QPushButton(Form)
        self.okBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ERROR"))
        self.msgLabel.setText(_translate("Form", "提示"))
        self.okBtn.setText(_translate("Form", "好的"))

#gview1475 966 mW 1797 1024
class Ui_MW(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1797, 1024)
        MainWindow.setStyleSheet("QGroupBox{\n"
                                 "    background-color: #f7f6ee;\n"
                                 "    border-radius:5px;\n"
                                 "    border:2px solid #000000;\n"
                                 "    padding:5px;\n"
                                 "    font-family:\'Microsoft YaHei\';\n"
                                 "    font-size:14px;\n"
                                 "    }\n"
                                 "QGroupBox:hover{\n"
                                 "     border:3px solid #385466;\n"
                                 "     }\n"
                                 "QPushButton{\n"
                                 "    border:0px;\n"
                                 "    width:140px;\n"
                                 "    height:30px;\n"
                                 "    border-radius:5px;\n"
                                 "    \n"
                                 "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                 "    }\n"
                                 "\n"
                                 " QPushButton:hover{\n"
                                 "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 #EAEAEA);\n"
                                 " }\n"
                                 " \n"
                                 " QPushButton:pressed{\n"
                                 "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #bdc3c7);\n"
                                 "     }\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.miniBtn = QtWidgets.QPushButton(self.centralwidget)
        self.miniBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.miniBtn.setMaximumSize(QtCore.QSize(93, 16777215))
        self.miniBtn.setStyleSheet("QPushButton{\n"
                                   "    border:1px solid #000000;\n"
                                   "    width:140px;\n"
                                   "    height:30px;\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "    border-radius:2px;\n"
                                   "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #000000, stop:1 #434343);\n"
                                   "    }\n"
                                   "\n"
                                   " QPushButton:hover{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 #EAEAEA);\n"
                                   " }\n"
                                   " \n"
                                   " QPushButton:pressed{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #bdc3c7);\n"
                                   "     }\n"
                                   "\n"
                                   "")
        self.miniBtn.setObjectName("miniBtn")
        self.gridLayout_4.addWidget(self.miniBtn, 0, 0, 1, 1)
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.closeBtn.setMaximumSize(QtCore.QSize(93, 16777215))
        self.closeBtn.setStyleSheet("QPushButton{\n"
                                    "    border:1px solid #000000;\n"
                                    "    width:140px;\n"
                                    "    height:30px;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    border-radius:2px;\n"
                                    "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #000000, stop:1 #434343);\n"
                                    "    }\n"
                                    "\n"
                                    " QPushButton:hover{\n"
                                    "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 #EAEAEA);\n"
                                    " }\n"
                                    " \n"
                                    " QPushButton:pressed{\n"
                                    "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #bdc3c7);\n"
                                    "     }\n"
                                    "\n"
                                    "")
        self.closeBtn.setObjectName("closeBtn")
        self.gridLayout_4.addWidget(self.closeBtn, 0, 1, 1, 1)
        self.helpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.helpBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.helpBtn.setMaximumSize(QtCore.QSize(93, 16777215))
        self.helpBtn.setStyleSheet("QPushButton{\n"
                                   "    border:1px solid #000000;\n"
                                   "    width:140px;\n"
                                   "    height:30px;\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "    border-radius:2px;\n"
                                   "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #000000, stop:1 #434343);\n"
                                   "    }\n"
                                   "\n"
                                   " QPushButton:hover{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 #EAEAEA);\n"
                                   " }\n"
                                   " \n"
                                   " QPushButton:pressed{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #bdc3c7);\n"
                                   "     }\n"
                                   "\n"
                                   "")
        self.helpBtn.setObjectName("helpBtn")
        self.gridLayout_4.addWidget(self.helpBtn, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(295, 16777215))
        self.groupBox.setStyleSheet("QGroupBox{\n"
                                    "    border-radius:5px;\n"
                                    "    border:2px solid #000000;\n"
                                    "    padding:5px;\n"
                                    "    font-family:\'Microsoft YaHei\';\n"
                                    "    font-size:14px;\n"
                                    "    }\n"
                                    "QGroupBox:hover{\n"
                                    "     border:3px solid #385466;\n"
                                    "     }\n"
                                    "")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.openBtn = QtWidgets.QPushButton(self.groupBox)
        self.openBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.openBtn.setStyleSheet("QPushButton{\n"
                                   "    border:0px;\n"
                                   "    width:140px;\n"
                                   "    height:30px;\n"
                                   "    border-radius:5px;\n"
                                   "    color:#FFFFFF;\n"
                                   "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                   "    }\n"
                                   "\n"
                                   " QPushButton:hover{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 #EAEAEA);\n"
                                   " }\n"
                                   " \n"
                                   " QPushButton:pressed{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #bdc3c7);\n"
                                   "     }\n"
                                   "\n"
                                   "")
        self.openBtn.setObjectName("openBtn")
        self.gridLayout.addWidget(self.openBtn, 0, 0, 1, 1)
        self.photoBtn = QtWidgets.QPushButton(self.groupBox)
        self.photoBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.photoBtn.setStyleSheet("QPushButton{\n"
                                    "    border:0px;\n"
                                    "    width:140px;\n"
                                    "    height:30px;\n"
                                    "    border-radius:5px;\n"
                                    "    color:#FFFFFF;\n"
                                    "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                    "    }\n"
                                    "\n"
                                    " QPushButton:hover{\n"
                                    "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 #EAEAEA);\n"
                                    " }\n"
                                    " \n"
                                    " QPushButton:pressed{\n"
                                    "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #bdc3c7);\n"
                                    "     }\n"
                                    "\n"
                                    "")
        self.photoBtn.setObjectName("photoBtn")
        self.gridLayout.addWidget(self.photoBtn, 0, 1, 1, 1)
        self.deleBtn = QtWidgets.QPushButton(self.groupBox)
        self.deleBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.deleBtn.setStyleSheet("QPushButton{\n"
                                   "    border:0px;\n"
                                   "    width:140px;\n"
                                   "    height:30px;\n"
                                   "    border-radius:5px;\n"
                                   "    color:#FFFFFF;\n"
                                   "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                   "    }\n"
                                   "\n"
                                   " QPushButton:hover{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 #EAEAEA);\n"
                                   " }\n"
                                   " \n"
                                   " QPushButton:pressed{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #bdc3c7);\n"
                                   "     }\n"
                                   "\n"
                                   "")
        self.deleBtn.setObjectName("deleBtn")
        self.gridLayout.addWidget(self.deleBtn, 0, 2, 1, 1)
        self.saveBtn = QtWidgets.QPushButton(self.groupBox)
        self.saveBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.saveBtn.setStyleSheet("QPushButton{\n"
                                   "    border:0px;\n"
                                   "    width:140px;\n"
                                   "    height:30px;\n"
                                   "    border-radius:5px;\n"
                                   "    color:#FFFFFF;\n"
                                   "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                   "    }\n"
                                   "\n"
                                   " QPushButton:hover{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 #EAEAEA);\n"
                                   " }\n"
                                   " \n"
                                   " QPushButton:pressed{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #bdc3c7);\n"
                                   "     }\n"
                                   "\n"
                                   "")
        self.saveBtn.setObjectName("saveBtn")
        self.gridLayout.addWidget(self.saveBtn, 0, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.copyBtn = QtWidgets.QPushButton(self.groupBox)
        self.copyBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.copyBtn.setStyleSheet("QPushButton{\n"
                                   "    border:0px;\n"
                                   "    width:140px;\n"
                                   "    height:30px;\n"
                                   "    border-radius:5px;\n"
                                   "    \n"
                                   "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                   "    }\n"
                                   "\n"
                                   " QPushButton:hover{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 #EAEAEA);\n"
                                   " }\n"
                                   " \n"
                                   " QPushButton:pressed{\n"
                                   "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #bdc3c7);\n"
                                   "     }\n"
                                   "\n"
                                   "")
        self.copyBtn.setObjectName("copyBtn")
        self.horizontalLayout.addWidget(self.copyBtn)
        self.cleanBtn = QtWidgets.QPushButton(self.groupBox)
        self.cleanBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.cleanBtn.setStyleSheet("QPushButton{\n"
                                    "    border:0px;\n"
                                    "    width:140px;\n"
                                    "    height:30px;\n"
                                    "    border-radius:5px;\n"
                                    "    \n"
                                    "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                    "    }\n"
                                    "\n"
                                    " QPushButton:hover{\n"
                                    "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 #EAEAEA);\n"
                                    " }\n"
                                    " \n"
                                    " QPushButton:pressed{\n"
                                    "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #bdc3c7);\n"
                                    "     }\n"
                                    "\n"
                                    "")
        self.cleanBtn.setObjectName("cleanBtn")
        self.horizontalLayout.addWidget(self.cleanBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 4)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    border-radius:2px;\n"
                                    "    border:2px solid #000000;\n"
                                    "\n"
                                    "    background-color: #f7f6ee;\n"
                                    "}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 4)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 3)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 577))
        self.tabWidget.setStyleSheet("QTabWidget::pane\n"
                                     "{\n"
                                     "    background-color:#f7f6ee;\n"
                                     "}\n"
                                     "QTabBar::tab{border:1px solid #000000;color:#FFFFFF;height:30;width:73;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);}\n"
                                     "QTabBar::tab:selected{height:30;width:73;background-color: #000000;}\n"
                                     "QTabBar{\n"
                                     "    background-color: #f7f6ee;\n"
                                     "}\n"
                                     "QSlider::handle:horizontal \n"
                                     "{\n"
                                     "    border:5px;\n"
                                     "    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, \n"
                                     "    stop:0.6 rgba(0,0,0), stop:0.778409 rgba(255, 255, 255, 255));\n"
                                     "    width: 10px;\n"
                                     "    margin-top: -3px;\n"
                                     "    margin-bottom: -3px;\n"
                                     "    border-radius: 0px;\n"
                                     "}\n"
                                     "QSlider::sub-page:horizontal {\n"
                                     "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                     "border: 1px solid #4A708B;\n"
                                     "height:1px;\n"
                                     "border-radius: 2px;\n"
                                     "}\n"
                                     "QSlider::groove:horizontal {\n"
                                     "border: 3px solid #ffffff;\n"
                                     "background: #232526;\n"
                                     "height: 5px;\n"
                                     "border-radius: 1px;\n"
                                     "padding-left:-1px;\n"
                                     "padding-right:-1px;\n"
                                     "}\n"
                                     "QLineEdit{\n"
                                     "    border-radius:2px;\n"
                                     "    border:1px solid #000000;\n"
                                     "    background-color: #f7f6ee;\n"
                                     "}\n"
                                     "QComboBox{\n"
                                     "    border:0px solid #000000; \n"
                                     "    color:#FFFFFF; \n"
                                     "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                     "}\n"
                                     "")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(30, 40))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.GP_transform = QtWidgets.QGroupBox(self.tab)
        self.GP_transform.setMinimumSize(QtCore.QSize(0, 400))
        self.GP_transform.setMaximumSize(QtCore.QSize(16777215, 500))
        self.GP_transform.setCheckable(True)
        self.GP_transform.setObjectName("GP_transform")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.GP_transform)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(3, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.moveBox = QtWidgets.QCheckBox(self.GP_transform)
        self.moveBox.setMinimumSize(QtCore.QSize(0, 25))
        self.moveBox.setChecked(True)
        self.moveBox.setObjectName("moveBox")
        self.gridLayout_2.addWidget(self.moveBox, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.GP_transform)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 25))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.GP_transform)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.GP_transform)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.rotateSlider = QtWidgets.QSlider(self.GP_transform)
        self.rotateSlider.setMaximum(360)
        self.rotateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rotateSlider.setObjectName("rotateSlider")
        self.horizontalLayout_2.addWidget(self.rotateSlider)
        self.rotatelabel = QtWidgets.QLabel(self.GP_transform)
        self.rotatelabel.setMinimumSize(QtCore.QSize(40, 0))
        self.rotatelabel.setMaximumSize(QtCore.QSize(40, 16777215))
        self.rotatelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rotatelabel.setObjectName("rotatelabel")
        self.horizontalLayout_2.addWidget(self.rotatelabel)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.GP_transform)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.GP_transform)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.scaleSliderH = QtWidgets.QSlider(self.GP_transform)
        self.scaleSliderH.setMaximum(30)
        self.scaleSliderH.setSingleStep(1)
        self.scaleSliderH.setProperty("value", 10)
        self.scaleSliderH.setOrientation(QtCore.Qt.Horizontal)
        self.scaleSliderH.setObjectName("scaleSliderH")
        self.horizontalLayout_3.addWidget(self.scaleSliderH)
        self.scalelabelH = QtWidgets.QLabel(self.GP_transform)
        self.scalelabelH.setMinimumSize(QtCore.QSize(40, 0))
        self.scalelabelH.setMaximumSize(QtCore.QSize(40, 16777215))
        self.scalelabelH.setAlignment(QtCore.Qt.AlignCenter)
        self.scalelabelH.setObjectName("scalelabelH")
        self.horizontalLayout_3.addWidget(self.scalelabelH)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.GP_transform)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.scaleSliderV = QtWidgets.QSlider(self.GP_transform)
        self.scaleSliderV.setMaximum(30)
        self.scaleSliderV.setSingleStep(1)
        self.scaleSliderV.setProperty("value", 10)
        self.scaleSliderV.setOrientation(QtCore.Qt.Horizontal)
        self.scaleSliderV.setObjectName("scaleSliderV")
        self.horizontalLayout_4.addWidget(self.scaleSliderV)
        self.scalelabelV = QtWidgets.QLabel(self.GP_transform)
        self.scalelabelV.setMinimumSize(QtCore.QSize(40, 0))
        self.scalelabelV.setMaximumSize(QtCore.QSize(40, 16777215))
        self.scalelabelV.setAlignment(QtCore.Qt.AlignCenter)
        self.scalelabelV.setObjectName("scalelabelV")
        self.horizontalLayout_4.addWidget(self.scalelabelV)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 5, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.applyBtn = QtWidgets.QPushButton(self.GP_transform)
        self.applyBtn.setMinimumSize(QtCore.QSize(220, 35))
        self.applyBtn.setObjectName("applyBtn")
        self.horizontalLayout_6.addWidget(self.applyBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 6, 0, 1, 2)
        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.GP_transform, 0, 0, 1, 1)
        self.GP_mirrorChange = QtWidgets.QGroupBox(self.tab)
        self.GP_mirrorChange.setCheckable(True)
        self.GP_mirrorChange.setObjectName("GP_mirrorChange")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.GP_mirrorChange)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.hMirrorBtn = QtWidgets.QPushButton(self.GP_mirrorChange)
        self.hMirrorBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.hMirrorBtn.setObjectName("hMirrorBtn")
        self.gridLayout_7.addWidget(self.hMirrorBtn, 0, 0, 1, 1)
        self.vMirrorBtn = QtWidgets.QPushButton(self.GP_mirrorChange)
        self.vMirrorBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.vMirrorBtn.setObjectName("vMirrorBtn")
        self.gridLayout_7.addWidget(self.vMirrorBtn, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.GP_mirrorChange, 1, 0, 1, 1)
        self.GP_imgCut = QtWidgets.QGroupBox(self.tab)
        self.GP_imgCut.setCheckable(True)
        self.GP_imgCut.setChecked(False)
        self.GP_imgCut.setObjectName("GP_imgCut")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.GP_imgCut)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.page1_changesrcBtn = QtWidgets.QRadioButton(self.GP_imgCut)
        self.page1_changesrcBtn.setMinimumSize(QtCore.QSize(120, 25))
        self.page1_changesrcBtn.setObjectName("page1_changesrcBtn")
        self.gridLayout_6.addWidget(self.page1_changesrcBtn, 0, 0, 1, 1)
        self.page1_copyBtn = QtWidgets.QRadioButton(self.GP_imgCut)
        self.page1_copyBtn.setMinimumSize(QtCore.QSize(120, 25))
        self.page1_copyBtn.setChecked(True)
        self.page1_copyBtn.setObjectName("page1_copyBtn")
        self.gridLayout_6.addWidget(self.page1_copyBtn, 1, 0, 1, 1)
        self.cutBtn = QtWidgets.QPushButton(self.GP_imgCut)
        self.cutBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.cutBtn.setObjectName("cutBtn")
        self.gridLayout_6.addWidget(self.cutBtn, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.GP_imgCut, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.GP_base = QtWidgets.QGroupBox(self.tab_2)
        self.GP_base.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.GP_base.setCheckable(True)
        self.GP_base.setChecked(False)
        self.GP_base.setObjectName("GP_base")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.GP_base)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_9 = QtWidgets.QLabel(self.GP_base)
        self.label_9.setObjectName("label_9")
        self.gridLayout_12.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.GP_base)
        self.label_10.setObjectName("label_10")
        self.gridLayout_12.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.GP_base)
        self.label_11.setObjectName("label_11")
        self.gridLayout_12.addWidget(self.label_11, 12, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.GP_base)
        self.label_23.setObjectName("label_23")
        self.gridLayout_12.addWidget(self.label_23, 8, 0, 1, 1)
        self.baseOk = QtWidgets.QPushButton(self.GP_base)
        self.baseOk.setMinimumSize(QtCore.QSize(0, 30))
        self.baseOk.setObjectName("baseOk")
        self.gridLayout_12.addWidget(self.baseOk, 15, 0, 1, 1)
        self.baseCancel = QtWidgets.QPushButton(self.GP_base)
        self.baseCancel.setMinimumSize(QtCore.QSize(0, 30))
        self.baseCancel.setObjectName("baseCancel")
        self.gridLayout_12.addWidget(self.baseCancel, 15, 1, 1, 1)
        self.page2_copyBtn = QtWidgets.QRadioButton(self.GP_base)
        self.page2_copyBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.page2_copyBtn.setChecked(True)
        self.page2_copyBtn.setObjectName("page2_copyBtn")
        self.gridLayout_12.addWidget(self.page2_copyBtn, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.GP_base)
        self.label_8.setObjectName("label_8")
        self.gridLayout_12.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.GP_base)
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_12.addWidget(self.label_12, 0, 0, 1, 2)
        self.page2_changesrcBtn = QtWidgets.QRadioButton(self.GP_base)
        self.page2_changesrcBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.page2_changesrcBtn.setObjectName("page2_changesrcBtn")
        self.gridLayout_12.addWidget(self.page2_changesrcBtn, 1, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.SSlider = QtWidgets.QSlider(self.GP_base)
        self.SSlider.setMinimum(0)
        self.SSlider.setMaximum(100)
        self.SSlider.setProperty("value", 0)
        self.SSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SSlider.setObjectName("SSlider")
        self.horizontalLayout_8.addWidget(self.SSlider)
        self.SlineEdit = QtWidgets.QLineEdit(self.GP_base)
        self.SlineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.SlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.SlineEdit.setObjectName("SlineEdit")
        self.horizontalLayout_8.addWidget(self.SlineEdit)
        self.gridLayout_12.addLayout(self.horizontalLayout_8, 5, 0, 1, 2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.CSlider = QtWidgets.QSlider(self.GP_base)
        self.CSlider.setOrientation(QtCore.Qt.Horizontal)
        self.CSlider.setObjectName("CSlider")
        self.horizontalLayout_9.addWidget(self.CSlider)
        self.ClineEdit = QtWidgets.QLineEdit(self.GP_base)
        self.ClineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ClineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ClineEdit.setObjectName("ClineEdit")
        self.horizontalLayout_9.addWidget(self.ClineEdit)
        self.gridLayout_12.addLayout(self.horizontalLayout_9, 7, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.VSlider = QtWidgets.QSlider(self.GP_base)
        self.VSlider.setMinimum(1)
        self.VSlider.setMaximum(100)
        self.VSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VSlider.setObjectName("VSlider")
        self.horizontalLayout_7.addWidget(self.VSlider)
        self.VlineEdit = QtWidgets.QLineEdit(self.GP_base)
        self.VlineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.VlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.VlineEdit.setObjectName("VlineEdit")
        self.horizontalLayout_7.addWidget(self.VlineEdit)
        self.gridLayout_12.addLayout(self.horizontalLayout_7, 3, 0, 1, 2)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.HSlider = QtWidgets.QSlider(self.GP_base)
        self.HSlider.setMinimum(0)
        self.HSlider.setMaximum(200)
        self.HSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HSlider.setObjectName("HSlider")
        self.horizontalLayout_17.addWidget(self.HSlider)
        self.HlineEdit = QtWidgets.QLineEdit(self.GP_base)
        self.HlineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.HlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.HlineEdit.setObjectName("HlineEdit")
        self.horizontalLayout_17.addWidget(self.HlineEdit)
        self.gridLayout_12.addLayout(self.horizontalLayout_17, 9, 0, 1, 2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.sharpenBox = QtWidgets.QCheckBox(self.GP_base)
        self.sharpenBox.setObjectName("sharpenBox")
        self.horizontalLayout_11.addWidget(self.sharpenBox)
        self.sharpen_comboBox = QtWidgets.QComboBox(self.GP_base)
        self.sharpen_comboBox.setEnabled(False)
        self.sharpen_comboBox.setMinimumSize(QtCore.QSize(0, 20))
        self.sharpen_comboBox.setStyleSheet("QComboBox{\n"
                                            "    border:0px solid #000000; \n"
                                            "    color:#FFFFFF; \n"
                                            "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                            "}")
        self.sharpen_comboBox.setObjectName("sharpen_comboBox")
        self.sharpen_comboBox.addItem("")
        self.sharpen_comboBox.addItem("")
        self.sharpen_comboBox.addItem("")
        self.sharpen_comboBox.addItem("")
        self.horizontalLayout_11.addWidget(self.sharpen_comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.gridLayout_12.addLayout(self.horizontalLayout_11, 11, 0, 1, 2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.LSlider = QtWidgets.QSlider(self.GP_base)
        self.LSlider.setEnabled(False)
        self.LSlider.setMaximum(50)
        self.LSlider.setProperty("value", 5)
        self.LSlider.setOrientation(QtCore.Qt.Horizontal)
        self.LSlider.setObjectName("LSlider")
        self.horizontalLayout_10.addWidget(self.LSlider)
        self.LlineEdit = QtWidgets.QLineEdit(self.GP_base)
        self.LlineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.LlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.LlineEdit.setObjectName("LlineEdit")
        self.horizontalLayout_10.addWidget(self.LlineEdit)
        self.gridLayout_12.addLayout(self.horizontalLayout_10, 13, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_12.addItem(spacerItem1, 10, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_12.addItem(spacerItem2, 14, 0, 1, 2)
        self.gridLayout_14.addWidget(self.GP_base, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.GP_addNoise = QtWidgets.QGroupBox(self.tab_3)
        self.GP_addNoise.setCheckable(True)
        self.GP_addNoise.setChecked(False)
        self.GP_addNoise.setObjectName("GP_addNoise")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.GP_addNoise)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.page3_copyBtn = QtWidgets.QRadioButton(self.GP_addNoise)
        self.page3_copyBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.page3_copyBtn.setChecked(True)
        self.page3_copyBtn.setObjectName("page3_copyBtn")
        self.gridLayout_13.addWidget(self.page3_copyBtn, 0, 0, 1, 1)
        self.page3_changesrcBtn = QtWidgets.QRadioButton(self.GP_addNoise)
        self.page3_changesrcBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.page3_changesrcBtn.setObjectName("page3_changesrcBtn")
        self.gridLayout_13.addWidget(self.page3_changesrcBtn, 0, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.GP_addNoise)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_13.addWidget(self.line_4, 1, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.GP_addNoise)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_13.setObjectName("label_13")
        self.gridLayout_13.addWidget(self.label_13, 2, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.GP_addNoise)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        self.SNRSlider = QtWidgets.QSlider(self.GP_addNoise)
        self.SNRSlider.setMinimum(1)
        self.SNRSlider.setMaximum(100)
        self.SNRSlider.setProperty("value", 70)
        self.SNRSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SNRSlider.setObjectName("SNRSlider")
        self.horizontalLayout_12.addWidget(self.SNRSlider)
        self.SNRlineEdit = QtWidgets.QLineEdit(self.GP_addNoise)
        self.SNRlineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.SNRlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.SNRlineEdit.setObjectName("SNRlineEdit")
        self.horizontalLayout_12.addWidget(self.SNRlineEdit)
        self.gridLayout_13.addLayout(self.horizontalLayout_12, 3, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.GP_addNoise)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_13.addWidget(self.line_2, 4, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.GP_addNoise)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_14.setObjectName("label_14")
        self.gridLayout_13.addWidget(self.label_14, 5, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.GP_addNoise)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_13.addWidget(self.label_17)
        self.muSlider = QtWidgets.QSlider(self.GP_addNoise)
        self.muSlider.setMinimum(1)
        self.muSlider.setMaximum(100)
        self.muSlider.setProperty("value", 5)
        self.muSlider.setOrientation(QtCore.Qt.Horizontal)
        self.muSlider.setObjectName("muSlider")
        self.horizontalLayout_13.addWidget(self.muSlider)
        self.mulineEdit = QtWidgets.QLineEdit(self.GP_addNoise)
        self.mulineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.mulineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.mulineEdit.setObjectName("mulineEdit")
        self.horizontalLayout_13.addWidget(self.mulineEdit)
        self.gridLayout_13.addLayout(self.horizontalLayout_13, 6, 0, 1, 2)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_18 = QtWidgets.QLabel(self.GP_addNoise)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_14.addWidget(self.label_18)
        self.sigmaSlider = QtWidgets.QSlider(self.GP_addNoise)
        self.sigmaSlider.setMinimum(1)
        self.sigmaSlider.setMaximum(100)
        self.sigmaSlider.setProperty("value", 10)
        self.sigmaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sigmaSlider.setObjectName("sigmaSlider")
        self.horizontalLayout_14.addWidget(self.sigmaSlider)
        self.sigmalineEdit = QtWidgets.QLineEdit(self.GP_addNoise)
        self.sigmalineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sigmalineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.sigmalineEdit.setObjectName("sigmalineEdit")
        self.horizontalLayout_14.addWidget(self.sigmalineEdit)
        self.gridLayout_13.addLayout(self.horizontalLayout_14, 7, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.GP_addNoise)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_13.addWidget(self.line_3, 8, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.GP_addNoise)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_15.setObjectName("label_15")
        self.gridLayout_13.addWidget(self.label_15, 9, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_19 = QtWidgets.QLabel(self.GP_addNoise)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_15.addWidget(self.label_19)
        self.lowlineEdit = QtWidgets.QLineEdit(self.GP_addNoise)
        self.lowlineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lowlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lowlineEdit.setObjectName("lowlineEdit")
        self.horizontalLayout_15.addWidget(self.lowlineEdit)
        self.label_20 = QtWidgets.QLabel(self.GP_addNoise)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_15.addWidget(self.label_20)
        self.highlineEdit = QtWidgets.QLineEdit(self.GP_addNoise)
        self.highlineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.highlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.highlineEdit.setObjectName("highlineEdit")
        self.horizontalLayout_15.addWidget(self.highlineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.gridLayout_13.addLayout(self.horizontalLayout_15, 10, 0, 1, 2)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_21 = QtWidgets.QLabel(self.GP_addNoise)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_16.addWidget(self.label_21)
        self.rateSlider = QtWidgets.QSlider(self.GP_addNoise)
        self.rateSlider.setMinimum(1)
        self.rateSlider.setMaximum(100)
        self.rateSlider.setProperty("value", 30)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setObjectName("rateSlider")
        self.horizontalLayout_16.addWidget(self.rateSlider)
        self.ratelineEdit = QtWidgets.QLineEdit(self.GP_addNoise)
        self.ratelineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ratelineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ratelineEdit.setObjectName("ratelineEdit")
        self.horizontalLayout_16.addWidget(self.ratelineEdit)
        self.gridLayout_13.addLayout(self.horizontalLayout_16, 11, 0, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.GP_addNoise)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_13.addWidget(self.line_5, 12, 0, 1, 2)
        self.noiseOk = QtWidgets.QPushButton(self.GP_addNoise)
        self.noiseOk.setMinimumSize(QtCore.QSize(0, 30))
        self.noiseOk.setObjectName("noiseOk")
        self.gridLayout_13.addWidget(self.noiseOk, 13, 0, 1, 1)
        self.noiseCancel = QtWidgets.QPushButton(self.GP_addNoise)
        self.noiseCancel.setMinimumSize(QtCore.QSize(0, 30))
        self.noiseCancel.setObjectName("noiseCancel")
        self.gridLayout_13.addWidget(self.noiseCancel, 13, 1, 1, 1)
        self.gridLayout_16.addWidget(self.GP_addNoise, 0, 0, 1, 1)
        self.GP_removeNoise = QtWidgets.QGroupBox(self.tab_3)
        self.GP_removeNoise.setCheckable(True)
        self.GP_removeNoise.setChecked(False)
        self.GP_removeNoise.setObjectName("GP_removeNoise")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.GP_removeNoise)
        self.gridLayout_15.setObjectName("gridLayout_15")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem4, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.GP_removeNoise)
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_22.setObjectName("label_22")
        self.gridLayout_15.addWidget(self.label_22, 0, 1, 1, 1)
        self.kernelSize = QtWidgets.QComboBox(self.GP_removeNoise)
        self.kernelSize.setMaximumSize(QtCore.QSize(16777215, 30))
        self.kernelSize.setObjectName("kernelSize")
        self.kernelSize.addItem("")
        self.kernelSize.addItem("")
        self.kernelSize.addItem("")
        self.kernelSize.addItem("")
        self.gridLayout_15.addWidget(self.kernelSize, 0, 2, 1, 2)
        self.maxFilBtn = QtWidgets.QPushButton(self.GP_removeNoise)
        self.maxFilBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.maxFilBtn.setObjectName("maxFilBtn")
        self.gridLayout_15.addWidget(self.maxFilBtn, 4, 0, 1, 4)
        self.meanFilBtn = QtWidgets.QPushButton(self.GP_removeNoise)
        self.meanFilBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.meanFilBtn.setObjectName("meanFilBtn")
        self.gridLayout_15.addWidget(self.meanFilBtn, 1, 0, 1, 4)
        self.midFilBtn = QtWidgets.QPushButton(self.GP_removeNoise)
        self.midFilBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.midFilBtn.setObjectName("midFilBtn")
        self.gridLayout_15.addWidget(self.midFilBtn, 2, 0, 1, 4)
        self.minFilBtn = QtWidgets.QPushButton(self.GP_removeNoise)
        self.minFilBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.minFilBtn.setObjectName("minFilBtn")
        self.gridLayout_15.addWidget(self.minFilBtn, 3, 0, 1, 4)
        self.gridLayout_16.addWidget(self.GP_removeNoise, 1, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.contourBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.contourBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.contourBtn.setObjectName("contourBtn")
        self.verticalLayout_5.addWidget(self.contourBtn)
        self.cameoBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.cameoBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.cameoBtn.setObjectName("cameoBtn")
        self.verticalLayout_5.addWidget(self.cameoBtn)
        self.fisheyeBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.fisheyeBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.fisheyeBtn.setObjectName("fisheyeBtn")
        self.verticalLayout_5.addWidget(self.fisheyeBtn)
        self.gridLayout_18.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sketchbkBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.sketchbkBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.sketchbkBtn.setObjectName("sketchbkBtn")
        self.verticalLayout_4.addWidget(self.sketchbkBtn)
        self.sketchclBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.sketchclBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.sketchclBtn.setObjectName("sketchclBtn")
        self.verticalLayout_4.addWidget(self.sketchclBtn)
        self.gridLayout_18.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cartoon1Btn = QtWidgets.QPushButton(self.groupBox_2)
        self.cartoon1Btn.setMinimumSize(QtCore.QSize(0, 40))
        self.cartoon1Btn.setObjectName("cartoon1Btn")
        self.verticalLayout_3.addWidget(self.cartoon1Btn)
        self.cartoon2Btn = QtWidgets.QPushButton(self.groupBox_2)
        self.cartoon2Btn.setMinimumSize(QtCore.QSize(0, 40))
        self.cartoon2Btn.setObjectName("cartoon2Btn")
        self.verticalLayout_3.addWidget(self.cartoon2Btn)
        self.cartoon3Btn = QtWidgets.QPushButton(self.groupBox_2)
        self.cartoon3Btn.setMinimumSize(QtCore.QSize(0, 40))
        self.cartoon3Btn.setObjectName("cartoon3Btn")
        self.verticalLayout_3.addWidget(self.cartoon3Btn)
        self.gridLayout_18.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_4.addWidget(self.tabWidget, 2, 0, 1, 3)
        self.horizontalLayout_5.addLayout(self.gridLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setStyleSheet("Line{\n"
                                  "  border:2px solid #000000;\n"
                                  "}")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 25))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(1475, 966))
        self.graphicsView.setStyleSheet("QGraphicsView{\n"
                                        "    border:2px solid #000000;\n"
                                        "    border-radius:5px;   \n"
                                        "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #536976, stop:1 #BBD2C5);\n"
                                        "    }\n"
                                        "")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.sharpen_comboBox.setCurrentIndex(0)
        self.sharpenBox.toggled['bool'].connect(self.sharpen_comboBox.setEnabled)
        self.sharpenBox.toggled['bool'].connect(self.LSlider.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.miniBtn.setText(_translate("MainWindow", "最小化"))
        self.closeBtn.setText(_translate("MainWindow", "关闭"))
        self.helpBtn.setText(_translate("MainWindow", "帮助"))
        self.openBtn.setText(_translate("MainWindow", "打开"))
        self.photoBtn.setText(_translate("MainWindow", "拍照"))
        self.deleBtn.setText(_translate("MainWindow", "删除"))
        self.saveBtn.setText(_translate("MainWindow", "保存"))
        self.label.setText(_translate("MainWindow", "当前操作对象："))
        self.copyBtn.setText(_translate("MainWindow", "复制图元"))
        self.cleanBtn.setText(_translate("MainWindow", "清空屏幕"))
        self.GP_transform.setTitle(_translate("MainWindow", "几何变换"))
        self.moveBox.setText(_translate("MainWindow", "允许图像移动"))
        self.checkBox.setText(_translate("MainWindow", "仅保留外接边框"))
        self.label_2.setText(_translate("MainWindow", "旋转角度："))
        self.label_7.setText(_translate("MainWindow", "A:"))
        self.rotatelabel.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "缩放系数："))
        self.label_5.setText(_translate("MainWindow", "H:"))
        self.scalelabelH.setText(_translate("MainWindow", "1.0"))
        self.label_6.setText(_translate("MainWindow", "V:"))
        self.scalelabelV.setText(_translate("MainWindow", "1.0"))
        self.applyBtn.setText(_translate("MainWindow", "应用"))
        self.GP_mirrorChange.setTitle(_translate("MainWindow", "镜像变换"))
        self.hMirrorBtn.setText(_translate("MainWindow", "水平镜像"))
        self.vMirrorBtn.setText(_translate("MainWindow", "垂直镜像"))
        self.GP_imgCut.setTitle(_translate("MainWindow", "图像裁剪"))
        self.page1_changesrcBtn.setText(_translate("MainWindow", "裁剪原图像"))
        self.page1_copyBtn.setText(_translate("MainWindow", "创建副本"))
        self.cutBtn.setText(_translate("MainWindow", "开始裁剪"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "常规"))
        self.GP_base.setTitle(_translate("MainWindow", "基础调整"))
        self.label_9.setText(_translate("MainWindow", "饱和度:"))
        self.label_10.setText(_translate("MainWindow", "对比度:"))
        self.label_11.setText(_translate("MainWindow", "锐化程度:"))
        self.label_23.setText(_translate("MainWindow", "色相:"))
        self.baseOk.setText(_translate("MainWindow", "确定"))
        self.baseCancel.setText(_translate("MainWindow", "取消"))
        self.page2_copyBtn.setText(_translate("MainWindow", "创建副本"))
        self.label_8.setText(_translate("MainWindow", "亮度:"))
        self.label_12.setText(_translate("MainWindow", "[请不要在调整过程中切换操作对象]"))
        self.page2_changesrcBtn.setText(_translate("MainWindow", "修改原图像"))
        self.sharpenBox.setText(_translate("MainWindow", "边缘锐化"))
        self.sharpen_comboBox.setItemText(0, _translate("MainWindow", "Roberts算子"))
        self.sharpen_comboBox.setItemText(1, _translate("MainWindow", "Prewitt算子"))
        self.sharpen_comboBox.setItemText(2, _translate("MainWindow", "Sobel算子"))
        self.sharpen_comboBox.setItemText(3, _translate("MainWindow", "Laplacian算子"))
        self.LlineEdit.setText(_translate("MainWindow", "0.05"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "增强"))
        self.GP_addNoise.setTitle(_translate("MainWindow", "添加噪声"))
        self.page3_copyBtn.setText(_translate("MainWindow", "创建副本"))
        self.page3_changesrcBtn.setText(_translate("MainWindow", "修改原图像"))
        self.label_13.setText(_translate("MainWindow", "椒盐噪声："))
        self.label_16.setText(_translate("MainWindow", "SNR："))
        self.SNRlineEdit.setText(_translate("MainWindow", "0.7"))
        self.label_14.setText(_translate("MainWindow", "高斯噪声："))
        self.label_17.setText(_translate("MainWindow", "mu："))
        self.mulineEdit.setText(_translate("MainWindow", "5"))
        self.label_18.setText(_translate("MainWindow", "sigma："))
        self.sigmalineEdit.setText(_translate("MainWindow", "10"))
        self.label_15.setText(_translate("MainWindow", "均匀随机噪声："))
        self.label_19.setText(_translate("MainWindow", "噪声区间："))
        self.lowlineEdit.setText(_translate("MainWindow", "5"))
        self.label_20.setText(_translate("MainWindow", "-"))
        self.highlineEdit.setText(_translate("MainWindow", "10"))
        self.label_21.setText(_translate("MainWindow", "噪声比例："))
        self.ratelineEdit.setText(_translate("MainWindow", "30%"))
        self.noiseOk.setText(_translate("MainWindow", "确定"))
        self.noiseCancel.setText(_translate("MainWindow", "取消"))
        self.GP_removeNoise.setTitle(_translate("MainWindow", "去除噪声"))
        self.label_22.setText(_translate("MainWindow", "模板大小："))
        self.kernelSize.setItemText(0, _translate("MainWindow", "       [ 3*3 ]"))
        self.kernelSize.setItemText(1, _translate("MainWindow", "       [ 5*5 ]"))
        self.kernelSize.setItemText(2, _translate("MainWindow", "       [ 7*7 ]"))
        self.kernelSize.setItemText(3, _translate("MainWindow", "       [ 9*9 ]"))
        self.maxFilBtn.setText(_translate("MainWindow", "最大值滤波处理"))
        self.meanFilBtn.setText(_translate("MainWindow", "均值滤波处理"))
        self.midFilBtn.setText(_translate("MainWindow", "中值滤波处理"))
        self.minFilBtn.setText(_translate("MainWindow", "最小值滤波处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "噪声"))
        self.groupBox_4.setTitle(_translate("MainWindow", "常用"))
        self.contourBtn.setText(_translate("MainWindow", "轮廓提取"))
        self.cameoBtn.setText(_translate("MainWindow", "浮雕化"))
        self.fisheyeBtn.setText(_translate("MainWindow", "鱼眼效果"))
        self.groupBox_3.setTitle(_translate("MainWindow", "素描化"))
        self.sketchbkBtn.setText(_translate("MainWindow", "黑白"))
        self.sketchclBtn.setText(_translate("MainWindow", "彩铅"))
        self.groupBox_2.setTitle(_translate("MainWindow", "卡通化"))
        self.cartoon1Btn.setText(_translate("MainWindow", "风格一"))
        self.cartoon2Btn.setText(_translate("MainWindow", "风格二"))
        self.cartoon3Btn.setText(_translate("MainWindow", "风格三"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "高级"))
        self.label_4.setText(_translate("MainWindow", "通知栏"))


class Ui_Cam(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 11, 631, 461))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.showlabel = QtWidgets.QLabel(self.widget)
        self.showlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.showlabel.setObjectName("showlabel")
        self.verticalLayout.addWidget(self.showlabel)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.photographBtn = QtWidgets.QPushButton(self.widget)
        self.photographBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.photographBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.photographBtn.setObjectName("photographBtn")
        self.horizontalLayout.addWidget(self.photographBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.showlabel.setText(_translate("Form", "正在打开摄像头，请稍后···"))
        self.label_2.setText(_translate("Form", "准备好后请点击下方拍照按钮进行拍照！"))
        self.photographBtn.setText(_translate("Form", "拍照"))