"""
Lab 1: Ultra-Compact Visualization
==================================
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def main():
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
    
    # Create ultra-compact visualization
    fig, axes = plt.subplots(2, 3, figsize=(12, 6))
    fig.suptitle('Lab 1: Quantum Computing with Qiskit', fontsize=14, fontweight='bold', y=0.98)
    
    # Flatten axes for easier indexing
    ax = axes.flatten()
    
    # Top row: Circuits with results
    circuits = [
        ("Basic Qubit |0⟩", "     ┌─┐\n  q: ┤M├\n     └╥┘\nc: 1/═╩═\n      0", counts1, 'lightblue'),
        ("Superposition |+⟩", "     ┌───┐┌─┐\n  q: ┤ H ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0", counts2, 'lightgreen'),
        ("Bell State |Φ+⟩", "        ┌───┐\n   q_0: ┤ H ├──■──\n        └───┘┌─┴─┐\n   q_1: ─────┤ X ├\n             └───┘", clean_counts3, 'lightsalmon')
    ]
    
    for i, (title, circuit, counts, color) in enumerate(circuits):
        # Circuit diagram with larger text
        ax[i].text(0.5, 0.9, title, ha='center', fontsize=11, fontweight='bold', transform=ax[i].transAxes)
        ax[i].text(0.5, 0.55, circuit, ha='center', fontsize=9, fontfamily='monospace', 
                   transform=ax[i].transAxes, bbox=dict(boxstyle="round,pad=0.15", facecolor=color, alpha=0.4))
        ax[i].text(0.5, 0.1, f'{counts}', ha='center', fontsize=9, fontweight='bold', transform=ax[i].transAxes)
        ax[i].axis('off')
        
        # Bar chart
        bars = ax[i+3].bar(counts.keys(), counts.values(), 
                          color=color, alpha=0.8, edgecolor='black', linewidth=1)
        ax[i+3].set_title(title.split()[0] + ' ' + title.split()[1], fontweight='bold', fontsize=9)
        ax[i+3].set_ylabel('Counts', fontsize=8)
        ax[i+3].tick_params(labelsize=7)
        
        # Add count labels on bars
        for bar in bars:
            height = bar.get_height()
            ax[i+3].text(bar.get_x() + bar.get_width()/2., height + max(counts.values())*0.02,
                         f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=8)
    
    # Adjust layout for maximum compactness
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.15, wspace=0.15, top=0.92, bottom=0.08)
    plt.savefig('lab1_compact.png', dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.05)
    plt.show()
    
    print("✓ Ultra-compact visualization saved as 'lab1_compact.png'")
    print("✓ Minimal white space, maximum information density")
    print("✓ Perfect for lab reports and presentations")

if __name__ == "__main__":
    main()