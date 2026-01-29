"""
Quantum Circuit Visualization Demo
A simple but majestic quantum circuit demonstration using Qiskit
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram, circuit_drawer
from qiskit_aer import AerSimulator
import numpy as np

def create_bell_state_circuit():
    """
    Creates a Bell state quantum circuit - one of the most fundamental
    and beautiful quantum circuits demonstrating entanglement
    """
    # Create quantum and classical registers
    qreg = QuantumRegister(2, 'q')
    creg = ClassicalRegister(2, 'c')
    
    # Create the quantum circuit
    circuit = QuantumCircuit(qreg, creg)
    
    # Add a barrier for visual clarity
    circuit.barrier()
    
    # Create superposition on first qubit
    circuit.h(qreg[0])  # Hadamard gate
    
    # Create entanglement between qubits
    circuit.cx(qreg[0], qreg[1])  # CNOT gate
    
    # Add another barrier
    circuit.barrier()
    
    # Measure both qubits
    circuit.measure(qreg, creg)
    
    return circuit

def create_quantum_fourier_transform():
    """
    Creates a 3-qubit Quantum Fourier Transform circuit
    A more complex and visually impressive circuit
    """
    n_qubits = 3
    qreg = QuantumRegister(n_qubits, 'q')
    circuit = QuantumCircuit(qreg)
    
    # QFT implementation
    for i in range(n_qubits):
        # Apply Hadamard gate
        circuit.h(qreg[i])
        
        # Apply controlled phase rotations
        for j in range(i + 1, n_qubits):
            circuit.cp(np.pi / (2 ** (j - i)), qreg[j], qreg[i])
    
    # Swap qubits to reverse the order
    for i in range(n_qubits // 2):
        circuit.swap(qreg[i], qreg[n_qubits - 1 - i])
    
    return circuit

def visualize_circuits():
    """
    Create and visualize multiple quantum circuits with different styles
    """
    # Set up the plotting style for a majestic look
    plt.style.use('dark_background')
    
    # Create circuits
    bell_circuit = create_bell_state_circuit()
    qft_circuit = create_quantum_fourier_transform()
    
    # Create a figure with subplots
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('Quantum Circuit Gallery', fontsize=20, color='gold', fontweight='bold')
    
    # Bell State Circuit Visualization
    ax1 = plt.subplot(3, 2, 1)
    bell_circuit.draw(output='mpl', style='iqp', ax=ax1)
    ax1.set_title('Bell State Circuit (Entanglement)', fontsize=14, color='cyan', pad=20)
    
    # QFT Circuit Visualization
    ax2 = plt.subplot(3, 2, 2)
    qft_circuit.draw(output='mpl', style='iqp', ax=ax2)
    ax2.set_title('Quantum Fourier Transform', fontsize=14, color='cyan', pad=20)
    
    # Text-based circuit representation
    ax3 = plt.subplot(3, 1, 2)
    ax3.text(0.1, 0.8, "Bell State Circuit (Text Representation):", 
             fontsize=12, color='yellow', transform=ax3.transAxes, fontweight='bold')
    ax3.text(0.1, 0.6, str(bell_circuit), 
             fontsize=10, color='white', transform=ax3.transAxes, family='monospace')
    ax3.text(0.1, 0.3, "QFT Circuit (Text Representation):", 
             fontsize=12, color='yellow', transform=ax3.transAxes, fontweight='bold')
    ax3.text(0.1, 0.1, str(qft_circuit), 
             fontsize=8, color='white', transform=ax3.transAxes, family='monospace')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis('off')
    
    # Simulate and plot results for Bell state
    simulator = AerSimulator()
    job = simulator.run(bell_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts()
    
    ax4 = plt.subplot(3, 2, 5)
    plot_histogram(counts, ax=ax4, color=['gold', 'cyan', 'magenta', 'lime'])
    ax4.set_title('Bell State Measurement Results', fontsize=12, color='cyan')
    
    # Add some quantum circuit statistics
    ax5 = plt.subplot(3, 2, 6)
    stats_text = f"""
    Bell State Circuit Stats:
    • Qubits: {bell_circuit.num_qubits}
    • Gates: {len(bell_circuit.data)}
    • Depth: {bell_circuit.depth()}
    • Entangled: Yes ✨
    
    QFT Circuit Stats:
    • Qubits: {qft_circuit.num_qubits}
    • Gates: {len(qft_circuit.data)}
    • Depth: {qft_circuit.depth()}
    • Quantum Algorithm: Yes 🌟
    """
    ax5.text(0.1, 0.9, stats_text, fontsize=11, color='gold', 
             transform=ax5.transAxes, verticalalignment='top', family='monospace')
    ax5.set_xlim(0, 1)
    ax5.set_ylim(0, 1)
    ax5.axis('off')
    
    plt.tight_layout()
    plt.savefig('quantum_circuits_visualization.png', dpi=300, bbox_inches='tight', 
                facecolor='black', edgecolor='none')
    plt.show()

def create_grover_search_circuit():
    """
    Creates a simple 2-qubit Grover's search algorithm circuit
    """
    qreg = QuantumRegister(2, 'q')
    creg = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg, creg)
    
    # Initialize superposition
    circuit.h(qreg[0])
    circuit.h(qreg[1])
    
    # Oracle (marking |11⟩ state)
    circuit.cz(qreg[0], qreg[1])
    
    # Diffusion operator
    circuit.h(qreg[0])
    circuit.h(qreg[1])
    circuit.z(qreg[0])
    circuit.z(qreg[1])
    circuit.cz(qreg[0], qreg[1])
    circuit.h(qreg[0])
    circuit.h(qreg[1])
    
    # Measure
    circuit.measure(qreg, creg)
    
    return circuit

if __name__ == "__main__":
    print("🌟 Creating Majestic Quantum Circuits 🌟")
    print("=" * 50)
    
    # Create and display individual circuits
    print("\n1. Bell State Circuit (Quantum Entanglement):")
    bell = create_bell_state_circuit()
    print(bell)
    
    print("\n2. Quantum Fourier Transform Circuit:")
    qft = create_quantum_fourier_transform()
    print(qft)
    
    print("\n3. Grover's Search Algorithm Circuit:")
    grover = create_grover_search_circuit()
    print(grover)
    
    print("\n🎨 Generating beautiful visualizations...")
    visualize_circuits()
    
    print("\n✨ Quantum circuits created successfully!")
    print("📊 Visualization saved as 'quantum_circuits_visualization.png'")
    print("\nThese circuits demonstrate:")
    print("• Quantum superposition (H gates)")
    print("• Quantum entanglement (CNOT gates)")
    print("• Quantum algorithms (QFT, Grover)")
    print("• Measurement and classical output")