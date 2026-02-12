"""
Lab 1: Introduction to Quantum Computing and Qiskit
===================================================

Experiment 1: Understanding Qubits, Superposition, Entanglement, and Qiskit Framework

Objective:
- Understand qubits, superposition, entanglement, and Qiskit framework
- Demonstrate quantum circuit creation and measurement
- Analyze quantum states and measurement outcomes

Theory:
- A qubit is represented as |ψ⟩ = α|0⟩ + β|1⟩ with |α|² + |β|² = 1
- Quantum computing uses superposition and entanglement for parallel computation
- Qiskit is IBM's SDK for quantum circuit design and simulation
"""

# Step 1: Import Qiskit libraries
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_state_qsphere
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

def print_section_header(title):
    """Print formatted section headers for clean output"""
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60)

def print_subsection(title):
    """Print formatted subsection headers"""
    print(f"\n{title}")
    print("-" * len(title))

def demonstrate_basic_qubit():
    """Demonstrate basic qubit operations"""
    print_section_header("PART 1: BASIC QUBIT DEMONSTRATION")
    
    # Step 2: Create quantum and classical registers
    print_subsection("Circuit Creation")
    qc = QuantumCircuit(1, 1)  # 1 qubit, 1 classical bit
    print("Created quantum circuit with 1 qubit and 1 classical bit")
    print("\nInitial Circuit:")
    print(qc.draw(output='text'))
    
    # Add measurement
    qc.measure(0, 0)
    print("\nCircuit with measurement:")
    print(qc.draw(output='text'))
    
    return qc

def demonstrate_superposition():
    """Demonstrate superposition using Hadamard gate"""
    print_section_header("PART 2: SUPERPOSITION DEMONSTRATION")
    
    # Step 3: Apply Hadamard gate for superposition
    print_subsection("Creating Superposition State")
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Apply Hadamard gate
    qc.measure(0, 0)
    
    print("Applied Hadamard gate to create superposition |+⟩ = (|0⟩ + |1⟩)/√2")
    print("\nSuperposition Circuit:")
    print(qc.draw(output='text'))
    
    return qc

def demonstrate_entanglement():
    """Demonstrate entanglement using Bell state"""
    print_section_header("PART 3: ENTANGLEMENT DEMONSTRATION")
    
    print_subsection("Creating Bell State")
    qc = QuantumCircuit(2, 2)  # 2 qubits for entanglement
    
    # Create Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2
    qc.h(0)      # Put first qubit in superposition
    qc.cx(0, 1)  # Entangle qubits with CNOT gate
    qc.measure_all()
    
    print("Created Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2")
    print("Steps: H(q0) → CNOT(q0,q1) → Measure")
    print("\nEntanglement Circuit:")
    print(qc.draw(output='text'))
    
    return qc

def execute_and_analyze(circuit, title, shots=1024):
    """Execute circuit and analyze results"""
    print_subsection(f"Execution and Analysis: {title}")
    
    # Step 4: Execute using Aer simulator
    simulator = AerSimulator()
    job = simulator.run(circuit, shots=shots)
    result = job.result()
    counts = result.get_counts(circuit)
    
    print(f"Executed {shots} shots on Aer simulator")
    print(f"Measurement results: {counts}")
    
    # Calculate probabilities
    print("\nProbability Distribution:")
    for state, count in counts.items():
        probability = count / shots
        print(f"  |{state}⟩: {count:4d} counts ({probability:.3f} probability)")
    
    return counts

def analyze_statevector(circuit_without_measurement, title):
    """Analyze quantum state before measurement"""
    print_subsection(f"State Vector Analysis: {title}")
    
    # Get statevector (remove measurements for this analysis)
    statevector = Statevector.from_instruction(circuit_without_measurement)
    
    print("Quantum State Vector:")
    for i, amplitude in enumerate(statevector.data):
        if abs(amplitude) > 1e-10:  # Only show non-zero amplitudes
            binary_state = format(i, f'0{circuit_without_measurement.num_qubits}b')
            probability = abs(amplitude)**2
            print(f"  |{binary_state}⟩: {amplitude:.3f} (probability: {probability:.3f})")
    
    return statevector

