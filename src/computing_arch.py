import math

class ComputingArchitectureSim:
    def __init__(self, voltage_max=5.0, thermal_noise=-0.8):
        self.voltage_max = voltage_max
        self.noise = thermal_noise
