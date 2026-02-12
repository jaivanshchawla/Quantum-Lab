from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

try:
    print("Creating circuit...")
    qc = QuantumCircuit(1)
    qc.h(0)
    
    print("Getting state vector...")
    state = Statevector.from_instruction(qc)
    print(f"State: {state.data}")
    
    print("Creating Bloch sphere...")
    fig = plot_bloch_multivector(state, title="Test")
    fig.savefig('test_bloch.png', dpi=150)
    plt.close()
    print("✓ Success!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
