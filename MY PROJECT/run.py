# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'run.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from New import Ui_Form

class Ui_MainWindow(object):

    def __init__(self):
        self.evalDialog = QtWidgets.QMainWindow()
        self.new_screen = Ui_Form()                           
        self.new_screen.setupUi(self.evalDialog)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(945, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 951, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 20, 0, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.batsman = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.batsman.setObjectName("batsman")
        self.horizontalLayout.addWidget(self.batsman)
        self.batcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.batcount.setObjectName("batcount")
        self.horizontalLayout.addWidget(self.batcount)
        self.wicketkeeper = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.wicketkeeper.setObjectName("wicketkeeper")
        self.horizontalLayout.addWidget(self.wicketkeeper)
        self.wicketcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.wicketcount.setObjectName("wicketcount")
        self.horizontalLayout.addWidget(self.wicketcount)
        self.Allrounder = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Allrounder.setObjectName("Allrounder")
        self.horizontalLayout.addWidget(self.Allrounder)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bowlers = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bowlers.setObjectName("bowlers")
        self.horizontalLayout.addWidget(self.bowlers)
        self.balllcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.balllcount.setObjectName("balllcount")
        self.horizontalLayout.addWidget(self.balllcount)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 941, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 20, 0, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 170, 931, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.totalplayers = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.totalplayers.setObjectName("totalplayers")
        self.horizontalLayout_3.addWidget(self.totalplayers)
        self.playercount = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.playercount.setObjectName("playercount")
        self.horizontalLayout_3.addWidget(self.playercount)
        self.teamname = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.teamname.setObjectName("teamname")
        self.horizontalLayout_3.addWidget(self.teamname)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 230, 441, 421))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_1.setGeometry(QtCore.QRect(450, 231, 491, 401))
        self.listWidget_1.setObjectName("listWidget_1")
        self.availableplayers = QtWidgets.QLabel(self.centralwidget)
        self.availableplayers.setGeometry(QtCore.QRect(170, 210, 121, 16))
        self.availableplayers.setObjectName("availableplayers")
        self.selectedplayers = QtWidgets.QLabel(self.centralwidget)
        self.selectedplayers.setGeometry(QtCore.QRect(560, 210, 121, 21))
        self.selectedplayers.setObjectName("selectedplayers")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 22))
        self.menubar.setObjectName("menubar")
        self.menuManage = QtWidgets.QMenu(self.menubar)
        self.menuManage.setObjectName("menuManage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionNew_Team.triggered.connect(Ui_Form)
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage.addAction(self.actionNew_Team)
        self.menuManage.addAction(self.actionOpen_Team)
        self.menuManage.addAction(self.actionSave_Team)
        self.menuManage.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

       


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.batsman.setText(_translate("MainWindow", "Batsman"))
        self.batcount.setText(_translate("MainWindow", "##"))
        self.wicketkeeper.setText(_translate("MainWindow", "WicketKeeper"))
        self.wicketcount.setText(_translate("MainWindow", "##"))
        self.Allrounder.setText(_translate("MainWindow", "Allrounder"))
        self.label_2.setText(_translate("MainWindow", "##"))
        self.bowlers.setText(_translate("MainWindow", "Bowlers"))
        self.balllcount.setText(_translate("MainWindow", "##"))
        self.radioButton_2.setText(_translate("MainWindow", "BAT"))
        self.radioButton_3.setText(_translate("MainWindow", "WK"))
        self.radioButton.setText(_translate("MainWindow", "ALR"))
        self.radioButton_4.setText(_translate("MainWindow", "BWL"))
        self.totalplayers.setText(_translate("MainWindow", "Totalplayers:"))
        self.playercount.setText(_translate("MainWindow", "00"))
        self.teamname.setText(_translate("MainWindow", "Teamname:"))
        self.label.setText(_translate("MainWindow", "name"))
        self.availableplayers.setText(_translate("MainWindow", "AvailablePlayers"))
        self.selectedplayers.setText(_translate("MainWindow", "SelectedPlayers"))
        self.menuManage.setTitle(_translate("MainWindow", " Manage"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
