# from pycode.MKT import Ideal_Gas


class Cylinder:
    def __init__(self, gas, V: float, T: float | None = None):
        self.gas = gas
        self.V = V