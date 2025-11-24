from pycode.ExperimentClasses import ExperimentWindow
from templates_py.MKT_exp_window import MKT_exp_window


class MKT_ExpWindow(ExperimentWindow):
    def __init__(self, parent):
        super().__init__(parent, MKT_exp_window)
        self.initUI()
    
    def initUI(self):
        super().initUI()
        
        self.type = 'MKT'