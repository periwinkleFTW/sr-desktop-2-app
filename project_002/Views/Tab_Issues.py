try:
    from PySide2.QtWidgets import QWidget
except:
    from PyQt.QtWidgets import QWidget

class IssuesTab(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.Parent = parent

        self.tbIssue = 'ISSUES'

        @property
        def Title(self):
            return self.tbIssue