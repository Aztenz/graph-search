from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Entry(object):
    def setupUi(self, Entry):
        self.dir = False
        Entry.setObjectName("Entry")
        Entry.resize(985, 709)
        self.centralwidget = QtWidgets.QWidget(Entry)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 631, 171))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 220, 631, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.directedgraph = QtWidgets.QPushButton(self.centralwidget)
        self.directedgraph.setGeometry(QtCore.QRect(220, 380, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.directedgraph.setFont(font)
        self.directedgraph.setObjectName("directedgraph")
        self.undirectedgraph = QtWidgets.QPushButton(self.centralwidget)
        self.undirectedgraph.setGeometry(QtCore.QRect(540, 380, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.undirectedgraph.setFont(font)
        self.undirectedgraph.setObjectName("undirectedgraph")
        Entry.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Entry)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 21))
        self.menubar.setObjectName("menubar")
        Entry.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Entry)
        self.statusbar.setObjectName("statusbar")
        Entry.setStatusBar(self.statusbar)
        self.retranslateUi(Entry)
        QtCore.QMetaObject.connectSlotsByName(Entry)

    def retranslateUi(self, Entry):
        _translate = QtCore.QCoreApplication.translate
        Entry.setWindowTitle(_translate("Entry", "Welcome"))
        self.label.setText(_translate("Entry", "Welcome to our search graph"))
        self.label_2.setText(_translate("Entry", "What kind of graph would you like to search on ?"))
        self.directedgraph.setText(_translate("Entry", "Directed Graph"))
        self.undirectedgraph.setText(_translate("Entry", "Undirected Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Entry = QtWidgets.QMainWindow()
    ui = Ui_Entry()
    ui.setupUi(Entry)
    Entry.show()
    sys.exit(app.exec_())

