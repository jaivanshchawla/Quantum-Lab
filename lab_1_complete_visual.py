"""
Lab 1: Complete Visual Output - Circuits + Results
==================================================
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from qiskit.visualization import circuit_drawer
import matplotlib.patches as patches

def create_complete_visualization():
    # Initialize simulator
    simulator = AerSimulator()
    
    # PART 1: Basic Qubit |0⟩
    qc1 = QuantumCircuit(1, 1)
    qc1.measure(0, 0)
    job1 = simulator.run(qc1, shots=1000)
    counts1 = job1.result().get_counts()
    
    # PART 2: Superposition |+⟩
    qc2 = QuantumCircuit(1, 1)
    qc2.h(0)
    qc2.measure(0, 0)
    job2 = simulator.run(qc2, shots=1000)
    counts2 = job2.result().get_counts()
    
    # PART 3: Bell State |Φ+⟩
    qc3 = QuantumCircuit(2, 2)
    qc3.h(0)
    qc3.cx(0, 1)
    qc3.measure_all()
    job3 = simulator.run(qc3, shots=1000)
    counts3 = job3.result().get_counts()
    
    # Clean up Bell state results
    clean_counts3 = {}
    for key, value in counts3.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts3[clean_key] = value
    
    # Create the complete visualization
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('Lab 1: Quantum Computing with Qiskit - Complete Results', 
                 fontsize=16, fontweight='bold', y=0.95)
    
    # Add student info
    fig.text(0.5, 0.92, 'Student: [Your Name] | Date: [Current Date]', 
             ha='center', fontsize=12)
    
    # PART 1: Basic Qubit
    # Circuit diagram
    ax1_circuit = plt.subplot(3, 3, 1)
    ax1_circuit.text(0.5, 0.8, 'PART 1: Basic Qubit |0⟩', 
                     ha='center', fontsize=12, fontweight='bold', transform=ax1_circuit.transAxes)
    ax1_circuit.text(0.5, 0.6, 'Circuit:', ha='center', fontsize=10, transform=ax1_circuit.transAxes)
    ax1_circuit.text(0.5, 0.4, '     ┌─┐\n  q: ┤M├\n     └╥┘\nc: 1/═╩═\n      0', 
                     ha='center', fontsize=8, fontfamily='monospace', transform=ax1_circuit.transAxes)
    ax1_circuit.axis('off')
    
    # Results text
    ax1_text = plt.subplot(3, 3, 2)
    ax1_text.text(0.5, 0.8, 'Results:', ha='center', fontsize=12, fontweight='bold', transform=ax1_text.transAxes)
    ax1_text.text(0.5, 0.6, f"{counts1}", ha='center', fontsize=11, transform=ax1_text.transAxes)
    ax1_text.text(0.5, 0.4, 'Always measures |0⟩\n(100% deterministic)', 
                  ha='center', fontsize=10, transform=ax1_text.transAxes)
    ax1_text.axis('off')
    
    # Bar plot
    ax1_bar = plt.subplot(3, 3, 3)
    bars1 = ax1_bar.bar(counts1.keys(), counts1.values(), color='skyblue', alpha=0.8)
    ax1_bar.set_title('Measurement Counts', fontweight='bold')
    ax1_bar.set_ylabel('Counts')
    ax1_bar.set_ylim(0, 1100)
    for bar in bars1:
        height = bar.get_height()
        ax1_bar.text(bar.get_x() + bar.get_width()/2., height + 10,
                     f'{int(height)}', ha='center', va='bottom')
    
    # PART 2: Superposition
    # Circuit diagram
    ax2_circuit = plt.subplot(3, 3, 4)
    ax2_circuit.text(0.5, 0.8, 'PART 2: Superposition |+⟩', 
                     ha='center', fontsize=12, fontweight='bold', transform=ax2_circuit.transAxes)
    ax2_circuit.text(0.5, 0.6, 'Circuit:', ha='center', fontsize=10, transform=ax2_circuit.transAxes)
    ax2_circuit.text(0.5, 0.4, '     ┌───┐┌─┐\n  q: ┤ H ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0', 
                     ha='center', fontsize=8, fontfamily='monospace', transform=ax2_circuit.transAxes)
    ax2_circuit.axis('off')
    
    # Results text
    ax2_text = plt.subplot(3, 3, 5)
    ax2_text.text(0.5, 0.8, 'Results:', ha='center', fontsize=12, fontweight='bold', transform=ax2_text.transAxes)
    ax2_text.text(0.5, 0.6, f"{counts2}", ha='center', fontsize=11, transform=ax2_text.transAxes)
    ax2_text.text(0.5, 0.4, '~50% |0⟩, ~50% |1⟩\n(Quantum superposition)', 
                  ha='center', fontsize=10, transform=ax2_text.transAxes)
    ax2_text.axis('off')
    
    # Bar plot
    ax2_bar = plt.subplot(3, 3, 6)
    bars2 = ax2_bar.bar(counts2.keys(), counts2.values(), color='lightgreen', alpha=0.8)
    ax2_bar.set_title('Measurement Counts', fontweight='bold')
    ax2_bar.set_ylabel('Counts')
    ax2_bar.set_ylim(0, 600)
    for bar in bars2:
        height = bar.get_height()
        ax2_bar.text(bar.get_x() + bar.get_width()/2., height + 10,
                     f'{int(height)}', ha='center', va='bottom')
    
    # PART 3: Bell State
    # Circuit diagram
    ax3_circuit = plt.subplot(3, 3, 7)
    ax3_circuit.text(0.5, 0.9, 'PART 3: Bell State |Φ+⟩', 
                     ha='center', fontsize=12, fontweight='bold', transform=ax3_circuit.transAxes)
    ax3_circuit.text(0.5, 0.75, 'Circuit:', ha='center', fontsize=10, transform=ax3_circuit.transAxes)
    ax3_circuit.text(0.5, 0.45, '        ┌───┐     \n   q_0: ┤ H ├──■──\n        └───┘┌─┴─┐\n   q_1: ─────┤ X ├\n             └───┘\n   measure_all()', 
                     ha='center', fontsize=8, fontfamily='monospace', transform=ax3_circuit.transAxes)
    ax3_circuit.axis('off')
    
    # Results text
    ax3_text = plt.subplot(3, 3, 8)
    ax3_text.text(0.5, 0.8, 'Results:', ha='center', fontsize=12, fontweight='bold', transform=ax3_text.transAxes)
    ax3_text.text(0.5, 0.6, f"{clean_counts3}", ha='center', fontsize=11, transform=ax3_text.transAxes)
    ax3_text.text(0.5, 0.4, 'Only |00⟩ and |11⟩\n(Quantum entanglement)', 
                  ha='center', fontsize=10, transform=ax3_text.transAxes)
    ax3_text.axis('off')
    
    # Bar plot
    ax3_bar = plt.subplot(3, 3, 9)
    bars3 = ax3_bar.bar(clean_counts3.keys(), clean_counts3.values(), color='salmon', alpha=0.8)
    ax3_bar.set_title('Measurement Counts', fontweight='bold')
    ax3_bar.set_ylabel('Counts')
    ax3_bar.set_ylim(0, 600)
    for bar in bars3:
        height = bar.get_height()
        ax3_bar.text(bar.get_x() + bar.get_width()/2., height + 10,
                     f'{int(height)}', ha='center', va='bottom')
    
    # Add summary box at the bottom
    fig.text(0.5, 0.08, 'OBSERVATIONS: Basic Qubit (deterministic) | Superposition (random 50/50) | Bell State (entangled correlations)', 
             ha='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
    fig.text(0.5, 0.04, 'CONCLUSION: ✓ Demonstrated quantum superposition ✓ Demonstrated quantum entanglement ✓ Results match theory', 
             ha='center', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.88, bottom=0.12)
    plt.savefig('lab1_complete_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Complete visualization saved as 'lab1_complete_visualization.png'")
    print("✓ This single image contains all circuits, results, and bar plots")

if __name__ == "__main__":
    create_complete_visualization()