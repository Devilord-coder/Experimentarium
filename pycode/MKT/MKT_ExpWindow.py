from pycode.ExperimentClasses import ExperimentWindow, ErrorDialog
from templates_py.MKT_exp_window import MKT_exp_window
from .MKT_Show import MKT_Show


class MKT_ExpWindow(ExperimentWindow):
    def __init__(self, parent):
        super().__init__(parent, MKT_exp_window)
        self.initUI()
    
    def initUI(self):
        super().initUI()
        
        self.type = 'MKT'
        self.start_btn.clicked.connect(self.start)
        self.add_figure_btn.clicked.connect(self.add_figure)
    
    def add_figure(self):
        if self.figures_textbrowser.toPlainText():
            dlg = ErrorDialog("В данном эксперименте можно создать только одно тело.\nХотите изменить его?", self)
            if dlg.exec():
                pass
            else:
                return

    def start(self):
        self.hide()
        self.sec_window = MKT_Show(self)
        self.sec_window.show()