import math

class ComputingArchitectureSim:
    def __init__(self, voltage_max=5.0, thermal_noise=-0.8):
        self.voltage_max = voltage_max
        self.noise = thermal_noise

    # ==========================================
    # PART 1: The Noise Margin Experiment
    # ==========================================
    
    def simulate_decimal_hardware(self, target_number):
        """Simulates sending a decimal number (0-9) over a single 5V wire."""
        # Each step is 0.5V (0 = 0V, 1 = 0.5V, ... 9 = 4.5V)
        voltage_step = self.voltage_max / 10
        transmitted_voltage = target_number * voltage_step
        
        # Apply thermal noise drop
        received_voltage = transmitted_voltage + self.noise
        
        # Hardware reads the nearest voltage step
        read_number = round(received_voltage / voltage_step)
        
        # Ensure it doesn't go below 0
        read_number = max(0, read_number)
        
        return transmitted_voltage, received_voltage, read_number

    def simulate_binary_hardware(self, bit_value):
        """Simulates sending a binary bit (0 or 1) over a 5V wire."""
        # 0 is 0V, 1 is 5V
        transmitted_voltage = self.voltage_max if bit_value == 1 else 0.0
        
        # Apply thermal noise drop
        received_voltage = transmitted_voltage + self.noise
        
        # Binary reading logic: > 3V is 1, < 2V is 0
        if received_voltage >= 3.0:
            read_bit = 1
        elif received_voltage <= 2.0:
            read_bit = 0
        else:
            read_bit = None # Corrupted data (Undefined state)
            
        return transmitted_voltage, received_voltage, read_bit
