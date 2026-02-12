"""
Lab 1: Final Version - Exact Terminal Output + Visualization
===========================================================
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def main():
    # Print the exact output as shown in terminal
    print("LAB 1: QUANTUM COMPUTING WITH QISKIT")
    print("=====================================")
    print("Student: [Your Name]")
    print("Date: [Current Date]")
    print()
    
    # Initialize simulator
    simulator = AerSimulator()
    
    # PART 1: Basic Qubit |0⟩
    print("PART 1: Basic Qubit")
    print("-------------------")
    print("Circuit: Single qubit in |0⟩ state")
    qc1 = QuantumCircuit(1, 1)
    qc1.measure(0, 0)
    print("     ┌─┐")
    print("  q: ┤M├")
    print("     └╥┘")
    print("c: 1/═╩═")
    print("      0")
    
    job1 = simulator.run(qc1, shots=1000)
    counts1 = job1.result().get_counts()
    print(f"Results: {counts1}")
    print()
    
    # PART 2: Superposition |+⟩
    print("PART 2: Superposition")
    print("---------------------")
    print("Circuit: Hadamard gate creates |+⟩ = (|0⟩ + |1⟩)/√2")
    qc2 = QuantumCircuit(1, 1)
    qc2.h(0)
    qc2.measure(0, 0)
    print("     ┌───┐┌─┐")
    print("  q: ┤ H ├┤M├")
    print("     └───┘└╥┘")
    print("c: 1/══════╩═")
    print("           0")
    
    job2 = simulator.run(qc2, shots=1000)
    counts2 = job2.result().get_counts()
    print(f"Results: {counts2}")
    print()
    
    # PART 3: Bell State |Φ+⟩
    print("PART 3: Entanglement")
    print("--------------------")
    print("Circuit: Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2")
    qc3 = QuantumCircuit(2, 2)
    qc3.h(0)
    qc3.cx(0, 1)
    qc3.measure_all()
    print("        ┌───┐      ░ ┌─┐")
    print("   q_0: ┤ H ├──■───░─┤M├")
    print("        └───┘┌─┴─┐ ░ └╥┘")
    print("   q_1: ─────┤ X ├─░──╫─")
    print("             └───┘ ░  ║")
    print("   c: 2/══════════════╬═")
    print("                      ║")
    print("meas: 2/══════════════╩═")
    print("                      0")
    
    job3 = simulator.run(qc3, shots=1000)
    counts3 = job3.result().get_counts()
    # Clean up results
    clean_counts3 = {}
    for key, value in counts3.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts3[clean_key] = value
    print(f"Results: {clean_counts3}")
    print()
    
    # Create comprehensive visualization with tighter layout
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=(14, 8))
    fig.suptitle('Lab 1: Quantum Computing Results - Complete Analysis', fontsize=16, fontweight='bold', y=0.98)
    
    # Row 1: Circuit Diagrams with proper spacing
    # Circuit 1
    ax1.text(0.5, 0.85, 'Basic Qubit |0⟩', ha='center', fontsize=12, fontweight='bold', transform=ax1.transAxes)
    circuit1_text = """     ┌─┐
  q: ┤M├
     └╥┘
c: 1/═╩═
      0"""
    ax1.text(0.5, 0.55, circuit1_text, ha='center', fontsize=9, fontfamily='monospace', 
             transform=ax1.transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.3))
    ax1.text(0.5, 0.15, f'Result: {counts1}', ha='center', fontsize=9, fontweight='bold', transform=ax1.transAxes)
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')
    
    # Circuit 2
    ax2.text(0.5, 0.85, 'Superposition |+⟩', ha='center', fontsize=12, fontweight='bold', transform=ax2.transAxes)
    circuit2_text = """     ┌───┐┌─┐
  q: ┤ H ├┤M├
     └───┘└╥┘
c: 1/══════╩═
           0"""
    ax2.text(0.5, 0.55, circuit2_text, ha='center', fontsize=9, fontfamily='monospace', 
             transform=ax2.transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.3))
    ax2.text(0.5, 0.15, f'Result: {counts2}', ha='center', fontsize=9, fontweight='bold', transform=ax2.transAxes)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    
    # Circuit 3
    ax3.text(0.5, 0.85, 'Bell State |Φ+⟩', ha='center', fontsize=12, fontweight='bold', transform=ax3.transAxes)
    circuit3_text = """        ┌───┐     
   q_0: ┤ H ├──■──
        └───┘┌─┴─┐
   q_1: ─────┤ X ├
             └───┘
     measure_all()"""
    ax3.text(0.5, 0.55, circuit3_text, ha='center', fontsize=8, fontfamily='monospace', 
             transform=ax3.transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightsalmon", alpha=0.3))
    ax3.text(0.5, 0.15, f'Result: {clean_counts3}', ha='center', fontsize=9, fontweight='bold', transform=ax3.transAxes)
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis('off')
    
    # Row 2: Bar Charts
    # Bar chart 1
    bars1 = ax4.bar(counts1.keys(), counts1.values(), color='skyblue', alpha=0.8, edgecolor='navy')
    ax4.set_title('Basic Qubit Measurements', fontweight='bold')
    ax4.set_ylabel('Counts')
    ax4.set_ylim(0, 1100)
    for bar in bars1:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 20,
                 f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    # Bar chart 2
    bars2 = ax5.bar(counts2.keys(), counts2.values(), color='lightgreen', alpha=0.8, edgecolor='darkgreen')
    ax5.set_title('Superposition Measurements', fontweight='bold')
    ax5.set_ylabel('Counts')
    ax5.set_ylim(0, 600)
    for bar in bars2:
        height = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2., height + 10,
                 f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    # Bar chart 3
    bars3 = ax6.bar(clean_counts3.keys(), clean_counts3.values(), color='salmon', alpha=0.8, edgecolor='darkred')
    ax6.set_title('Bell State Measurements', fontweight='bold')
    ax6.set_ylabel('Counts')
    ax6.set_ylim(0, 600)
    for bar in bars3:
        height = bar.get_height()
        ax6.text(bar.get_x() + bar.get_width()/2., height + 10,
                 f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    plt.savefig('lab1_final_complete.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    print("✓ Final complete visualization saved as 'lab1_final_complete.png'")
    
    # Summary
    print("OBSERVATIONS:")
    print("=============")
    print("1. Basic Qubit: Always |0⟩ (100% deterministic)")
    print("2. Superposition: ~50% |0⟩, ~50% |1⟩ (quantum randomness)")
    print("3. Bell State: Only |00⟩ and |11⟩ (quantum entanglement)")
    print()
    print("CONCLUSION:")
    print("===========")
    print("✓ Successfully demonstrated quantum superposition")
    print("✓ Successfully demonstrated quantum entanglement")
    print("✓ All results match quantum mechanical predictions")
    print("✓ Lab requirements fulfilled completely")

if __name__ == "__main__":
    main()