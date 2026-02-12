"""
Lab 6: Single-Qubit Gates: Pauli-X, Y, Z
========================================
Objective: Apply Pauli gates and observe transformations
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def main():
    print("LAB 6: SINGLE-QUBIT GATES: PAULI-X, Y, Z")
    print("=========================================")
    print()
    
    # Initialize simulator
    simulator = AerSimulator()
    
    # PART 1: Pauli-X Gate
    print("PART 1: Pauli-X Gate")
    print("--------------------")
    qc1 = QuantumCircuit(1, 1)
    qc1.x(0)  # Pauli-X gate
    qc1.measure(0, 0)
    print("Circuit: X gate (bit flip)")
    print(qc1.draw(output='text'))
    
    job1 = simulator.run(qc1, shots=1000)
    counts1 = job1.result().get_counts()
    print(f"Results: {counts1}")
    print("Effect: |0⟩ → |1⟩ (bit flip)")
    print()
    
    # PART 2: Pauli-Y Gate
    print("PART 2: Pauli-Y Gate")
    print("--------------------")
    qc2 = QuantumCircuit(1, 1)
    qc2.y(0)  # Pauli-Y gate
    qc2.measure(0, 0)
    print("Circuit: Y gate (bit + phase flip)")
    print(qc2.draw(output='text'))
    
    job2 = simulator.run(qc2, shots=1000)
    counts2 = job2.result().get_counts()
    print(f"Results: {counts2}")
    print("Effect: |0⟩ → i|1⟩ (bit flip + phase)")
    print()
    
    # PART 3: Pauli-Z Gate
    print("PART 3: Pauli-Z Gate")
    print("--------------------")
    qc3 = QuantumCircuit(1, 1)
    qc3.z(0)  # Pauli-Z gate
    qc3.measure(0, 0)
    print("Circuit: Z gate (phase flip)")
    print(qc3.draw(output='text'))
    
    job3 = simulator.run(qc3, shots=1000)
    counts3 = job3.result().get_counts()
    print(f"Results: {counts3}")
    print("Effect: |0⟩ → |0⟩, |1⟩ → -|1⟩ (phase flip)")
    print()
    
    # PART 4: Combined Operations
    print("PART 4: Combined Pauli Operations")
    print("---------------------------------")
    qc4 = QuantumCircuit(1, 1)
    qc4.h(0)    # Create superposition
    qc4.x(0)    # Apply X gate
    qc4.measure(0, 0)
    print("Circuit: H then X (superposition + bit flip)")
    print(qc4.draw(output='text'))
    
    job4 = simulator.run(qc4, shots=1000)
    counts4 = job4.result().get_counts()
    print(f"Results: {counts4}")
    print("Effect: H|0⟩ = |+⟩, then X|+⟩ = |+⟩ (still superposition)")
    print()
    
    # Create proper visualization
    fig, axes = plt.subplots(2, 4, figsize=(16, 10))
    fig.suptitle('Lab 6: Pauli Gates Transformations', fontsize=16, fontweight='bold', y=0.95)
    
    # Circuit data
    circuits = [
        ("Pauli-X Gate", "     ┌───┐┌─┐\n  q: ┤ X ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0", counts1, 'lightblue'),
        ("Pauli-Y Gate", "     ┌───┐┌─┐\n  q: ┤ Y ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0", counts2, 'lightgreen'),
        ("Pauli-Z Gate", "     ┌───┐┌─┐\n  q: ┤ Z ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0", counts3, 'lightyellow'),
        ("H + X Gates", "     ┌───┐┌───┐┌─┐\n  q: ┤ H ├┤ X ├┤M├\n     └───┘└───┘└╥┘\nc: 1/═══════════╩═\n               0", counts4, 'lightsalmon')
    ]
    
    # Top row: Circuit diagrams
    for i, (title, circuit, counts, color) in enumerate(circuits):
        ax = axes[0, i]
        ax.text(0.5, 0.9, title, ha='center', fontsize=11, fontweight='bold', transform=ax.transAxes)
        ax.text(0.5, 0.5, circuit, ha='center', fontsize=8, fontfamily='monospace', 
                transform=ax.transAxes, bbox=dict(boxstyle="round,pad=0.1", facecolor=color, alpha=0.4))
        ax.text(0.5, 0.05, f'{counts}', ha='center', fontsize=9, fontweight='bold', transform=ax.transAxes)
        ax.axis('off')
    
    # Bottom row: Proper bar charts
    test_results = [counts1, counts2, counts3, counts4]
    colors = ['skyblue', 'lightgreen', 'gold', 'salmon']
    titles = ['X Gate Results', 'Y Gate Results', 'Z Gate Results', 'H+X Results']
    
    for i, (counts, color, title) in enumerate(zip(test_results, colors, titles)):
        ax = axes[1, i]
        
        # Create proper bar chart
        states = list(counts.keys())
        values = list(counts.values())
        bars = ax.bar(states, values, color=color, alpha=0.8, edgecolor='black', linewidth=1)
        
        ax.set_title(title, fontweight='bold', fontsize=10)
        ax.set_ylabel('Counts', fontsize=9)
        ax.set_xlabel('Measurement', fontsize=9)
        ax.tick_params(labelsize=8)
        
        # Set consistent y-axis limits
        ax.set_ylim(0, 1100)
        
        # Add count labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 20,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        # Add grid for better readability
        ax.grid(True, alpha=0.3, axis='y')
    
    # Add comprehensive theory summary
    fig.text(0.5, 0.08, 'PAULI GATES THEORY: X (σₓ) flips |0⟩↔|1⟩ | Y (σᵧ) = iXZ combines bit+phase flip | Z (σᵤ) adds phase: |1⟩→-|1⟩', 
             ha='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcyan", edgecolor="teal"))
    fig.text(0.5, 0.03, 'MATRIX EFFECTS: X=[0,1;1,0] | Y=[0,-i;i,0] | Z=[1,0;0,-1] | All are unitary and Hermitian', 
             ha='center', fontsize=10, fontweight='bold', color='darkblue')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.88, bottom=0.15, hspace=0.3, wspace=0.2)
    plt.savefig('qiskit_lab_6_final_image.png', dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.05)
    plt.show()
    
    print("PAULI GATES ANALYSIS COMPLETE")
    print("==============================")
    print("✓ Pauli-X: Bit flip transformation |0⟩ ↔ |1⟩")
    print("✓ Pauli-Y: Combined bit and phase flip")
    print("✓ Pauli-Z: Phase flip only (|0⟩ unchanged)")
    print("✓ Combined operations demonstrate gate composition")
    print()
    print("THEORETICAL VERIFICATION:")
    print("=========================")
    print("• X|0⟩ = |1⟩ → Always measures 1")
    print("• Y|0⟩ = i|1⟩ → Always measures 1 (phase ignored)")
    print("• Z|0⟩ = |0⟩ → Always measures 0")
    print("• H+X creates superposition that remains balanced")
    print()
    print("CONCLUSION:")
    print("===========")
    print("✓ Pauli gates are fundamental single-qubit operations")
    print("✓ Each gate has distinct transformation properties")
    print("✓ Gates can be combined for complex operations")
    print("✓ Visualization saved as 'qiskit_lab_6_final_image.png'")

if __name__ == "__main__":
    main()