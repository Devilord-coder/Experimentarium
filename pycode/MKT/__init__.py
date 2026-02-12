from .Ideal_Gas import Ideal_Gas
from .Tube.Tube_Window import TubeWindow
from .Cylinder.Cylinder_Window import CylinderWindow


"""
Главный модуль для экспериментов типа МКТ
(Молекулярно-кинетическая теория)
"""
print('You opened a MKT module...')

PACKAGE_VERSION = "1.0.0"

__all__ = [
    "Ideal_Gas",
    "TubeWindow",
    "CylinderWindow"
]