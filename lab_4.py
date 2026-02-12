"""
Lab 4: Creating a Simple Quantum Circuit
========================================
Objective: Design and simulate a basic quantum circuit
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def main():
    print("LAB 4: CREATING A SIMPLE QUANTUM CIRCUIT")
    print("=========================================")
    print()
    
    # Initialize simulator
    simulator = AerSimulator()
    
    # PART 1: Basic Circuit Creation
    print("PART 1: Basic Circuit with X Gate")
    print("---------------------------------")
    qc1 = QuantumCircuit(1, 1)
    qc1.x(0)  # X gate (NOT gate)
    qc1.measure(0, 0)
    print("Circuit: X gate followed by measurement")
    print(qc1.draw(output='text'))
    
    job1 = simulator.run(qc1, shots=1000)
    counts1 = job1.result().get_counts()
    print(f"Results: {counts1}")
    print()
    
    # PART 2: Circuit with Y Gate
    print("PART 2: Circuit with Y Gate")
    print("---------------------------")
    qc2 = QuantumCircuit(1, 1)
    qc2.y(0)  # Y gate
    qc2.measure(0, 0)
    print("Circuit: Y gate followed by measurement")
    print(qc2.draw(output='text'))
    
    job2 = simulator.run(qc2, shots=1000)
    counts2 = job2.result().get_counts()
    print(f"Results: {counts2}")
    print()
    
    # PART 3: Circuit with Z Gate
    print("PART 3: Circuit with Z Gate")
    print("---------------------------")
    qc3 = QuantumCircuit(1, 1)
    qc3.z(0)  # Z gate
    qc3.measure(0, 0)
    print("Circuit: Z gate followed by measurement")
    print(qc3.draw(output='text'))
    
    job3 = simulator.run(qc3, shots=1000)
    counts3 = job3.result().get_counts()
    print(f"Results: {counts3}")
    print()
    
    # PART 4: Multi-Gate Circuit
    print("PART 4: Multi-Gate Circuit")
    print("--------------------------")
    qc4 = QuantumCircuit(1, 1)
    qc4.h(0)  # Hadamard gate
    qc4.x(0)  # X gate
    qc4.measure(0, 0)
    print("Circuit: H gate then X gate")
    print(qc4.draw(output='text'))
    
    job4 = simulator.run(qc4, shots=1000)
    counts4 = job4.result().get_counts()
    print(f"Results: {counts4}")
    print()
    
    # Create compact visualization
    fig, axes = plt.subplots(2, 4, figsize=(14, 8))
    fig.suptitle('Lab 4: Simple Quantum Circuits', fontsize=14, fontweight='bold', y=0.95)
    
    # Circuit data
    circuits = [
        ("X Gate", "     ┌───┐┌─┐\n  q: ┤ X ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0", counts1, 'lightblue'),
        ("Y Gate", "     ┌───┐┌─┐\n  q: ┤ Y ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0", counts2, 'lightgreen'),
        ("Z Gate", "     ┌───┐┌─┐\n  q: ┤ Z ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0", counts3, 'lightyellow'),
        ("H+X Gates", "     ┌───┐┌───┐┌─┐\n  q: ┤ H ├┤ X ├┤M├\n     └───┘└───┘└╥┘\nc: 1/═══════════╩═\n               0", counts4, 'lightsalmon')
    ]
    
    # Top row: Circuit diagrams
    for i, (title, circuit, counts, color) in enumerate(circuits):
        ax = axes[0, i]
        ax.text(0.5, 0.9, title, ha='center', fontsize=10, fontweight='bold', transform=ax.transAxes)
        ax.text(0.5, 0.5, circuit, ha='center', fontsize=7, fontfamily='monospace', 
                transform=ax.transAxes, bbox=dict(boxstyle="round,pad=0.1", facecolor=color, alpha=0.4))
        ax.text(0.5, 0.05, f'{counts}', ha='center', fontsize=8, fontweight='bold', transform=ax.transAxes)
        ax.axis('off')
    
    # Bottom row: Bar charts
    test_results = [counts1, counts2, counts3, counts4]
    colors = ['skyblue', 'lightgreen', 'gold', 'salmon']
    titles = ['X Gate', 'Y Gate', 'Z Gate', 'H+X Gates']
    
    for i, (counts, color, title) in enumerate(zip(test_results, colors, titles)):
        ax = axes[1, i]
        bars = ax.bar(counts.keys(), counts.values(), color=color, alpha=0.8, edgecolor='black', linewidth=1)
        ax.set_title(title, fontweight='bold', fontsize=9)
        ax.set_ylabel('Counts', fontsize=8)
        ax.tick_params(labelsize=7)
        
        # Add count labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(counts.values())*0.02,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=8)
    
    # Add compact summary
    fig.text(0.5, 0.08, 'QUANTUM GATES: X (NOT) | Y (Pauli-Y) | Z (Phase) | H+X (Composite)', 
             ha='center', fontsize=10, bbox=dict(boxstyle="round,pad=0.2", facecolor="lightcyan", edgecolor="teal"))
    fig.text(0.5, 0.03, 'UNITARY OPERATIONS: ✓ Single Gates ✓ Gate Sequences ✓ Measurement ✓ Classical Output', 
             ha='center', fontsize=10, fontweight='bold', color='darkblue')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.88, bottom=0.15, hspace=0.1, wspace=0.2)
    plt.savefig('qiskit_lab_4_final_image.png', dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.05)
    plt.show()
    
    print("CIRCUIT ANALYSIS COMPLETE")
    print("=========================")
    print("✓ X Gate: Flips |0⟩ to |1⟩ (bit flip)")
    print("✓ Y Gate: Complex rotation (flips + phase)")
    print("✓ Z Gate: Phase flip (|0⟩ unchanged, |1⟩ → -|1⟩)")
    print("✓ H+X: Composite operation (superposition then flip)")
    print()
    print("THEORETICAL VERIFICATION:")
    print("=========================")
    print("• X|0⟩ = |1⟩ → Always measures 1")
    print("• Y|0⟩ = i|1⟩ → Always measures 1 (phase ignored)")
    print("• Z|0⟩ = |0⟩ → Always measures 0")
    print("• H+X creates |-⟩ state → Always measures 0")
    print()
    print("CONCLUSION:")
    print("===========")
    print("✓ Quantum circuits are sequences of unitary gates")
    print("✓ Gates transform quantum states deterministically")
    print("✓ Measurement collapses superposition to classical bits")
    print("✓ Visualization saved as 'qiskit_lab_4_final_image.png'")

if __name__ == "__main__":
    main()