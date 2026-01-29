"""
Visual Quantum Circuit Demo with Matplotlib
Beautiful quantum circuits with graphical visualization
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import numpy as np

def create_beautiful_bell_circuit():
    """Create a Bell state circuit with visual styling"""
    qreg = QuantumRegister(2, 'qubit')
    creg = ClassicalRegister(2, 'classical')
    circuit = QuantumCircuit(qreg, creg)
    
    # Add gates with barriers for visual clarity
    circuit.barrier(label='Start')
    circuit.h(qreg[0])
    circuit.cx(qreg[0], qreg[1])
    circuit.barrier(label='Entangled')
    circuit.measure(qreg, creg)
    
    return circuit

def create_grover_circuit():
    """Create a simple 2-qubit Grover search circuit"""
    qreg = QuantumRegister(2, 'q')
    creg = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg, creg)
    
    # Initialize superposition
    circuit.h(qreg[0])
    circuit.h(qreg[1])
    circuit.barrier(label='Superposition')
    
    # Oracle (marking |11⟩ state)
    circuit.cz(qreg[0], qreg[1])
    circuit.barrier(label='Oracle')
    
    # Diffusion operator
    circuit.h(qreg[0])
    circuit.h(qreg[1])
    circuit.z(qreg[0])
    circuit.z(qreg[1])
    circuit.cz(qreg[0], qreg[1])
    circuit.h(qreg[0])
    circuit.h(qreg[1])
    circuit.barrier(label='Diffusion')
    
    circuit.measure(qreg, creg)
    return circuit

def visualize_quantum_gallery():
    """Create a comprehensive visual gallery of quantum circuits"""
    
    # Set up the plotting style
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(20, 14))
    fig.suptitle('Quantum Circuit Gallery', fontsize=24, color='gold', fontweight='bold', y=0.95)
    
    # Create circuits
    bell_circuit = create_beautiful_bell_circuit()
    grover_circuit = create_grover_circuit()
    
    # Simple QFT circuit
    qft_circuit = QuantumCircuit(3)
    qft_circuit.h(0)
    qft_circuit.cp(np.pi/2, 1, 0)
    qft_circuit.cp(np.pi/4, 2, 0)
    qft_circuit.h(1)
    qft_circuit.cp(np.pi/2, 2, 1)
    qft_circuit.h(2)
    qft_circuit.swap(0, 2)
    
    try:
        # Circuit visualizations
        ax1 = plt.subplot(3, 3, 1)
        bell_circuit.draw(output='mpl', ax=ax1, style='iqp')
        ax1.set_title('Bell State Circuit', fontsize=14, color='cyan', pad=20)
        
        ax2 = plt.subplot(3, 3, 2)
        grover_circuit.draw(output='mpl', ax=ax2, style='iqp')
        ax2.set_title("Grover's Algorithm", fontsize=14, color='cyan', pad=20)
        
        ax3 = plt.subplot(3, 3, 3)
        qft_circuit.draw(output='mpl', ax=ax3, style='iqp')
        ax3.set_title('Quantum Fourier Transform', fontsize=14, color='cyan', pad=20)
        
    except Exception as e:
        print(f"Matplotlib visualization not available: {e}")
        print("Falling back to text-based visualization...")
        
        # Text-based fallback
        ax1 = plt.subplot(3, 1, 1)
        ax1.text(0.1, 0.8, "Bell State Circuit:", fontsize=16, color='yellow', fontweight='bold')
        ax1.text(0.1, 0.4, str(bell_circuit), fontsize=10, color='white', family='monospace')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.axis('off')
        
        ax2 = plt.subplot(3, 1, 2)
        ax2.text(0.1, 0.8, "Grover's Algorithm:", fontsize=16, color='yellow', fontweight='bold')
        ax2.text(0.1, 0.4, str(grover_circuit), fontsize=8, color='white', family='monospace')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        ax2.axis('off')
        
        ax3 = plt.subplot(3, 1, 3)
        ax3.text(0.1, 0.8, "Quantum Fourier Transform:", fontsize=16, color='yellow', fontweight='bold')
        ax3.text(0.1, 0.4, str(qft_circuit), fontsize=10, color='white', family='monospace')
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        ax3.axis('off')
    
    # Simulate and plot results
    simulator = AerSimulator()
    
    # Bell state results
    bell_job = simulator.run(bell_circuit, shots=1000)
    bell_counts = bell_job.result().get_counts()
    
    ax4 = plt.subplot(3, 3, 4)
    plot_histogram(bell_counts, ax=ax4, color=['gold', 'cyan'])
    ax4.set_title('Bell State Results', fontsize=12, color='cyan')
    
    # Grover results
    grover_job = simulator.run(grover_circuit, shots=1000)
    grover_counts = grover_job.result().get_counts()
    
    ax5 = plt.subplot(3, 3, 5)
    plot_histogram(grover_counts, ax=ax5, color=['lime', 'magenta', 'orange', 'red'])
    ax5.set_title('Grover Search Results', fontsize=12, color='cyan')
    
    # Add quantum facts
    ax6 = plt.subplot(3, 3, 6)
    quantum_facts = """
