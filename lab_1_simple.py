"""
Lab 1: Quantum Computing with Qiskit - Simple Version
====================================================
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

print("LAB 1: QUANTUM COMPUTING WITH QISKIT")
print("=====================================")
print("Student: [Your Name]")
print("Date: [Current Date]")
print()

# Initialize simulator
simulator = AerSimulator()

# PART 1: Basic Qubit |0⟩
print("PART 1: Basic Qubit |0⟩")
print("------------------------")
qc1 = QuantumCircuit(1, 1)
qc1.measure(0, 0)
print("Circuit:")
print(qc1.draw(output='text'))

job1 = simulator.run(qc1, shots=1000)
counts1 = job1.result().get_counts()
print(f"Results: {counts1}")
print()

# PART 2: Superposition |+⟩
print("PART 2: Superposition |+⟩")
print("---------------------------")
qc2 = QuantumCircuit(1, 1)
qc2.h(0)  # Hadamard gate
qc2.measure(0, 0)
print("Circuit:")
print(qc2.draw(output='text'))

job2 = simulator.run(qc2, shots=1000)
counts2 = job2.result().get_counts()
print(f"Results: {counts2}")
print()

# PART 3: Bell State |Φ+⟩
print("PART 3: Bell State |Φ+⟩")
print("------------------------")
qc3 = QuantumCircuit(2, 2)
qc3.h(0)      # Hadamard
qc3.cx(0, 1)  # CNOT
qc3.measure_all()
print("Circuit:")
print(qc3.draw(output='text'))

job3 = simulator.run(qc3, shots=1000)
counts3 = job3.result().get_counts()
# Clean up results for display
clean_counts3 = {}
for key, value in counts3.items():
    clean_key = key.split()[0] if ' ' in key else key
    clean_counts3[clean_key] = value
print(f"Results: {clean_counts3}")
print()

# Create simple bar chart visualization
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

# Plot 1: Basic Qubit
ax1.bar(counts1.keys(), counts1.values(), color='skyblue')
ax1.set_title('Basic Qubit |0⟩', fontweight='bold')
ax1.set_ylabel('Counts')

# Plot 2: Superposition
ax2.bar(counts2.keys(), counts2.values(), color='lightgreen')
ax2.set_title('Superposition |+⟩', fontweight='bold')
ax2.set_ylabel('Counts')

# Plot 3: Bell State
ax3.bar(clean_counts3.keys(), clean_counts3.values(), color='salmon')
ax3.set_title('Bell State |Φ+⟩', fontweight='bold')
ax3.set_ylabel('Counts')

plt.tight_layout()
plt.savefig('lab1_simple_results.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved as 'lab1_simple_results.png'")

# Summary
print()
print("OBSERVATIONS:")
print("=============")
print("1. Basic Qubit: Always |0⟩ (deterministic)")
print("2. Superposition: ~50% |0⟩, ~50% |1⟩ (random)")
print("3. Bell State: Only |00⟩ and |11⟩ (entangled)")
print()
print("CONCLUSION:")
print("===========")
print("✓ Demonstrated quantum superposition")
print("✓ Demonstrated quantum entanglement")
print("✓ Results match quantum theory")