# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_ColorMath.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(785, 202)
        Form.setStyleSheet("font: 10pt \"Arial\";")
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonOpFreq1 = QtWidgets.QPushButton(self.frame_3)
        self.pushButtonOpFreq1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonOpFreq1.setObjectName("pushButtonOpFreq1")
        self.horizontalLayout.addWidget(self.pushButtonOpFreq1)
        self.comboBoxOperations = QtWidgets.QComboBox(self.frame_3)
        self.comboBoxOperations.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxOperations.sizePolicy().hasHeightForWidth())
        self.comboBoxOperations.setSizePolicy(sizePolicy)
        self.comboBoxOperations.setObjectName("comboBoxOperations")
        self.horizontalLayout.addWidget(self.comboBoxOperations)
        self.pushButtonOpFreq2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButtonOpFreq2.setEnabled(False)
        self.pushButtonOpFreq2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonOpFreq2.setObjectName("pushButtonOpFreq2")
        self.horizontalLayout.addWidget(self.pushButtonOpFreq2)
        self.pushButtonOpFreq3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButtonOpFreq3.setEnabled(False)
        self.pushButtonOpFreq3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonOpFreq3.setObjectName("pushButtonOpFreq3")
        self.horizontalLayout.addWidget(self.pushButtonOpFreq3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setEnabled(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_5.addWidget(self.checkBox)
        self.pushButtonDoMath = QtWidgets.QPushButton(self.frame)
        self.pushButtonDoMath.setEnabled(True)
        self.pushButtonDoMath.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonDoMath.setObjectName("pushButtonDoMath")
        self.verticalLayout_5.addWidget(self.pushButtonDoMath)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEditMax = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditMax.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEditMax.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEditMax.setReadOnly(False)
        self.lineEditMax.setObjectName("lineEditMax")
        self.verticalLayout_2.addWidget(self.lineEditMax)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEditMin = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditMin.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEditMin.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEditMin.setReadOnly(False)
        self.lineEditMin.setObjectName("lineEditMin")
        self.verticalLayout.addWidget(self.lineEditMin)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBoxFixed = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxFixed.setEnabled(True)
        self.checkBoxFixed.setChecked(False)
        self.checkBoxFixed.setObjectName("checkBoxFixed")
        self.verticalLayout_8.addWidget(self.checkBoxFixed)
        self.checkBoxCompress = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxCompress.setEnabled(True)
        self.checkBoxCompress.setChecked(False)
        self.checkBoxCompress.setObjectName("checkBoxCompress")
        self.verticalLayout_8.addWidget(self.checkBoxCompress)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 2, 3, 1)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonCondFreq1 = QtWidgets.QPushButton(self.frame_4)
        self.pushButtonCondFreq1.setEnabled(False)
        self.pushButtonCondFreq1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonCondFreq1.setObjectName("pushButtonCondFreq1")
        self.horizontalLayout_2.addWidget(self.pushButtonCondFreq1)
        self.comboBoxCondOps = QtWidgets.QComboBox(self.frame_4)
        self.comboBoxCondOps.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCondOps.sizePolicy().hasHeightForWidth())
        self.comboBoxCondOps.setSizePolicy(sizePolicy)
        self.comboBoxCondOps.setObjectName("comboBoxCondOps")
        self.horizontalLayout_2.addWidget(self.comboBoxCondOps)
        self.pushButtonCondFreq2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButtonCondFreq2.setEnabled(False)
        self.pushButtonCondFreq2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonCondFreq2.setObjectName("pushButtonCondFreq2")
        self.horizontalLayout_2.addWidget(self.pushButtonCondFreq2)
        self.pushButtonCondFreq3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButtonCondFreq3.setEnabled(False)
        self.pushButtonCondFreq3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonCondFreq3.setObjectName("pushButtonCondFreq3")
        self.horizontalLayout_2.addWidget(self.pushButtonCondFreq3)
        self.comboBoxCondInEquality = QtWidgets.QComboBox(self.frame_4)
        self.comboBoxCondInEquality.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCondInEquality.sizePolicy().hasHeightForWidth())
        self.comboBoxCondInEquality.setSizePolicy(sizePolicy)
        self.comboBoxCondInEquality.setObjectName("comboBoxCondInEquality")
        self.horizontalLayout_2.addWidget(self.comboBoxCondInEquality)
        self.spinBoxInEquality = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.spinBoxInEquality.setEnabled(False)
        self.spinBoxInEquality.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBoxInEquality.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxInEquality.setDecimals(5)
        self.spinBoxInEquality.setMinimum(-1000000000000.0)
        self.spinBoxInEquality.setMaximum(1000000000000.0)
        self.spinBoxInEquality.setObjectName("spinBoxInEquality")
        self.horizontalLayout_2.addWidget(self.spinBoxInEquality)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Basic Math"))
        self.pushButtonOpFreq1.setText(_translate("Form", "Freq 1"))
        self.pushButtonOpFreq2.setText(_translate("Form", "Freq 2"))
        self.pushButtonOpFreq3.setText(_translate("Form", "Freq 3"))
        self.checkBox.setText(_translate("Form", "Norm. Intensity"))
        self.pushButtonDoMath.setText(_translate("Form", "Perform Math"))
        self.label.setText(_translate("Form", "Maximum"))
        self.label_2.setText(_translate("Form", "Minimum"))
        self.checkBoxFixed.setText(_translate("Form", "Fixed"))
        self.checkBoxCompress.setText(_translate("Form", "Compress"))
        self.label_4.setText(_translate("Form", "Conditional"))
        self.pushButtonCondFreq1.setText(_translate("Form", "Freq 1"))
        self.pushButtonCondFreq2.setText(_translate("Form", "Freq 2"))
        self.pushButtonCondFreq3.setText(_translate("Form", "Freq 3"))

