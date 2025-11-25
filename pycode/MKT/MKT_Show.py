from PyQt6.QtWidgets import QWidget


class MKT_Show(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        self.initUI()
        
    def initUI(self):
        pass