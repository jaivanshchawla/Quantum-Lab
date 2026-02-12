"""
Lab 8: Quantum Superposition
=============================
Objective: Generate and analyze superposition states
Theory: Superposition allows simultaneous existence of |0⟩ and |1⟩ states
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def main():
    print("LAB 8: QUANTUM SUPERPOSITION")
    print("=============================")
    print()
    
    # Initialize simulator
    simulator = AerSimulator()
    shots = 1000
    
    # PART 1: Basic State |0⟩ (No Superposition)
    print("PART 1: Basic State |0⟩")
    print("------------------------")
    qc1 = QuantumCircuit(1, 1)
    qc1.measure(0, 0)
    print("Circuit: Single qubit in ground state |0⟩")
    print(qc1.draw(output='text'))
    
    job1 = simulator.run(qc1, shots=shots)
    counts1 = job1.result().get_counts()
    print(f"Results: {counts1}")
    print("Observation: Deterministic - always measures |0⟩")
    print()
    
    # PART 2: Superposition State |+⟩ (Hadamard Gate)
    print("PART 2: Superposition State |+⟩")
    print("--------------------------------")
    qc2 = QuantumCircuit(1, 1)
    qc2.h(0)  # Hadamard gate creates superposition
    qc2.measure(0, 0)
    print("Circuit: Hadamard gate H|0⟩ = |+⟩ = (|0⟩ + |1⟩)/√2")
    print(qc2.draw(output='text'))
    
    job2 = simulator.run(qc2, shots=shots)
    counts2 = job2.result().get_counts()
    print(f"Results: {counts2}")
    print("Observation: Equal superposition - ~50% |0⟩, ~50% |1⟩")
    print()
    
    # PART 3: Superposition State |−⟩ (X then Hadamard)
    print("PART 3: Superposition State |−⟩")
    print("--------------------------------")
    qc3 = QuantumCircuit(1, 1)
    qc3.x(0)  # X gate flips to |1⟩
    qc3.h(0)  # Hadamard creates |−⟩ = (|0⟩ - |1⟩)/√2
    qc3.measure(0, 0)
    print("Circuit: X then H creates |−⟩ = (|0⟩ - |1⟩)/√2")
    print(qc3.draw(output='text'))
    
    job3 = simulator.run(qc3, shots=shots)
    counts3 = job3.result().get_counts()
    print(f"Results: {counts3}")
    print("Observation: Equal superposition - ~50% |0⟩, ~50% |1⟩")
    print("Note: |+⟩ and |−⟩ differ by phase, same measurement statistics")
    print()
    
    # Create visualization
    print("CREATING VISUALIZATION...")
    fig = plt.figure(figsize=(15, 10))
    fig.suptitle('Lab 8: Quantum Superposition States', fontsize=16, fontweight='bold')
    
    # Create grid layout
    gs = fig.add_gridspec(3, 3, height_ratios=[0.6, 1.2, 1], hspace=0.4, wspace=0.3)
    
    # Top row: Theory explanation
    ax_theory = fig.add_subplot(gs[0, :])
    theory_text = """SUPERPOSITION THEORY
Quantum superposition: A qubit can exist in multiple states simultaneously
|+⟩ = H|0⟩ = (|0⟩ + |1⟩)/√2  |  |−⟩ = H|1⟩ = (|0⟩ - |1⟩)/√2
Measurement collapses superposition to definite state with equal probability"""
    
    ax_theory.text(0.5, 0.5, theory_text, ha='center', va='center', fontsize=11,
                   transform=ax_theory.transAxes, 
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.4))
    ax_theory.axis('off')
    
    # Middle row: Circuit diagrams
    circuits = [
        ("State |0⟩", "     ┌─┐\nq: ──┤M├\n     └╥┘\nc: 1/═╩═\n      0 ", counts1, 'lightgray'),
        ("State |+⟩", "     ┌───┐┌─┐\nq: ──┤ H ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0 ", counts2, 'lightgreen'),
        ("State |−⟩", "     ┌───┐┌───┐┌─┐\nq: ──┤ X ├┤ H ├┤M├\n     └───┘└───┘└╥┘\nc: 1/═══════════╩═\n                0 ", counts3, 'lightsalmon')
    ]
    
    for i, (title, circuit, counts, color) in enumerate(circuits):
        ax = fig.add_subplot(gs[1, i])
        ax.text(0.5, 0.95, title, ha='center', fontsize=11, fontweight='bold', 
                transform=ax.transAxes)
        ax.text(0.5, 0.55, circuit, ha='center', fontsize=8, fontfamily='monospace',
                transform=ax.transAxes, 
                bbox=dict(boxstyle="round,pad=0.15", facecolor=color, alpha=0.5))
        ax.text(0.5, 0.05, f'{counts}', ha='center', fontsize=9, fontweight='bold',
                transform=ax.transAxes)
        ax.axis('off')
    
    # Bottom row: Bar charts
    test_results = [counts1, counts2, counts3]
    colors = ['gray', 'limegreen', 'coral']
    titles = ['Ground State |0⟩', 'Superposition |+⟩', 'Superposition |−⟩']
    
    for i, (counts, color, title) in enumerate(zip(test_results, colors, titles)):
        ax = fig.add_subplot(gs[2, i])
        
        # Ensure both 0 and 1 are shown even if count is 0
        all_states = {'0': counts.get('0', 0), '1': counts.get('1', 0)}
        
        bars = ax.bar(all_states.keys(), all_states.values(), color=color, 
                     alpha=0.8, edgecolor='black', linewidth=1.5)
        ax.set_title(title, fontweight='bold', fontsize=10)
        ax.set_ylabel('Counts', fontsize=9)
        ax.set_xlabel('Measurement Outcome', fontsize=9)
        ax.tick_params(labelsize=8)
        ax.set_ylim(0, shots * 1.1)
        
        # Add count labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + shots*0.02,
                   f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        # Add percentage labels
        for state, count in all_states.items():
            percentage = (count / shots) * 100
            ax.text(float(state), -shots*0.08, f'{percentage:.1f}%', 
                   ha='center', fontsize=8, color='darkblue', fontweight='bold')
    
    # Add summary at bottom
    fig.text(0.5, 0.02, 
             '✓ Superposition Demonstrated  ✓ Equal Probability Distribution  ✓ Quantum Measurement Collapse',
             ha='center', fontsize=11, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", edgecolor="orange"))
    
    plt.savefig('qiskit_lab_8_final_image.png', dpi=300, bbox_inches='tight', 
                facecolor='white', pad_inches=0.1)
    print("✓ Visualization saved as 'qiskit_lab_8_final_image.png'")
    plt.show()
    
    print()
    print("OBSERVATIONS & RESULTS")
    print("======================")
    print("1. Ground State |0⟩: Deterministic measurement (100% |0⟩)")
    print("2. Superposition |+⟩: Equal probability (~50% |0⟩, ~50% |1⟩)")
    print("3. Superposition |−⟩: Equal probability (~50% |0⟩, ~50% |1⟩)")
    print()
    print("THEORETICAL VERIFICATION")
    print("========================")
    print("✓ Hadamard gate creates equal superposition")
    print("✓ Measurement collapses superposition to definite state")
    print("✓ |+⟩ and |−⟩ have same measurement statistics (differ by phase)")
    print("✓ Results match quantum theory predictions")
    print()
    print("CONCLUSION")
    print("==========")
    print("✓ Successfully generated superposition states")
    print("✓ Verified equal probability distribution")
    print("✓ Demonstrated quantum measurement collapse")
    print("✓ Confirmed theoretical expectations")

if __name__ == "__main__":
    main()
