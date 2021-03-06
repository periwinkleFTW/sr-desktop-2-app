try:
    # from PySide2.QtCore    import
    from PySide2.QtWidgets import QApplication, QMainWindow
except:
    # from PyQt5.QtCore    import
    from PyQt5.QtWidgets import QApplication, QMainWindow

from sys import exit as sysExit

import Views.srCentralPanel as CntrPnl


class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("SR test")

        self.setGeometry(150, 150, 1470, 750)

        self.CenterPane = CntrPnl.CenterPanel(self)
        self.setCentralWidget(self.CenterPane)


if __name__ == "__main__":
    MainEventThread = QApplication([])

    MainApplication = Main()
    MainApplication.show()

    sysExit(MainEventThread.exec_())
