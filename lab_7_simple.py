"""
Lab 7: Hadamard Gate and Bloch Sphere Visualization
===================================================
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

print("LAB 7: HADAMARD GATE AND BLOCH SPHERE")
print("======================================\n")

# Create states
qc1 = QuantumCircuit(1)
state1 = Statevector.from_instruction(qc1)
print("State 1: |0⟩")
print(qc1.draw(output='text'))

qc2 = QuantumCircuit(1)
qc2.h(0)
state2 = Statevector.from_instruction(qc2)
print("\nState 2: H|0⟩")
print(qc2.draw(output='text'))

qc3 = QuantumCircuit(1)
qc3.x(0)
state3 = Statevector.from_instruction(qc3)
print("\nState 3: X|0⟩")
print(qc3.draw(output='text'))

qc4 = QuantumCircuit(1)
qc4.y(0)
state4 = Statevector.from_instruction(qc4)
print("\nState 4: Y|0⟩")
print(qc4.draw(output='text'))

# Create Bloch spheres
print("\nCreating Bloch sphere visualizations...")
states = [state1, state2, state3, state4]
titles = ['|0⟩ State', 'H|0⟩ State', 'X|0⟩ State', 'Y|0⟩ State']

for i, (state, title) in enumerate(zip(states, titles)):
    fig = plot_bloch_multivector(state, title=title)
    filename = f'lab7_bloch_{i+1}.png'
    fig.savefig(filename, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"✓ Saved {filename}")

print("\n✓ Lab 7 complete! Bloch spheres saved.")
print("You can now take screenshots of the output files.")
