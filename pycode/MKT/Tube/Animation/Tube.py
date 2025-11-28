from PyQt6.QtWidgets import QWidget
try:
    from .Molecule import Molecule
except ImportError:
    from Molecule import Molecule
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QTimer
import random


class Tube(QWidget):
    def __init__(self, parent):
        super().__init__()
        
        self.main_window = parent
        self.molecules = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_balls)
        self.timer.start(16)
        
        self.setStyleSheet('background-color: "black";')
        
        self.create_molecules(self.main_window.T_Slider.value())
    
    def create_molecules(self, T):
        T_factor = T / 1000
        for _ in range(300):
            radius = 5
            x = random.randint(radius, self.width() - radius)
            y = random.randint(radius, self.height() - radius)
            color = QColor(128, 128, 128)
            
            if T_factor < 0.2:
                speeds = [-2, -1, 1, 2]
            elif 0.2 <= T_factor < 0.4:
                speeds = [-3, -4, 4, 3]
            elif 0.4 <= T_factor < 0.6:
                speeds = [-5, -6, 5, 6]
            elif 0.6 <= T_factor < 0.8:
                speeds = [-7, -8, 8, 7]
            else:
                speeds = [-9, -10, 10, 9]
            delta_x = random.choice(speeds)
            delta_y = random.choice(speeds)
            
            self.molecules.append(Molecule(x, y, radius, color, delta_x, delta_y))
    
    def update_balls(self):
        # Обновляем позиции всех шариков
        for molecule in self.molecules:
            molecule.move(self.width(), self.height())
        
        # Перерисовываем виджет
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Рисуем все шарики
        for molecule in self.molecules:
            molecule.draw(painter)