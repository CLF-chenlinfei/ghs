# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PixivUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(645, 480)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 400, 621, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_path = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_path.setFont(font)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout.addWidget(self.lineEdit_path)
        self.pushButton_fpath = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_fpath.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        self.pushButton_fpath.setFont(font)
        self.pushButton_fpath.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_fpath.setAutoDefault(True)
        self.pushButton_fpath.setObjectName("pushButton_fpath")
        self.horizontalLayout.addWidget(self.pushButton_fpath)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 621, 32))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_gz = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_gz.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        self.pushButton_gz.setFont(font)
        self.pushButton_gz.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_gz.setAutoDefault(True)
        self.pushButton_gz.setObjectName("pushButton_gz")
        self.horizontalLayout_2.addWidget(self.pushButton_gz)
        self.pushButton_hs = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_hs.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        self.pushButton_hs.setFont(font)
        self.pushButton_hs.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_hs.setAutoDefault(True)
        self.pushButton_hs.setObjectName("pushButton_hs")
        self.horizontalLayout_2.addWidget(self.pushButton_hs)
        self.pushButton_ph = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_ph.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        self.pushButton_ph.setFont(font)
        self.pushButton_ph.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_ph.setAutoDefault(True)
        self.pushButton_ph.setObjectName("pushButton_ph")
        self.horizontalLayout_2.addWidget(self.pushButton_ph)
        self.pushButton_xz = QtWidgets.QPushButton(Dialog)
        self.pushButton_xz.setGeometry(QtCore.QRect(210, 440, 201, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        self.pushButton_xz.setFont(font)
        self.pushButton_xz.setObjectName("pushButton_xz")
        self.frame_hsym = QtWidgets.QFrame(Dialog)
        self.frame_hsym.setGeometry(QtCore.QRect(200, 88, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_hsym.setFont(font)
        self.frame_hsym.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_hsym.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_hsym.setObjectName("frame_hsym")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_hsym)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 231, 29))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_hsid = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_hsid.setObjectName("lineEdit_hsid")
        self.horizontalLayout_3.addWidget(self.lineEdit_hsid, 0, QtCore.Qt.AlignLeft)
        self.frame_gzym = QtWidgets.QFrame(Dialog)
        self.frame_gzym.setGeometry(QtCore.QRect(200, 88, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_gzym.setFont(font)
        self.frame_gzym.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gzym.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gzym.setObjectName("frame_gzym")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_gzym)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 231, 36))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEdit_hsid_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_hsid_2.setObjectName("lineEdit_hsid_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_hsid_2)
        self.frame_phym = QtWidgets.QFrame(Dialog)
        self.frame_phym.setEnabled(True)
        self.frame_phym.setGeometry(QtCore.QRect(200, 88, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_phym.setFont(font)
        self.frame_phym.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_phym.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_phym.setObjectName("frame_phym")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame_phym)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 262, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_hsid_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_hsid_3.setObjectName("lineEdit_hsid_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_hsid_3)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 621, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_cook = QtWidgets.QPushButton(Dialog)
        self.pushButton_cook.setGeometry(QtCore.QRect(420, 440, 201, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        self.pushButton_cook.setFont(font)
        self.pushButton_cook.setObjectName("pushButton_cook")
        self.frame_hsym.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.pushButton_xz.raise_()
        self.frame_gzym.raise_()
        self.frame_phym.raise_()
        self.textEdit.raise_()
        self.pushButton_cook.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PixivSpider"))
        self.pushButton_fpath.setText(_translate("Dialog", "文件保存目录"))
        self.pushButton_gz.setText(_translate("Dialog", "xvideos视频下载"))
        self.pushButton_hs.setText(_translate("Dialog", "Pixiv画师下载"))
        self.pushButton_ph.setText(_translate("Dialog", "排行榜下载"))
        self.pushButton_xz.setText(_translate("Dialog", "开始下载"))
        self.label_5.setText(_translate("Dialog", "作者编号："))
        self.label_6.setText(_translate("Dialog", "标签搜索"))
        self.lineEdit_hsid_2.setText(_translate("Dialog", "热舞"))
        self.label_7.setText(_translate("Dialog", "多少天前："))
        self.lineEdit_hsid_3.setText(_translate("Dialog", "10"))
        self.comboBox.setItemText(0, _translate("Dialog", "R-18__"))
        self.comboBox.setItemText(1, _translate("Dialog", "一般__"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_cook.setText(_translate("Dialog", "保存Cookies"))
