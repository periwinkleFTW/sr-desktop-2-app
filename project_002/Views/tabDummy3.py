try:
    from PySide2.QtWidgets import QWidget
except:
    from PyQt.QtWidgets import QWidget

class TabDummy3(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.Parent = parent

        self.tabTitle = 'Tab3'

        @property
        def Title(self):
            return self.tabTitle