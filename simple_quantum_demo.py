"""
Simple Quantum Circuit Demo
Beautiful quantum circuits with text-based visualization
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np

def create_bell_state_circuit():
    """
    Creates a Bell state quantum circuit - demonstrates quantum entanglement
    This creates the famous |Φ+⟩ = (|00⟩ + |11⟩)/√2 state
    """
    qreg = QuantumRegister(2, 'q')
    creg = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg, creg)
    
    # Add barriers for visual clarity
    circuit.barrier()
    
    # Create superposition on first qubit
    circuit.h(qreg[0])  # Hadamard gate: |0⟩ → (|0⟩ + |1⟩)/√2
    
    # Create entanglement between qubits
    circuit.cx(qreg[0], qreg[1])  # CNOT gate: creates entanglement
    
    circuit.barrier()
    
    # Measure both qubits
    circuit.measure(qreg, creg)
    
    return circuit

def create_superposition_circuit():
    """
    Creates a simple superposition circuit on 3 qubits
    """
    qreg = QuantumRegister(3, 'q')
    creg = ClassicalRegister(3, 'c')
    circuit = QuantumCircuit(qreg, creg)
    
    # Put all qubits in superposition
    circuit.h(qreg[0])
    circuit.h(qreg[1])
    circuit.h(qreg[2])
    
    # Add some phase gates for visual interest
    circuit.s(qreg[1])  # S gate (phase gate)
    circuit.t(qreg[2])  # T gate (π/8 gate)
    
    # Measure all qubits
    circuit.measure(qreg, creg)
    
    return circuit

def create_quantum_fourier_transform():
    """
    Creates a 3-qubit Quantum Fourier Transform circuit
    """
    n_qubits = 3
    qreg = QuantumRegister(n_qubits, 'q')
    circuit = QuantumCircuit(qreg)
    
    # QFT implementation
    for i in range(n_qubits):
        circuit.h(qreg[i])
        for j in range(i + 1, n_qubits):
            circuit.cp(np.pi / (2 ** (j - i)), qreg[j], qreg[i])
    
    # Swap qubits to reverse the order
    for i in range(n_qubits // 2):
        circuit.swap(qreg[i], qreg[n_qubits - 1 - i])
    
    return circuit

def simulate_circuit(circuit, shots=1000):
    """
    Simulate a quantum circuit and return the results
    """
    simulator = AerSimulator()
    job = simulator.run(circuit, shots=shots)
    result = job.result()
    counts = result.get_counts()
    return counts

def print_circuit_info(circuit, name):
    """
    Print detailed information about a quantum circuit
    """
    print(f"\n{'='*60}")
    print(f"🌟 {name} 🌟")
    print(f"{'='*60}")
    print(f"📊 Circuit Statistics:")
    print(f"   • Qubits: {circuit.num_qubits}")
    print(f"   • Classical bits: {circuit.num_clbits}")
    print(f"   • Gates: {len(circuit.data)}")
    print(f"   • Depth: {circuit.depth()}")
    print(f"\n🎨 Circuit Diagram:")
    print(circuit)
    
    # If circuit has measurements, simulate it
    if circuit.num_clbits > 0:
        print(f"\n🔬 Simulation Results (1000 shots):")
        counts = simulate_circuit(circuit)
        total_shots = sum(counts.values())
        
        # Sort results by count (descending)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        for state, count in sorted_counts:
            probability = count / total_shots
            bar_length = int(probability * 40)  # Scale bar to 40 characters
            bar = "█" * bar_length + "░" * (40 - bar_length)
            print(f"   |{state}⟩: {count:4d} ({probability:.1%}) {bar}")

def main():
    """
    Main function to demonstrate quantum circuits
    """
    print("🚀 Welcome to the Quantum Circuit Gallery! 🚀")
    print("Exploring the beautiful world of quantum computing...")
    
    # Create and display Bell State Circuit
    bell_circuit = create_bell_state_circuit()
    print_circuit_info(bell_circuit, "Bell State Circuit (Quantum Entanglement)")
    print("\n💡 This circuit creates quantum entanglement between two qubits.")
    print("   The measurement results will only show |00⟩ and |11⟩ states!")
    
    # Create and display Superposition Circuit
    superposition_circuit = create_superposition_circuit()
    print_circuit_info(superposition_circuit, "3-Qubit Superposition Circuit")
    print("\n💡 This circuit puts 3 qubits in superposition with phase gates.")
    print("   You should see all 8 possible states (000 to 111) with equal probability!")
    
    # Create and display QFT Circuit (no measurements for clarity)
    qft_circuit = create_quantum_fourier_transform()
    print_circuit_info(qft_circuit, "Quantum Fourier Transform (3-qubit)")
    print("\n💡 The QFT is a key component in many quantum algorithms like Shor's algorithm.")
    print("   This transforms the computational basis to the Fourier basis.")
    
    # Create a simple demonstration circuit
    demo_circuit = QuantumCircuit(2, 2)
    demo_circuit.h(0)  # Superposition
    demo_circuit.cx(0, 1)  # Entanglement
    demo_circuit.measure_all()  # Measure everything
    
    print_circuit_info(demo_circuit, "Simple Demo Circuit")
    print("\n💡 This is the simplest example of quantum entanglement!")
    
    print(f"\n{'='*60}")
    print("🎉 Quantum Circuit Gallery Complete! 🎉")
    print("Key Quantum Concepts Demonstrated:")
    print("   🔸 Superposition (H gates)")
    print("   🔸 Entanglement (CNOT gates)")
    print("   🔸 Phase manipulation (S, T gates)")
    print("   🔸 Quantum algorithms (QFT)")
    print("   🔸 Measurement and classical output")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()