# Binary Noise Margin Simulation

A small Python simulation that compares decimal and binary computing architectures through electrical noise tolerance and physical component cost.

## What It Demonstrates

- **Noise margin:** compares how decimal voltage levels and binary logic levels respond to a thermal noise drop.
- **Physical cost:** estimates the number of components needed to store a decimal number using an ENIAC-style decimal representation versus a binary representation.
- **Logical cost:** shows the trade-off between longer binary bit chains and the practical benefits of using smaller, easier-to-fabricate components.

## Requirements

- Python 3.8 or newer

The simulation uses only the Python standard library, so no external packages are required.

## Running the Simulation

From the project root, run:

```bash
python3 main.py
```

The program runs two experiments and prints the transmitted voltage, received voltage, decoded value, and component comparisons to the terminal.

## Project Structure

```text
.
├── main.py                 # Runs the simulation experiments
├── src/
│   └── computing_arch.py   # ComputingArchitectureSim implementation
└── test/                   # Example results and supporting test material
```

## Creator

Created by [jvbenetti](https://github.com/jvbenetti).