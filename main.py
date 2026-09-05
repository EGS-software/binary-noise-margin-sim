from .src import ComputingArchitectureSim

if __name__ == "__main__":
    sim = ComputingArchitectureSim(voltage_max=5.0, thermal_noise=-0.8)
    
    print("=== EXPERIMENT 1: NOISE MARGIN ===")
    
    # Testing Decimal (Trying to send '8')
    t_v, r_v, read_dec = sim.simulate_decimal_hardware(8)
    print(f"DECIMAL: Sent 8 ({t_v}V) | Noise applied ({sim.noise}V) | Received {r_v:.1f}V | Hardware read: {read_dec}")
    if read_dec != 8:
        print("-> Result: DECIMAL DATA CORRUPTED!\n")
        
    # Testing Binary (Trying to send '1')
    t_v, r_v, read_bin = sim.simulate_binary_hardware(1)
    print(f"BINARY: Sent 1 ({t_v}V) | Noise applied ({sim.noise}V) | Received {r_v:.1f}V | Hardware read: {read_bin}")
    if read_bin == 1:
        print("-> Result: BINARY SURVIVED NOISE!\n")

    print("=== EXPERIMENT 2: THE ENIAC PARADOX ===")
    test_number = 395
    eniac_valves = sim.calculate_eniac_valves(test_number)
    bin_trans, bin_str = sim.calculate_binary_transistors(test_number)
    
    print(f"To store the number {test_number}:")
    print(f"ENIAC (Decimal): Needed {eniac_valves} valves in a ring counter.")
    print(f"Modern (Binary): Needs {bin_trans} components to store '{bin_str}'.\n")
    
    sim.compare_costs(test_number)