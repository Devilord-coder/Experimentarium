from pycode.ExperimentClasses import ExperimentWindow


class MKT_ExpWindow(ExperimentWindow):
    """ Основной класс МКТ-экспериментов """
    
    def __init__(self, parent, template):
        super().__init__(parent, template)
        self.initUI()
    
    def initUI(self):
        super().initUI()
        
        self.physics_window = None
        self.physical_base_btn.clicked.connect(self.show_physics)
    
    def show_physics(self):
        """ Функция для открытия окна с формулами """
        
        self.sec_window = self.physics_window
        self.sec_window.show()