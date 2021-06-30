# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.gridLayout.addWidget(self.fileNameLabel, 0, 3, 1, 1)
        self.dataTable = QtWidgets.QTableWidget(self.centralwidget)
        self.dataTable.setMinimumSize(QtCore.QSize(0, 0))
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(4)
        self.dataTable.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(3, 3, item)
        self.gridLayout.addWidget(self.dataTable, 1, 3, 1, 1)
        self.chooseFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.gridLayout.addWidget(self.chooseFileButton, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data display"))
        self.fileNameLabel.setText(_translate("MainWindow", "File name"))
        self.dataTable.setSortingEnabled(False)
        item = self.dataTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row 1"))
        item = self.dataTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row 2"))
        item = self.dataTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row 3"))
        item = self.dataTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row 4"))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column 1"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column 2"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column 3"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column 4"))
        __sortingEnabled = self.dataTable.isSortingEnabled()
        self.dataTable.setSortingEnabled(False)
        item = self.dataTable.item(0, 0)
        item.setText(_translate("MainWindow", "11"))
        item = self.dataTable.item(0, 1)
        item.setText(_translate("MainWindow", "12"))
        item = self.dataTable.item(0, 2)
        item.setText(_translate("MainWindow", "13"))
        item = self.dataTable.item(0, 3)
        item.setText(_translate("MainWindow", "14"))
        item = self.dataTable.item(1, 0)
        item.setText(_translate("MainWindow", "21"))
        item = self.dataTable.item(1, 1)
        item.setText(_translate("MainWindow", "22"))
        item = self.dataTable.item(1, 2)
        item.setText(_translate("MainWindow", "23"))
        item = self.dataTable.item(1, 3)
        item.setText(_translate("MainWindow", "24"))
        item = self.dataTable.item(2, 0)
        item.setText(_translate("MainWindow", "31"))
        item = self.dataTable.item(2, 1)
        item.setText(_translate("MainWindow", "32"))
        item = self.dataTable.item(2, 2)
        item.setText(_translate("MainWindow", "33"))
        item = self.dataTable.item(2, 3)
        item.setText(_translate("MainWindow", "34"))
        item = self.dataTable.item(3, 0)
        item.setText(_translate("MainWindow", "41"))
        item = self.dataTable.item(3, 1)
        item.setText(_translate("MainWindow", "42"))
        item = self.dataTable.item(3, 2)
        item.setText(_translate("MainWindow", "43"))
        item = self.dataTable.item(3, 3)
        item.setText(_translate("MainWindow", "44"))
        self.dataTable.setSortingEnabled(__sortingEnabled)
        self.chooseFileButton.setText(_translate("MainWindow", "Choose file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
