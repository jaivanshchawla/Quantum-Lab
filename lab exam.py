from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

states = [
    ("|0>",      []),           # ground state, north pole
    ("H|0>",     ['h']),        # Hadamard once → |+⟩, equator +X
    ("HH|0>",    ['h','h']),    # Hadamard twice → back to |0⟩ (H is its own inverse)
    ("HX|0>",    ['h','x']),    # Hadamard then X → still on equator (X preserves |+⟩)
    ("XH|0>",    ['x','h']),    # X then Hadamard → |−⟩, equator −X
    ("HZ|0>",    ['h','z']),    # Hadamard then Z → |−⟩, equator −X (Z flips phase in superposition)
    ("ZH|0>",    ['z','h']),    # Z then Hadamard → same as H|0⟩ (Z on |0⟩ is no-op)
    ("HY|0>",    ['h','y']),    # Hadamard then Y → equator −X with phase
    ("X|0>",     ['x']),        # Pauli-X, south pole
    ("Y|0>",     ['y']),        # Pauli-Y, south pole with phase i
]

for label, gates in states:
    qc = QuantumCircuit(1)
    
    for g in gates:
        getattr(qc, g)(0)
    sv = Statevector.from_instruction(qc)
    fig = plot_bloch_multivector(sv, title=label)
    fname = f"blochlabfinal_{label.replace('|', '').replace('>', '')}.png"
    fig.savefig(fname, dpi=150, bbox_inches='tight', facecolor='white')
    plt.show()
    plt.close(fig)
    print(f"Saved: {fname}")