Quantum Computing Facts

* Superposition: Qubits can be in multiple 
  states simultaneously

* Entanglement: Qubits can be correlated 
  in ways impossible classically

* Interference: Quantum amplitudes can 
  cancel or reinforce each other

* Measurement: Observing a quantum state 
  collapses it to a classical state

* Quantum Advantage: Some problems can be 
  solved exponentially faster on quantum 
  computers
    """
    ax6.text(0.05, 0.95, quantum_facts, fontsize=11, color='gold', 
             transform=ax6.transAxes, verticalalignment='top', family='monospace')
    ax6.set_xlim(0, 1)
    ax6.set_ylim(0, 1)
    ax6.axis('off')
    
    # Circuit statistics
    ax7 = plt.subplot(3, 3, 7)
    stats_text = f"""
Circuit Statistics:

Bell State:
* Qubits: {bell_circuit.num_qubits}
* Gates: {len(bell_circuit.data)}
* Depth: {bell_circuit.depth()}

Grover Search:
* Qubits: {grover_circuit.num_qubits}
* Gates: {len(grover_circuit.data)}
* Depth: {grover_circuit.depth()}

QFT:
* Qubits: {qft_circuit.num_qubits}
* Gates: {len(qft_circuit.data)}
* Depth: {qft_circuit.depth()}
    """
    ax7.text(0.05, 0.95, stats_text, fontsize=11, color='lightblue', 
             transform=ax7.transAxes, verticalalignment='top', family='monospace')
    ax7.set_xlim(0, 1)
    ax7.set_ylim(0, 1)
    ax7.axis('off')
    
    # Quantum gates explanation
    ax8 = plt.subplot(3, 3, 8)
    gates_text = """
Quantum Gates Used:

H (Hadamard): Creates superposition
  |0> -> (|0> + |1>)/sqrt(2)

CNOT (CX): Creates entanglement
  |00> -> |00>, |10> -> |11>

Z: Phase flip gate
  |0> -> |0>, |1> -> -|1>

S: Phase gate (pi/2 rotation)
  |1> -> i|1>

CZ: Controlled-Z gate
  Applies Z to target if control is |1>
    """
    ax8.text(0.05, 0.95, gates_text, fontsize=10, color='lightgreen', 
             transform=ax8.transAxes, verticalalignment='top', family='monospace')
    ax8.set_xlim(0, 1)
    ax8.set_ylim(0, 1)
    ax8.axis('off')
    
    # Applications
    ax9 = plt.subplot(3, 3, 9)
    apps_text = """
Quantum Applications:

* Cryptography: Quantum key distribution,
  breaking RSA encryption

* Optimization: Solving complex 
  optimization problems

* Machine Learning: Quantum neural 
  networks and algorithms

* Chemistry: Molecular simulation 
  and drug discovery

* Finance: Portfolio optimization 
  and risk analysis

* AI: Quantum machine learning 
  and pattern recognition
    """
    ax9.text(0.05, 0.95, apps_text, fontsize=10, color='orange', 
             transform=ax9.transAxes, verticalalignment='top', family='monospace')
    ax9.set_xlim(0, 1)
    ax9.set_ylim(0, 1)
    ax9.axis('off')
    
    plt.tight_layout()
    plt.savefig('quantum_gallery.png', dpi=300, bbox_inches='tight', 
                facecolor='black', edgecolor='none')
    plt.show()
    
    return bell_counts, grover_counts

def main():
    """Main function to run the visual quantum demo"""
    print("🎨 Creating Visual Quantum Circuit Gallery...")
    print("=" * 60)
    
    try:
        bell_counts, grover_counts = visualize_quantum_gallery()
        
        print("\n✨ Visual gallery created successfully!")
        print("📊 Saved as 'quantum_gallery.png'")
        
        print(f"\n🔬 Bell State Results: {bell_counts}")
        print(f"🔍 Grover Results: {grover_counts}")
        
        print("\n🌟 Key Observations:")
        print("• Bell state shows perfect entanglement (only |00⟩ and |11⟩)")
        print("• Grover's algorithm amplifies the |11⟩ state probability")
        print("• Quantum circuits demonstrate superposition and interference")
        
    except Exception as e:
        print(f"Error creating visual gallery: {e}")
        print("Please ensure all required packages are installed:")
        print("pip install qiskit qiskit-aer matplotlib pylatexenc")

if __name__ == "__main__":
    main()