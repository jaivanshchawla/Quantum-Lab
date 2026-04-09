"""Lab 7: Bloch Sphere Visualization only"""

# QuantumCircuit lets us build quantum circuits by adding gates
from qiskit import QuantumCircuit

# Statevector computes the exact quantum state vector of a circuit (no measurement noise)
from qiskit.quantum_info import Statevector

# plot_bloch_multivector renders a statevector as a 3D Bloch sphere figure
from qiskit.visualization import plot_bloch_multivector

# matplotlib.pyplot is needed to call show() and close() on the figures
import matplotlib.pyplot as plt

# Each tuple: (display label, list of gate names to apply in order)
# Empty gate list means no gates applied — qubit stays in ground state |0>
states = [
    ("|0>",  []),       # no gates: qubit at north pole of Bloch sphere
    ("H|0>", ['h']),    # Hadamard: puts qubit on equator (+X axis), equal superposition
    ("X|0>", ['x']),    # Pauli-X (NOT gate): flips |0> to |1>, south pole
    ("Y|0>", ['y']),    # Pauli-Y: also reaches south pole but with a phase of i
]

# Loop over each state definition
for label, gates in states:

    # Create a fresh 1-qubit circuit (no classical bits needed, no measurement)
    qc = QuantumCircuit(1)

    # Apply each gate by name using getattr
    # e.g. gates=['h'] calls qc.h(0), gates=['x'] calls qc.x(0)
    for g in gates:
        getattr(qc, g)(0)   # getattr(qc, 'h') returns qc.h, then (0) applies it to qubit 0

    # Compute the exact statevector — pure math, no simulation shots needed
    # Returns a complex vector of length 2: [amplitude_of_|0>, amplitude_of_|1>]
    sv = Statevector.from_instruction(qc)

    # Convert the statevector into a Bloch sphere matplotlib figure
    # title= labels the sphere with the state name
    fig = plot_bloch_multivector(sv, title=label)

    # Build a safe filename by stripping ket notation characters
    # e.g. "H|0>" becomes "bloch_H0>.png" -> we strip | only here
    fname = f"bloch_{label.replace('|', '')}.png"

    # Save the figure to disk as PNG at 150 DPI with white background
    fig.savefig(fname, dpi=150, bbox_inches='tight', facecolor='white')

    # Display the Bloch sphere window on screen (blocks until window is closed)
    plt.show()

    # Close the figure and free memory before moving to the next state
    plt.close(fig)

    # Confirm the file was saved
    print(f"Saved: {fname}")

