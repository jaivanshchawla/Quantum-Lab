"""
Lab 1: Clean Circuit Visualization
==================================
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    
    # Create the visualization with larger figure and white background
    plt.style.use('default')  # Use default style for white background
    fig = plt.figure(figsize=(18, 12), facecolor='white')
    fig.suptitle('Qiskit Lab 1 Final Image', 
                 fontsize=18, fontweight='bold', y=0.95, color='black')
    
    # Create grid layout: 3 rows, 3 columns
    gs = fig.add_gridspec(3, 3, height_ratios=[1, 1, 1.2], hspace=0.4, wspace=0.3)
    
    # Row 1: Circuit Diagrams
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[0, 2])
    
    # Row 2: Results Text
    ax4 = fig.add_subplot(gs[1, 0])
    ax5 = fig.add_subplot(gs[1, 1])
    ax6 = fig.add_subplot(gs[1, 2])
    
    # Row 3: Bar Charts (spanning full width for better visibility)
    ax7 = fig.add_subplot(gs[2, 0])
    ax8 = fig.add_subplot(gs[2, 1])
    ax9 = fig.add_subplot(gs[2, 2])
    
    # Circuit 1: Basic Qubit
    ax1.text(0.5, 0.9, 'PART 1: Basic Qubit |0⟩', ha='center', fontsize=14, fontweight='bold', 
             transform=ax1.transAxes, color='black')
    circuit1_box = patches.Rectangle((0.1, 0.2), 0.8, 0.6, linewidth=2, edgecolor='blue', facecolor='lightblue', alpha=0.3)
    ax1.add_patch(circuit1_box)
    circuit1_text = """     ┌─┐
  q: ┤M├
     └╥┘
c: 1/═╩═
      0"""
    ax1.text(0.5, 0.5, circuit1_text, ha='center', va='center', fontsize=11, fontfamily='monospace', 
             transform=ax1.transAxes, fontweight='bold', color='black')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')
    ax1.set_facecolor('white')
    
    # Circuit 2: Superposition
    ax2.text(0.5, 0.9, 'PART 2: Superposition |+⟩', ha='center', fontsize=14, fontweight='bold', 
             transform=ax2.transAxes, color='black')
    circuit2_box = patches.Rectangle((0.1, 0.2), 0.8, 0.6, linewidth=2, edgecolor='green', facecolor='lightgreen', alpha=0.3)
    ax2.add_patch(circuit2_box)
    circuit2_text = """     ┌───┐┌─┐
  q: ┤ H ├┤M├
     └───┘└╥┘
