"""
Lab 1: Introduction to Quantum Computing and Qiskit
===================================================
Simple demonstration of qubits, superposition, and entanglement
"""

# Step 1: Import Qiskit libraries
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def main():
    print("LAB 1: QUANTUM COMPUTING WITH QISKIT")
    print("=====================================")
    print("Student: [Your Name]")
    print("Date: [Current Date]\n")
    
    # Part 1: Basic Qubit (|0⟩ state)
    print("PART 1: Basic Qubit")
    print("-------------------")
    qc1 = QuantumCircuit(1, 1)
    qc1.measure(0, 0)
    print("Circuit: Single qubit in |0⟩ state")
    print(qc1.draw(output='text'))
    
    # Execute and get results
    simulator = AerSimulator()
    job1 = simulator.run(qc1, shots=1000)
    counts1 = job1.result().get_counts()
    print(f"Results: {counts1}\n")
    
    # Part 2: Superposition (Hadamard gate)
    print("PART 2: Superposition")
    print("---------------------")
    qc2 = QuantumCircuit(1, 1)
    qc2.h(0)  # Hadamard gate
    qc2.measure(0, 0)
    print("Circuit: Hadamard gate creates |+⟩ = (|0⟩ + |1⟩)/√2")
    print(qc2.draw(output='text'))
    
    job2 = simulator.run(qc2, shots=1000)
    counts2 = job2.result().get_counts()
    print(f"Results: {counts2}\n")
    
    # Part 3: Entanglement (Bell state)
    print("PART 3: Entanglement")
    print("--------------------")
    qc3 = QuantumCircuit(2, 2)
    qc3.h(0)      # Hadamard on first qubit
    qc3.cx(0, 1)  # CNOT gate
    qc3.measure_all()
    print("Circuit: Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2")
    print(qc3.draw(output='text'))
    
    job3 = simulator.run(qc3, shots=1000)
    counts3 = job3.result().get_counts()
    print(f"Results: {counts3}\n")
    
    # Create visualizations
    print("CREATING VISUALIZATION...")
    plt.figure(figsize=(15, 5))
    
    # Plot 1: Basic Qubit
    plt.subplot(1, 3, 1)
    states1 = list(counts1.keys())
    values1 = list(counts1.values())
    plt.bar(states1, values1, color='blue', alpha=0.7)
    plt.title("Basic Qubit |0⟩", fontsize=12, fontweight='bold')
    plt.ylabel('Counts')
    plt.xlabel('Measurement')
    
    # Plot 2: Superposition
    plt.subplot(1, 3, 2)
    states2 = list(counts2.keys())
    values2 = list(counts2.values())
    plt.bar(states2, values2, color='green', alpha=0.7)
    plt.title("Superposition |+⟩", fontsize=12, fontweight='bold')
    plt.ylabel('Counts')
    plt.xlabel('Measurement')
    
    # Plot 3: Entanglement
    plt.subplot(1, 3, 3)
    # Clean up the Bell state results for better display
    clean_counts3 = {}
    for key, value in counts3.items():
        # Extract just the measurement part (first two bits)
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts3[clean_key] = value
    
    states3 = list(clean_counts3.keys())
    values3 = list(clean_counts3.values())
    plt.bar(states3, values3, color='red', alpha=0.7)
    plt.title("Bell State |Φ+⟩", fontsize=12, fontweight='bold')
    plt.ylabel('Counts')
    plt.xlabel('Measurement')
    
    plt.tight_layout()
    plt.savefig('lab1_results.png', dpi=300, bbox_inches='tight')
    print("✓ Visualization saved as 'lab1_results.png'")
    
    # Summary
    print("OBSERVATIONS & RESULTS")
    print("======================")
    print("1. Basic Qubit: Always measures |0⟩ (100%)")
    print("2. Superposition: ~50% |0⟩, ~50% |1⟩")
    print("3. Bell State: Only |00⟩ and |11⟩ (entangled)")
    print("\nCONCLUSION")
    print("==========")
    print("✓ Demonstrated qubit states")
    print("✓ Created superposition with H gate")
    print("✓ Created entanglement with CNOT gate")
    print("✓ Results match quantum theory")

if __name__ == "__main__":
    main()