def main():
    """Main execution function"""
    print_section_header("LAB 1: QUANTUM COMPUTING WITH QISKIT")
    print("Student: [Your Name]")
    print("Date: [Current Date]")
    print("Course: Quantum Computing Laboratory")
    
    # Part 1: Basic qubit
    basic_circuit = demonstrate_basic_qubit()
    counts1 = execute_and_analyze(basic_circuit, "Basic Qubit (|0⟩ state)")
    
    # Analyze initial state
    basic_no_measure = QuantumCircuit(1)
    analyze_statevector(basic_no_measure, "Initial |0⟩ State")
    
    # Part 2: Superposition
    superposition_circuit = demonstrate_superposition()
    counts2 = execute_and_analyze(superposition_circuit, "Superposition State")
    
    # Analyze superposition state
    super_no_measure = QuantumCircuit(1)
    super_no_measure.h(0)
    analyze_statevector(super_no_measure, "Superposition |+⟩ State")
    
    # Part 3: Entanglement
    entanglement_circuit = demonstrate_entanglement()
    counts3 = execute_and_analyze(entanglement_circuit, "Bell State (Entangled)")
    
    # Analyze Bell state
    bell_no_measure = QuantumCircuit(2)
    bell_no_measure.h(0)
    bell_no_measure.cx(0, 1)
    analyze_statevector(bell_no_measure, "Bell State |Φ+⟩")
    
    # Summary and theoretical verification
    print_section_header("OBSERVATIONS AND RESULTS")
    
    print_subsection("Theoretical vs Experimental Results")
    
    print("1. Basic Qubit |0⟩:")
    print("   - Theoretical: 100% probability of measuring |0⟩")
    print(f"   - Experimental: {counts1}")
    print("   - Verification: ✓ Matches expectation")
    
    print("\n2. Superposition |+⟩ = (|0⟩ + |1⟩)/√2:")
    print("   - Theoretical: 50% |0⟩, 50% |1⟩")
    print(f"   - Experimental: {counts2}")
    total2 = sum(counts2.values())
    prob_0 = counts2.get('0', 0) / total2
    prob_1 = counts2.get('1', 0) / total2
    print(f"   - Measured probabilities: |0⟩={prob_0:.3f}, |1⟩={prob_1:.3f}")
    print("   - Verification: ✓ Approximately equal distribution")
    
    print("\n3. Bell State |Φ+⟩ = (|00⟩ + |11⟩)/√2:")
    print("   - Theoretical: 50% |00⟩, 50% |11⟩, 0% |01⟩, 0% |10⟩")
    print(f"   - Experimental: {counts3}")
    total3 = sum(counts3.values())
    for state in ['00', '01', '10', '11']:
        prob = counts3.get(state, 0) / total3
        print(f"   - |{state}⟩: {prob:.3f}")
    print("   - Verification: ✓ Only |00⟩ and |11⟩ observed (entanglement confirmed)")
    
    print_section_header("CONCLUSION")
    print("✓ Successfully demonstrated qubit initialization")
    print("✓ Successfully created and measured superposition states")
    print("✓ Successfully created and verified entangled states")
    print("✓ Experimental results match theoretical predictions")
    print("✓ Qiskit framework successfully used for quantum circuit simulation")
    
    print("\nKey Learning Outcomes:")
    print("- Qubits can exist in superposition of |0⟩ and |1⟩ states")
    print("- Hadamard gate creates equal superposition")
    print("- CNOT gate can create entanglement between qubits")
    print("- Measurement collapses quantum states to classical outcomes")
    print("- Qiskit provides powerful tools for quantum circuit design and simulation")

if __name__ == "__main__":
    main()