c: 1/══════╩═
           0"""
    ax2.text(0.5, 0.5, circuit2_text, ha='center', va='center', fontsize=11, fontfamily='monospace', 
             transform=ax2.transAxes, fontweight='bold', color='black')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    ax2.set_facecolor('white')
    
    # Circuit 3: Bell State
    ax3.text(0.5, 0.9, 'PART 3: Bell State |Φ+⟩', ha='center', fontsize=14, fontweight='bold', 
             transform=ax3.transAxes, color='black')
    circuit3_box = patches.Rectangle((0.05, 0.15), 0.9, 0.7, linewidth=2, edgecolor='red', facecolor='lightsalmon', alpha=0.3)
    ax3.add_patch(circuit3_box)
    circuit3_text = """        ┌───┐     
   q_0: ┤ H ├──■──
        └───┘┌─┴─┐
   q_1: ─────┤ X ├
             └───┘
     measure_all()"""
    ax3.text(0.5, 0.5, circuit3_text, ha='center', va='center', fontsize=10, fontfamily='monospace', 
             transform=ax3.transAxes, fontweight='bold', color='black')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis('off')
    ax3.set_facecolor('white')
    
    # Results Text
    ax4.text(0.5, 0.7, 'RESULTS:', ha='center', fontsize=12, fontweight='bold', 
             transform=ax4.transAxes, color='black')
    ax4.text(0.5, 0.5, f'{counts1}', ha='center', fontsize=11, transform=ax4.transAxes, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.5), color='black')
    ax4.text(0.5, 0.2, 'Always |0⟩\n(100% deterministic)', ha='center', fontsize=10, 
             transform=ax4.transAxes, color='black')
    ax4.axis('off')
    ax4.set_facecolor('white')
    
    ax5.text(0.5, 0.7, 'RESULTS:', ha='center', fontsize=12, fontweight='bold', 
             transform=ax5.transAxes, color='black')
    ax5.text(0.5, 0.5, f'{counts2}', ha='center', fontsize=11, transform=ax5.transAxes,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.5), color='black')
    ax5.text(0.5, 0.2, '~50% |0⟩, ~50% |1⟩\n(Quantum superposition)', ha='center', fontsize=10, 
             transform=ax5.transAxes, color='black')
    ax5.axis('off')
    ax5.set_facecolor('white')
    
    ax6.text(0.5, 0.7, 'RESULTS:', ha='center', fontsize=12, fontweight='bold', 
             transform=ax6.transAxes, color='black')
    ax6.text(0.5, 0.5, f'{clean_counts3}', ha='center', fontsize=11, transform=ax6.transAxes,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightsalmon", alpha=0.5), color='black')
    ax6.text(0.5, 0.2, 'Only |00⟩ and |11⟩\n(Quantum entanglement)', ha='center', fontsize=10, 
             transform=ax6.transAxes, color='black')
    ax6.axis('off')
    ax6.set_facecolor('white')
    
    # Bar Charts with enhanced styling
    # Bar chart 1
    bars1 = ax7.bar(counts1.keys(), counts1.values(), color='skyblue', alpha=0.8, edgecolor='navy', linewidth=2)
    ax7.set_title('Basic Qubit Measurements', fontweight='bold', fontsize=12)
    ax7.set_ylabel('Counts', fontweight='bold')
    ax7.set_ylim(0, 1100)
    ax7.grid(True, alpha=0.3)
    for bar in bars1:
        height = bar.get_height()
        ax7.text(bar.get_x() + bar.get_width()/2., height + 20,
                 f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Bar chart 2
    bars2 = ax8.bar(counts2.keys(), counts2.values(), color='lightgreen', alpha=0.8, edgecolor='darkgreen', linewidth=2)
    ax8.set_title('Superposition Measurements', fontweight='bold', fontsize=12)
    ax8.set_ylabel('Counts', fontweight='bold')
    ax8.set_ylim(0, 600)
    ax8.grid(True, alpha=0.3)
    for bar in bars2:
        height = bar.get_height()
        ax8.text(bar.get_x() + bar.get_width()/2., height + 10,
                 f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Bar chart 3
    bars3 = ax9.bar(clean_counts3.keys(), clean_counts3.values(), color='salmon', alpha=0.8, edgecolor='darkred', linewidth=2)
    ax9.set_title('Bell State Measurements', fontweight='bold', fontsize=12)
    ax9.set_ylabel('Counts', fontweight='bold')
    ax9.set_ylim(0, 600)
    ax9.grid(True, alpha=0.3)
    for bar in bars3:
        height = bar.get_height()
        ax9.text(bar.get_x() + bar.get_width()/2., height + 10,
                 f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Add summary at bottom (keep only the observations)
    fig.text(0.5, 0.08, 'OBSERVATIONS: Basic Qubit (deterministic) | Superposition (random 50/50) | Bell State (entangled correlations)', 
             ha='center', fontsize=12, bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", edgecolor="orange"))
    
    plt.savefig('qiskit_lab_1_final_image.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    
    print("✓ Final image saved as 'qiskit_lab_1_final_image.png'")
    print("✓ Clean layout without student info or conclusion text")
    print("✓ Perfect for lab submission")

if __name__ == "__main__":
    main()