# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1478, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 731, 131))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 20, 401, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.youngaParameter = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.youngaParameter.sizePolicy().hasHeightForWidth())
        self.youngaParameter.setSizePolicy(sizePolicy)
        self.youngaParameter.setPlaceholderText("")
        self.youngaParameter.setObjectName("youngaParameter")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.youngaParameter)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.poissonParameter = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.poissonParameter.sizePolicy().hasHeightForWidth())
        self.poissonParameter.setSizePolicy(sizePolicy)
        self.poissonParameter.setObjectName("poissonParameter")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.poissonParameter)
        self.verticalLayout_9.addLayout(self.formLayout_5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 20, 321, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.thicknessParameter = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thicknessParameter.sizePolicy().hasHeightForWidth())
        self.thicknessParameter.setSizePolicy(sizePolicy)
        self.thicknessParameter.setObjectName("thicknessParameter")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.thicknessParameter)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.powerValue = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerValue.sizePolicy().hasHeightForWidth())
        self.powerValue.setSizePolicy(sizePolicy)
        self.powerValue.setObjectName("powerValue")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.powerValue)
        self.verticalLayout_8.addLayout(self.formLayout_6)
        self.setupBraketParametersBtn = QtWidgets.QPushButton(self.groupBox)
        self.setupBraketParametersBtn.setGeometry(QtCore.QRect(10, 100, 701, 23))
        self.setupBraketParametersBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setupBraketParametersBtn.setObjectName("setupBraketParametersBtn")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 140, 721, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.meshSizeInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meshSizeInput.sizePolicy().hasHeightForWidth())
        self.meshSizeInput.setSizePolicy(sizePolicy)
        self.meshSizeInput.setObjectName("meshSizeInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.meshSizeInput)
        self.meshGenerateBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meshGenerateBtn.sizePolicy().hasHeightForWidth())
        self.meshGenerateBtn.setSizePolicy(sizePolicy)
        self.meshGenerateBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.meshGenerateBtn.setObjectName("meshGenerateBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.meshGenerateBtn)
        self.fixParametersBox = QtWidgets.QGroupBox(self.centralwidget)
        self.fixParametersBox.setGeometry(QtCore.QRect(20, 210, 721, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixParametersBox.sizePolicy().hasHeightForWidth())
        self.fixParametersBox.setSizePolicy(sizePolicy)
        self.fixParametersBox.setObjectName("fixParametersBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fixParametersBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.fixParametersBox)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 699, 266))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.fixParametersBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixParametersBox_2.sizePolicy().hasHeightForWidth())
        self.fixParametersBox_2.setSizePolicy(sizePolicy)
        self.fixParametersBox_2.setObjectName("fixParametersBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fixParametersBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.fixTypeBox = QtWidgets.QComboBox(self.fixParametersBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixTypeBox.sizePolicy().hasHeightForWidth())
        self.fixTypeBox.setSizePolicy(sizePolicy)
        self.fixTypeBox.setObjectName("fixTypeBox")
        self.fixTypeBox.addItem("")
        self.fixTypeBox.addItem("")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fixTypeBox)
        self.label_6 = QtWidgets.QLabel(self.fixParametersBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.fixNodeBoxes = QtWidgets.QHBoxLayout()
        self.fixNodeBoxes.setObjectName("fixNodeBoxes")
        self.bottomFixNodeCheckBox = QtWidgets.QCheckBox(self.fixParametersBox_2)
        self.bottomFixNodeCheckBox.setObjectName("bottomFixNodeCheckBox")
        self.fixNodeBoxes.addWidget(self.bottomFixNodeCheckBox)
        self.leftFixNodeCheckBox = QtWidgets.QCheckBox(self.fixParametersBox_2)
        self.leftFixNodeCheckBox.setObjectName("leftFixNodeCheckBox")
        self.fixNodeBoxes.addWidget(self.leftFixNodeCheckBox)
        self.rightFixNodeCheckBox = QtWidgets.QCheckBox(self.fixParametersBox_2)
        self.rightFixNodeCheckBox.setObjectName("rightFixNodeCheckBox")
        self.fixNodeBoxes.addWidget(self.rightFixNodeCheckBox)
        self.formLayout_7.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.fixNodeBoxes)
        self.label_7 = QtWidgets.QLabel(self.fixParametersBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.fixEdgeBoxes = QtWidgets.QHBoxLayout()
        self.fixEdgeBoxes.setObjectName("fixEdgeBoxes")
        self.edgeLeftFixCheckBox = QtWidgets.QCheckBox(self.fixParametersBox_2)
        self.edgeLeftFixCheckBox.setEnabled(False)
        self.edgeLeftFixCheckBox.setCheckable(False)
        self.edgeLeftFixCheckBox.setObjectName("edgeLeftFixCheckBox")
        self.fixEdgeBoxes.addWidget(self.edgeLeftFixCheckBox)
        self.edgeRightFixCheckBox = QtWidgets.QCheckBox(self.fixParametersBox_2)
        self.edgeRightFixCheckBox.setEnabled(False)
        self.edgeRightFixCheckBox.setCheckable(False)
        self.edgeRightFixCheckBox.setObjectName("edgeRightFixCheckBox")
        self.fixEdgeBoxes.addWidget(self.edgeRightFixCheckBox)
        self.edgeDiagonalFixCheckBox = QtWidgets.QCheckBox(self.fixParametersBox_2)
        self.edgeDiagonalFixCheckBox.setEnabled(False)
        self.edgeDiagonalFixCheckBox.setCheckable(False)
        self.edgeDiagonalFixCheckBox.setObjectName("edgeDiagonalFixCheckBox")
        self.fixEdgeBoxes.addWidget(self.edgeDiagonalFixCheckBox)
        self.formLayout_7.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.fixEdgeBoxes)
        self.label_5 = QtWidgets.QLabel(self.fixParametersBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_2.addLayout(self.formLayout_7)
        self.gridLayout_3.addWidget(self.fixParametersBox_2, 0, 0, 1, 1)
        self.loadParametersBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.loadParametersBox.setObjectName("loadParametersBox")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.loadParametersBox)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_8 = QtWidgets.QLabel(self.loadParametersBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.loadParametersBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.loadParametersBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.loadTypeBox = QtWidgets.QComboBox(self.loadParametersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadTypeBox.sizePolicy().hasHeightForWidth())
        self.loadTypeBox.setSizePolicy(sizePolicy)
        self.loadTypeBox.setObjectName("loadTypeBox")
        self.loadTypeBox.addItem("")
        self.loadTypeBox.addItem("")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loadTypeBox)
        self.loadNodeBoxes = QtWidgets.QHBoxLayout()
        self.loadNodeBoxes.setObjectName("loadNodeBoxes")
        self.bottomLoadNodeCheckBox = QtWidgets.QCheckBox(self.loadParametersBox)
        self.bottomLoadNodeCheckBox.setObjectName("bottomLoadNodeCheckBox")
        self.loadNodeBoxes.addWidget(self.bottomLoadNodeCheckBox)
        self.leftLoadNodeCheckBox = QtWidgets.QCheckBox(self.loadParametersBox)
        self.leftLoadNodeCheckBox.setObjectName("leftLoadNodeCheckBox")
        self.loadNodeBoxes.addWidget(self.leftLoadNodeCheckBox)
        self.rightLoadNodeCheckBox = QtWidgets.QCheckBox(self.loadParametersBox)
        self.rightLoadNodeCheckBox.setObjectName("rightLoadNodeCheckBox")
        self.loadNodeBoxes.addWidget(self.rightLoadNodeCheckBox)
        self.formLayout_8.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.loadNodeBoxes)
        self.loadEdgeBoxes = QtWidgets.QHBoxLayout()
        self.loadEdgeBoxes.setObjectName("loadEdgeBoxes")
        self.edgeLeftLoadCheckBox = QtWidgets.QCheckBox(self.loadParametersBox)
        self.edgeLeftLoadCheckBox.setEnabled(False)
        self.edgeLeftLoadCheckBox.setCheckable(False)
        self.edgeLeftLoadCheckBox.setObjectName("edgeLeftLoadCheckBox")
        self.loadEdgeBoxes.addWidget(self.edgeLeftLoadCheckBox)
        self.edgeRightLoadCheckBox = QtWidgets.QCheckBox(self.loadParametersBox)
        self.edgeRightLoadCheckBox.setEnabled(False)
        self.edgeRightLoadCheckBox.setCheckable(False)
        self.edgeRightLoadCheckBox.setObjectName("edgeRightLoadCheckBox")
        self.loadEdgeBoxes.addWidget(self.edgeRightLoadCheckBox)
        self.edgeDiagonalLoadCheckBox = QtWidgets.QCheckBox(self.loadParametersBox)
        self.edgeDiagonalLoadCheckBox.setEnabled(False)
        self.edgeDiagonalLoadCheckBox.setCheckable(False)
        self.edgeDiagonalLoadCheckBox.setObjectName("edgeDiagonalLoadCheckBox")
        self.loadEdgeBoxes.addWidget(self.edgeDiagonalLoadCheckBox)
        self.formLayout_8.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.loadEdgeBoxes)
        self.verticalLayout_11.addLayout(self.formLayout_8)
        self.gridLayout_3.addWidget(self.loadParametersBox, 1, 0, 1, 1)
        self.setupLFparametersBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.setupLFparametersBtn.setObjectName("setupLFparametersBtn")
        self.gridLayout_3.addWidget(self.setupLFparametersBtn, 2, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout.addWidget(self.scrollArea_3)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(760, 20, 711, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.plotLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)
        self.plotLayout.setObjectName("plotLayout")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(740, 330, 721, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.resultText = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultText.sizePolicy().hasHeightForWidth())
        self.resultText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resultText.setFont(font)
        self.resultText.setObjectName("resultText")
        self.gridLayout_4.addWidget(self.resultText, 0, 1, 1, 1)
        self.bracketParametersText = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bracketParametersText.sizePolicy().hasHeightForWidth())
        self.bracketParametersText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bracketParametersText.setFont(font)
        self.bracketParametersText.setObjectName("bracketParametersText")
        self.gridLayout_4.addWidget(self.bracketParametersText, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1478, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Параметры материала"))
        self.label_2.setText(_translate("MainWindow", "Коэффициент Юнга (Модуль упругости):"))
        self.youngaParameter.setText(_translate("MainWindow", "0.65e5"))
        self.label_3.setText(_translate("MainWindow", "Коэффициент Пуассона (жёсткость):"))
        self.poissonParameter.setText(_translate("MainWindow", "0.25"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Свойства"))
        self.label_4.setText(_translate("MainWindow", "Толщина кронштейна (мм):"))
        self.thicknessParameter.setText(_translate("MainWindow", "4"))
        self.label_11.setText(_translate("MainWindow", "Значение силы (H):"))
        self.powerValue.setText(_translate("MainWindow", "600"))
        self.setupBraketParametersBtn.setText(_translate("MainWindow", "Установить параметры"))
        self.label.setText(_translate("MainWindow", "Размер сетки (мм):"))
        self.meshSizeInput.setText(_translate("MainWindow", "170"))
        self.meshGenerateBtn.setText(_translate("MainWindow", "Сгенерировать сетку и произвести расчёты"))
        self.fixParametersBox.setTitle(_translate("MainWindow", "Закрепления"))
        self.fixParametersBox_2.setTitle(_translate("MainWindow", "Закрепления"))
        self.fixTypeBox.setItemText(0, _translate("MainWindow", "Узел"))
        self.fixTypeBox.setItemText(1, _translate("MainWindow", "Грань"))
        self.label_6.setText(_translate("MainWindow", "Узлы:"))
        self.bottomFixNodeCheckBox.setText(_translate("MainWindow", "[Changed text]"))
        self.leftFixNodeCheckBox.setText(_translate("MainWindow", "[Changed text]"))
        self.rightFixNodeCheckBox.setText(_translate("MainWindow", "[Changed text]"))
        self.label_7.setText(_translate("MainWindow", "Грани:"))
        self.edgeLeftFixCheckBox.setText(_translate("MainWindow", "Слева"))
        self.edgeRightFixCheckBox.setText(_translate("MainWindow", "Справа"))
        self.edgeDiagonalFixCheckBox.setText(_translate("MainWindow", "Диагональ"))
        self.label_5.setText(_translate("MainWindow", "Тип закрепления:"))
        self.loadParametersBox.setTitle(_translate("MainWindow", "Приложенная сила"))
        self.label_8.setText(_translate("MainWindow", "Приложение силы:"))
        self.label_9.setText(_translate("MainWindow", "Узлы:"))
        self.label_10.setText(_translate("MainWindow", "Грани:"))
        self.loadTypeBox.setItemText(0, _translate("MainWindow", "Узел"))
        self.loadTypeBox.setItemText(1, _translate("MainWindow", "Грань"))
        self.bottomLoadNodeCheckBox.setText(_translate("MainWindow", "[Changed text]"))
        self.leftLoadNodeCheckBox.setText(_translate("MainWindow", "[Changed text]"))
        self.rightLoadNodeCheckBox.setText(_translate("MainWindow", "[Changed text]"))
        self.edgeLeftLoadCheckBox.setText(_translate("MainWindow", "Слева"))
        self.edgeRightLoadCheckBox.setText(_translate("MainWindow", "Справа"))
        self.edgeDiagonalLoadCheckBox.setText(_translate("MainWindow", "Диагональ"))
        self.setupLFparametersBtn.setText(_translate("MainWindow", "Задать закрепления и нагрузки"))
        self.resultText.setText(_translate("MainWindow", "TextLabel"))
        self.bracketParametersText.setText(_translate("MainWindow", "Параметры кронштейна не установлены!"))
