from PyQt6.QtWidgets import QWidget
from resources.MKT_physiscs import PHYSICS
from PyQt6.QtGui import QIcon
from PyQt6 import uic
import io
from templates.physical_base_window import physical_base_window
from sheets_py.experiment_window_sheet import experiment_window_sheet


class Physical_Base_Window(QWidget):
    """ Окно для выводы физических формул """
    
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi(io.StringIO(physical_base_window), self)
        self.setWindowIcon(QIcon("resources/vampire_bat.png"))
        self.setStyleSheet(experiment_window_sheet)
        self.main_window = main_window
        
        self.textBrowser.setHtml(PHYSICS)