try:
    from PySide2.QtWidgets import QWidget
except:
    from PyQt5.QtWidgets import QWidget

class PeopleTab(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.Parent = parent

        self.tbPeople = 'People'

        @property
        def Title(self):
            return self.tbPeople