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

    # ==========================================
    # PART 2: The ENIAC Paradox (Physical Cost)
    # ==========================================
    
    def calculate_eniac_valves(self, number):
        """Calculates how many valves ENIAC needed (10 per decimal digit)."""
        num_str = str(number)
        decimal_digits = len(num_str)
        valves_needed = decimal_digits * 10
        return valves_needed
        
    def calculate_binary_transistors(self, number):
        """Calculates transistors needed for pure binary (1 per bit)."""
        binary_str = bin(number)[2:] # Removes the '0b' prefix
        bits_needed = len(binary_str)
        return bits_needed, binary_str

    # ==========================================
    # PART 3: Logical Cost vs Physical Viability
    # ==========================================
    
    def compare_costs(self, number):
        """Compares logical chain length vs physical component count."""
        decimal_len = len(str(number))
        binary_len = len(bin(number)[2:])
        
        print(f"--- Logical Cost Trade-off for number {number} ---")
        print(f"Decimal length: {decimal_len} digits")
        print(f"Binary length: {binary_len} bits (Longer chain = Higher logical cost)")
        print(f"Why it's worth it: {binary_len} micro-transistors are easier to print via photolithography than {decimal_len * 10} macro-components.")
