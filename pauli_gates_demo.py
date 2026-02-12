"""
Pauli Gates Demonstration
Simple execution of Pauli-X, Pauli-Y, and Pauli-Z gates using Qiskit
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np

def demonstrate_pauli_x():
    """Demonstrate Pauli-X gate (bit flip)"""
    print("=" * 60)
    print("🔄 PAULI-X GATE (Bit Flip Gate)")
    print("=" * 60)
    print("Effect: |0⟩ → |1⟩ and |1⟩ → |0⟩")
    print("Matrix: [[0, 1], [1, 0]]")
    
    # Test X gate on |0⟩ state
    circuit_0 = QuantumCircuit(1, 1)
    circuit_0.x(0)  # Apply X gate
    circuit_0.measure(0, 0)
    
    print(f"\n🎨 Circuit (starting from |0⟩):")
    print(circuit_0)
    
    # Simulate
    simulator = AerSimulator()
    job = simulator.run(circuit_0, shots=1000)
    counts_0 = job.result().get_counts()
    
    print(f"📊 Results starting from |0⟩:")
    for state, count in counts_0.items():
        print(f"   |{state}⟩: {count} times (should be 1000 times |1⟩)")
    
    # Test X gate on |1⟩ state (start with X to get |1⟩, then apply X again)
    circuit_1 = QuantumCircuit(1, 1)
    circuit_1.x(0)  # First X: |0⟩ → |1⟩
    circuit_1.x(0)  # Second X: |1⟩ → |0⟩
    circuit_1.measure(0, 0)
    
    print(f"\n🎨 Circuit (X applied twice):")
    print(circuit_1)
    
    job = simulator.run(circuit_1, shots=1000)
    counts_1 = job.result().get_counts()
    
    print(f"📊 Results after two X gates:")
    for state, count in counts_1.items():
        print(f"   |{state}⟩: {count} times (should be 1000 times |0⟩)")

def demonstrate_pauli_y():
    """Demonstrate Pauli-Y gate (bit and phase flip)"""
    print("\n" + "=" * 60)
    print("🌀 PAULI-Y GATE (Bit + Phase Flip Gate)")
    print("=" * 60)
    print("Effect: |0⟩ → i|1⟩ and |1⟩ → -i|0⟩")
    print("Matrix: [[0, -i], [i, 0]]")
    
    # Y gate on |0⟩
    circuit_y = QuantumCircuit(1, 1)
    circuit_y.y(0)  # Apply Y gate
    circuit_y.measure(0, 0)
    
    print(f"\n🎨 Circuit (Y gate on |0⟩):")
    print(circuit_y)
    
    simulator = AerSimulator()
    job = simulator.run(circuit_y, shots=1000)
    counts_y = job.result().get_counts()
    
    print(f"📊 Results after Y gate on |0⟩:")
    for state, count in counts_y.items():
        print(f"   |{state}⟩: {count} times (should be 1000 times |1⟩)")
    
    # Y gate applied twice (should return to |0⟩ with phase change)
    circuit_y2 = QuantumCircuit(1, 1)
    circuit_y2.y(0)  # First Y: |0⟩ → i|1⟩
    circuit_y2.y(0)  # Second Y: i|1⟩ → i(-i|0⟩) = |0⟩
    circuit_y2.measure(0, 0)
    
    print(f"\n🎨 Circuit (Y gate applied twice):")
    print(circuit_y2)
    
    job = simulator.run(circuit_y2, shots=1000)
    counts_y2 = job.result().get_counts()
    
    print(f"📊 Results after two Y gates:")
    for state, count in counts_y2.items():
        print(f"   |{state}⟩: {count} times (should be 1000 times |0⟩)")

def demonstrate_pauli_z():
    """Demonstrate Pauli-Z gate (phase flip)"""
    print("\n" + "=" * 60)
    print("⚡ PAULI-Z GATE (Phase Flip Gate)")
    print("=" * 60)
    print("Effect: |0⟩ → |0⟩ and |1⟩ → -|1⟩")
    print("Matrix: [[1, 0], [0, -1]]")
    
    # Z gate on |0⟩ (no visible effect in measurement)
    circuit_z0 = QuantumCircuit(1, 1)
    circuit_z0.z(0)  # Apply Z gate to |0⟩
    circuit_z0.measure(0, 0)
    
    print(f"\n🎨 Circuit (Z gate on |0⟩):")
    print(circuit_z0)
    
    simulator = AerSimulator()
    job = simulator.run(circuit_z0, shots=1000)
    counts_z0 = job.result().get_counts()
    
    print(f"📊 Results after Z gate on |0⟩:")
    for state, count in counts_z0.items():
        print(f"   |{state}⟩: {count} times (Z has no effect on |0⟩)")
    
    # Z gate on |1⟩ (phase flip, but not visible in direct measurement)
    circuit_z1 = QuantumCircuit(1, 1)
    circuit_z1.x(0)  # First create |1⟩
    circuit_z1.z(0)  # Apply Z gate: |1⟩ → -|1⟩
    circuit_z1.measure(0, 0)
    
    print(f"\n🎨 Circuit (Z gate on |1⟩):")
    print(circuit_z1)
    
    job = simulator.run(circuit_z1, shots=1000)
    counts_z1 = job.result().get_counts()
    
    print(f"📊 Results after Z gate on |1⟩:")
    for state, count in counts_z1.items():
        print(f"   |{state}⟩: {count} times (still measures as |1⟩, but with -1 phase)")

def demonstrate_z_phase_effect():
    """Show the phase effect of Z gate using interference"""
    print("\n" + "=" * 60)
    print("🔬 DEMONSTRATING Z GATE PHASE EFFECT")
    print("=" * 60)
    print("Using interference to show the phase change")
    
    # Circuit without Z gate
    circuit_no_z = QuantumCircuit(1, 1)
    circuit_no_z.h(0)  # Create superposition
    circuit_no_z.h(0)  # Second H should return to |0⟩
    circuit_no_z.measure(0, 0)
    
    print(f"\n🎨 Circuit (H-H, no Z gate):")
    print(circuit_no_z)
    
    simulator = AerSimulator()
    job = simulator.run(circuit_no_z, shots=1000)
    counts_no_z = job.result().get_counts()
    
    print(f"📊 Results H-H (should be all |0⟩):")
    for state, count in counts_no_z.items():
        print(f"   |{state}⟩: {count} times")
    
    # Circuit with Z gate in between
    circuit_with_z = QuantumCircuit(1, 1)
    circuit_with_z.h(0)  # Create superposition: (|0⟩ + |1⟩)/√2
    circuit_with_z.z(0)  # Apply phase: (|0⟩ - |1⟩)/√2
    circuit_with_z.h(0)  # Second H: should give |1⟩
    circuit_with_z.measure(0, 0)
    
    print(f"\n🎨 Circuit (H-Z-H):")
    print(circuit_with_z)
    
    job = simulator.run(circuit_with_z, shots=1000)
    counts_with_z = job.result().get_counts()
    
    print(f"📊 Results H-Z-H (should be all |1⟩):")
    for state, count in counts_with_z.items():
        print(f"   |{state}⟩: {count} times")
    
    print(f"\n💡 EXPLANATION:")
    print("   • H-H: (|0⟩ + |1⟩)/√2 → |0⟩ (constructive interference)")
    print("   • H-Z-H: (|0⟩ - |1⟩)/√2 → |1⟩ (destructive interference)")
    print("   • The Z gate flipped the phase, changing the interference!")

def compare_all_pauli_gates():
    """Compare all three Pauli gates side by side"""
    print("\n" + "=" * 60)
    print("📊 PAULI GATES COMPARISON")
    print("=" * 60)
    
    gates = [
        ("Identity (no gate)", ""),
        ("Pauli-X", "x"),
        ("Pauli-Y", "y"), 
        ("Pauli-Z", "z")
    ]
    
    simulator = AerSimulator()
    
    for gate_name, gate_op in gates:
        # Test on |0⟩ state
        circuit = QuantumCircuit(1, 1)
        if gate_op:
            getattr(circuit, gate_op)(0)  # Apply the gate
        circuit.measure(0, 0)
        
        job = simulator.run(circuit, shots=1000)
        counts = job.result().get_counts()
        
        result_0 = counts.get('0', 0)
        result_1 = counts.get('1', 0)
        
        print(f"{gate_name:15} on |0⟩: |0⟩={result_0:4d}, |1⟩={result_1:4d}")

def main():
    """Main function to run all Pauli gate demonstrations"""
    
    print("🌟 PAULI GATES DEMONSTRATION 🌟")
    print("The three fundamental single-qubit quantum gates")
    
    # Demonstrate each Pauli gate
    demonstrate_pauli_x()
    demonstrate_pauli_y() 
    demonstrate_pauli_z()
    
    # Show Z gate phase effect through interference
    demonstrate_z_phase_effect()
    
    # Compare all gates
    compare_all_pauli_gates()
    
    print("\n" + "=" * 60)
    print("🎯 KEY TAKEAWAYS")
    print("=" * 60)
    print("• Pauli-X: Flips bit (|0⟩ ↔ |1⟩) - like classical NOT gate")
    print("• Pauli-Y: Flips bit AND adds phase (complex rotation)")
    print("• Pauli-Z: Flips phase only (|1⟩ → -|1⟩) - invisible in direct measurement")
    print("• Phase effects become visible through quantum interference")
    print("• These gates are building blocks for all quantum algorithms")
    print("=" * 60)

if __name__ == "__main__":
    main()