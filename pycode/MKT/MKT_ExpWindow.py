from pycode.ExperimentClasses import ExperimentWindow
from templates.MKT_exp_window import MKT_exp_window


class MKT_ExpWindow(ExperimentWindow):
    """ Основной класс МКТ-экспериментов """
    
    def __init__(self, parent):
        super().__init__(parent, MKT_exp_window)
        self.initUI()
    
    def initUI(self):
        super().initUI()
        
        ...