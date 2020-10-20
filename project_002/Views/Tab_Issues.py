try:
    from PySide2.QtWidgets import QWidget
except:
    from PyQt5.QtWidgets import QWidget

class IssuesTab(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.Parent = parent

        self.tbIssue = 'Issues'

        @property
        def Title(self):
            return self.tbIssue