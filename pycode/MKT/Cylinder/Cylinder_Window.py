from pycode.MKT.MKT_ExpWindow import MKT_ExpWindow
from templates.MKT_Cylinder_window import MKT_Cylinder_window


class CylinderWindow(MKT_ExpWindow):
    """ Окно для экспериментов типа МКТ подтипа "Поршень" """
    
    def __init__(self, parent):
        super().__init__(parent, MKT_Cylinder_window)
        self.initUI()
    
    def initUI(self):
        super().initUI()
        
        self.T_Slider.valueChanged.connect(self.update_T)
        ...
        
    def update_T(self):
        """ Обновление температуры """
        
        self.T_lcdNumber.display(self.T_Slider.value())
    
    def start(self):
        """ Запуск эксперимента """
        
        ...