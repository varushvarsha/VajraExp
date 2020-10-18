# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'overlay.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.WindowModal)
        mainWindow.resize(533, 707)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(533, 707))
        mainWindow.setMaximumSize(QtCore.QSize(533, 707))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 550, 491, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sectorLabel = QtWidgets.QLabel(self.layoutWidget)
        self.sectorLabel.setObjectName("sectorLabel")
        self.horizontalLayout.addWidget(self.sectorLabel)
        self.sectorComboBox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectorComboBox.sizePolicy().hasHeightForWidth())
        self.sectorComboBox.setSizePolicy(sizePolicy)
        self.sectorComboBox.setMinimumSize(QtCore.QSize(261, 24))
        self.sectorComboBox.setObjectName("sectorComboBox")
        self.horizontalLayout.addWidget(self.sectorComboBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 491, 64))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fundNameLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.fundNameLabel.setObjectName("fundNameLabel")
        self.horizontalLayout_5.addWidget(self.fundNameLabel)
        self.fundNameComboBox = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fundNameComboBox.sizePolicy().hasHeightForWidth())
        self.fundNameComboBox.setSizePolicy(sizePolicy)
        self.fundNameComboBox.setMinimumSize(QtCore.QSize(291, 24))
        self.fundNameComboBox.setObjectName("fundNameComboBox")
        self.horizontalLayout_5.addWidget(self.fundNameComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.instrumentNameLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.instrumentNameLabel.setObjectName("instrumentNameLabel")
        self.horizontalLayout_4.addWidget(self.instrumentNameLabel)
        self.instrumentNameComboBox = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instrumentNameComboBox.sizePolicy().hasHeightForWidth())
        self.instrumentNameComboBox.setSizePolicy(sizePolicy)
        self.instrumentNameComboBox.setMinimumSize(QtCore.QSize(261, 24))
        self.instrumentNameComboBox.setEditable(False)
        self.instrumentNameComboBox.setObjectName("instrumentNameComboBox")
        self.horizontalLayout_4.addWidget(self.instrumentNameComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 590, 491, 68))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelCurrentStatus = QtWidgets.QLabel(self.layoutWidget2)
        self.labelCurrentStatus.setObjectName("labelCurrentStatus")
        self.horizontalLayout_2.addWidget(self.labelCurrentStatus)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.displayButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.displayButton.setObjectName("displayButton")
        self.horizontalLayout_2.addWidget(self.displayButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.executeButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.executeButton.setObjectName("executeButton")
        self.horizontalLayout_3.addWidget(self.executeButton)
        self.checkBoxEvaluation = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBoxEvaluation.setObjectName("checkBoxEvaluation")
        self.horizontalLayout_3.addWidget(self.checkBoxEvaluation)
        spacerItem1 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButtonClear = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_3.addWidget(self.pushButtonClear)
        self.exitButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_3.addWidget(self.exitButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 93, 491, 284))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.lineEditSharesHeld = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditSharesHeld.setMaximumSize(QtCore.QSize(249, 16777215))
        self.lineEditSharesHeld.setReadOnly(True)
        self.lineEditSharesHeld.setObjectName("lineEditSharesHeld")
        self.horizontalLayout_6.addWidget(self.lineEditSharesHeld)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.lineEditMarketValue = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditMarketValue.setMinimumSize(QtCore.QSize(249, 0))
        self.lineEditMarketValue.setMaximumSize(QtCore.QSize(249, 16777215))
        self.lineEditMarketValue.setReadOnly(True)
        self.lineEditMarketValue.setObjectName("lineEditMarketValue")
        self.horizontalLayout_7.addWidget(self.lineEditMarketValue)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.lineEditPrPerOfPortfolio = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditPrPerOfPortfolio.setMinimumSize(QtCore.QSize(249, 0))
        self.lineEditPrPerOfPortfolio.setMaximumSize(QtCore.QSize(249, 16777215))
        self.lineEditPrPerOfPortfolio.setReadOnly(True)
        self.lineEditPrPerOfPortfolio.setObjectName("lineEditPrPerOfPortfolio")
        self.horizontalLayout_8.addWidget(self.lineEditPrPerOfPortfolio)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.lineEditRanking = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditRanking.setMaximumSize(QtCore.QSize(249, 16777215))
        self.lineEditRanking.setReadOnly(True)
        self.lineEditRanking.setObjectName("lineEditRanking")
        self.horizontalLayout_9.addWidget(self.lineEditRanking)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.lineEditChangeInShares = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditChangeInShares.setMaximumSize(QtCore.QSize(249, 16777215))
        self.lineEditChangeInShares.setReadOnly(True)
        self.lineEditChangeInShares.setObjectName("lineEditChangeInShares")
        self.horizontalLayout_10.addWidget(self.lineEditChangeInShares)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.lineEditPercentageChange = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditPercentageChange.setMaximumSize(QtCore.QSize(249, 16777215))
        self.lineEditPercentageChange.setText("")
        self.lineEditPercentageChange.setReadOnly(True)
        self.lineEditPercentageChange.setObjectName("lineEditPercentageChange")
        self.horizontalLayout_11.addWidget(self.lineEditPercentageChange)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_12.addWidget(self.label_8)
        self.lineEditPerOwnership = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditPerOwnership.setMaximumSize(QtCore.QSize(249, 16777215))
        self.lineEditPerOwnership.setReadOnly(True)
        self.lineEditPerOwnership.setObjectName("lineEditPerOwnership")
        self.horizontalLayout_12.addWidget(self.lineEditPerOwnership)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_13.addWidget(self.label_9)
        self.lineEditQtrFirstOwned = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditQtrFirstOwned.setMaximumSize(QtCore.QSize(249, 16777215))
        self.lineEditQtrFirstOwned.setReadOnly(True)
        self.lineEditQtrFirstOwned.setObjectName("lineEditQtrFirstOwned")
        self.horizontalLayout_13.addWidget(self.lineEditQtrFirstOwned)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 390, 491, 140))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.lineEditSoureType = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditSoureType.setMaximumSize(QtCore.QSize(242, 16777215))
        self.lineEditSoureType.setReadOnly(True)
        self.lineEditSoureType.setObjectName("lineEditSoureType")
        self.horizontalLayout_14.addWidget(self.lineEditSoureType)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_16.addWidget(self.label_7)
        self.lineEditChangeType = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditChangeType.setMaximumSize(QtCore.QSize(242, 16777215))
        self.lineEditChangeType.setReadOnly(True)
        self.lineEditChangeType.setObjectName("lineEditChangeType")
        self.horizontalLayout_16.addWidget(self.lineEditChangeType)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.lineEditSourceData = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditSourceData.setMaximumSize(QtCore.QSize(242, 16777215))
        self.lineEditSourceData.setReadOnly(True)
        self.lineEditSourceData.setObjectName("lineEditSourceData")
        self.horizontalLayout_15.addWidget(self.lineEditSourceData)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_17.addWidget(self.label_12)
        self.lineEditAveragePrice = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditAveragePrice.setMaximumSize(QtCore.QSize(242, 16777215))
        self.lineEditAveragePrice.setReadOnly(True)
        self.lineEditAveragePrice.setObjectName("lineEditAveragePrice")
        self.horizontalLayout_17.addWidget(self.lineEditAveragePrice)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 533, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        mainWindow.setMenuBar(self.menuBar)
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_Fund = QtWidgets.QAction(mainWindow)
        self.actionAdd_Fund.setObjectName("actionAdd_Fund")
        self.actionAboutVajra = QtWidgets.QAction(mainWindow)
        self.actionAboutVajra.setObjectName("actionAboutVajra")
        self.actionExit_2 = QtWidgets.QAction(mainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionAddFundMenu = QtWidgets.QAction(mainWindow)
        self.actionAddFundMenu.setObjectName("actionAddFundMenu")
        self.actionExitMenu = QtWidgets.QAction(mainWindow)
        self.actionExitMenu.setObjectName("actionExitMenu")
        self.actionAboutMenu = QtWidgets.QAction(mainWindow)
        self.actionAboutMenu.setObjectName("actionAboutMenu")
        self.actionAddInstrument = QtWidgets.QAction(mainWindow)
        self.actionAddInstrument.setObjectName("actionAddInstrument")
        self.menuFile.addAction(self.actionAddFundMenu)
        self.menuFile.addAction(self.actionAddInstrument)
        self.menuFile.addAction(self.actionAboutMenu)
        self.menuFile.addAction(self.actionExitMenu)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        self.exitButton.clicked.connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.fundNameComboBox, self.instrumentNameComboBox)
        mainWindow.setTabOrder(self.instrumentNameComboBox, self.sectorComboBox)
        mainWindow.setTabOrder(self.sectorComboBox, self.displayButton)
        mainWindow.setTabOrder(self.displayButton, self.executeButton)
        mainWindow.setTabOrder(self.executeButton, self.exitButton)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Vajra [Compromised Exp]"))
        self.sectorLabel.setText(_translate("mainWindow", "Sector"))
        self.fundNameLabel.setText(_translate("mainWindow", "Fund Name"))
        self.instrumentNameLabel.setText(_translate("mainWindow", "Instrument  Name"))
        self.labelCurrentStatus.setText(_translate("mainWindow", "Current Status from the Web: "))
        self.displayButton.setText(_translate("mainWindow", "Display"))
        self.executeButton.setText(_translate("mainWindow", "Execute Test"))
        self.checkBoxEvaluation.setText(_translate("mainWindow", "Evaluate From The Web"))
        self.pushButtonClear.setText(_translate("mainWindow", "&Clear"))
        self.exitButton.setText(_translate("mainWindow", "Exit"))
        self.label.setText(_translate("mainWindow", "Shares Held"))
        self.label_2.setText(_translate("mainWindow", "Market Value"))
        self.label_3.setText(_translate("mainWindow", "Current % of Portfolio"))
        self.label_5.setText(_translate("mainWindow", "Type"))
        self.label_4.setText(_translate("mainWindow", "Change in  Shares"))
        self.label_6.setText(_translate("mainWindow", "% Change"))
        self.label_8.setText(_translate("mainWindow", "% Ownership"))
        self.label_9.setText(_translate("mainWindow", "Quarter First Owned"))
        self.label_10.setText(_translate("mainWindow", "Source Type"))
        self.label_7.setText(_translate("mainWindow", "Change Type"))
        self.label_11.setText(_translate("mainWindow", "Source Date"))
        self.label_12.setText(_translate("mainWindow", "Average Price"))
        self.menuFile.setTitle(_translate("mainWindow", "&File"))
        self.actionAbout.setText(_translate("mainWindow", "About"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
        self.actionAdd_Fund.setText(_translate("mainWindow", "Add Fund"))
        self.actionAboutVajra.setText(_translate("mainWindow", "About"))
        self.actionExit_2.setText(_translate("mainWindow", "Exit"))
        self.actionAddFundMenu.setText(_translate("mainWindow", "&Add Fund"))
        self.actionAddFundMenu.setShortcut(_translate("mainWindow", "Alt+A"))
        self.actionExitMenu.setText(_translate("mainWindow", "&Exit"))
        self.actionExitMenu.setShortcut(_translate("mainWindow", "Ctrl+Q"))
        self.actionAboutMenu.setText(_translate("mainWindow", "A&bout"))
        self.actionAboutMenu.setShortcut(_translate("mainWindow", "F1"))
        self.actionAddInstrument.setText(_translate("mainWindow", "Add &Instrument"))
        self.actionAddInstrument.setShortcut(_translate("mainWindow", "Alt+I"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
