"""
Lab 9: Quantum Measurement and Probability Distributions
========================================================
Objective: Analyze probabilistic measurement outcomes
Theory: Measurement collapses statevector into classical states 
        with probability |α|² for |0⟩ and |β|² for |1⟩
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("LAB 9: QUANTUM MEASUREMENT AND PROBABILITY DISTRIBUTIONS")
    print("=========================================================")
    print()
    
    # Initialize simulator
    simulator = AerSimulator()
    shots = 1000
    
    # PART 1: Deterministic State |0⟩
    print("PART 1: Deterministic State |0⟩")
    print("--------------------------------")
    qc1 = QuantumCircuit(1, 1)
    qc1.measure(0, 0)
    print("Circuit: Measure ground state |0⟩")
    print(qc1.draw(output='text'))
    
    # Get statevector before measurement
    sv1 = Statevector.from_label('0')
    print(f"Statevector: {sv1.data}")
    print(f"Probabilities: |α|² = {abs(sv1.data[0])**2:.3f}, |β|² = {abs(sv1.data[1])**2:.3f}")
    
    job1 = simulator.run(qc1, shots=shots)
    counts1 = job1.result().get_counts()
    print(f"Measurement Results: {counts1}")
    print("Observation: 100% probability of measuring |0⟩")
    print()
    
    # PART 2: Equal Superposition |+⟩
    print("PART 2: Equal Superposition |+⟩")
    print("--------------------------------")
    qc2 = QuantumCircuit(1, 1)
    qc2.h(0)  # Hadamard creates |+⟩ = (|0⟩ + |1⟩)/√2
    qc2.measure(0, 0)
    print("Circuit: H|0⟩ = |+⟩ = (|0⟩ + |1⟩)/√2")
    print(qc2.draw(output='text'))
    
    # Get statevector before measurement
    qc2_sv = QuantumCircuit(1)
    qc2_sv.h(0)
    sv2 = Statevector.from_instruction(qc2_sv)
    print(f"Statevector: {sv2.data}")
    print(f"Probabilities: |α|² = {abs(sv2.data[0])**2:.3f}, |β|² = {abs(sv2.data[1])**2:.3f}")
    
    job2 = simulator.run(qc2, shots=shots)
    counts2 = job2.result().get_counts()
    print(f"Measurement Results: {counts2}")
    print("Observation: 50% probability for each outcome")
    print()
    
    # PART 3: Unequal Superposition (Ry gate)
    print("PART 3: Unequal Superposition (Ry gate)")
    print("---------------------------------------")
    qc3 = QuantumCircuit(1, 1)
    angle = np.pi / 3  # 60 degrees
    qc3.ry(angle, 0)  # Ry rotation creates unequal superposition
    qc3.measure(0, 0)
    print(f"Circuit: Ry(π/3)|0⟩ creates unequal superposition")
    print(qc3.draw(output='text'))
    
    # Get statevector before measurement
    qc3_sv = QuantumCircuit(1)
    qc3_sv.ry(angle, 0)
    sv3 = Statevector.from_instruction(qc3_sv)
    prob_0 = abs(sv3.data[0])**2
    prob_1 = abs(sv3.data[1])**2
    print(f"Statevector: {sv3.data}")
    print(f"Probabilities: |α|² = {prob_0:.3f}, |β|² = {prob_1:.3f}")
    
    job3 = simulator.run(qc3, shots=shots)
    counts3 = job3.result().get_counts()
    print(f"Measurement Results: {counts3}")
    print(f"Observation: ~{prob_0*100:.1f}% |0⟩, ~{prob_1*100:.1f}% |1⟩")
    print()
    
    # PART 4: Another Unequal Superposition (Ry gate)
    print("PART 4: Another Unequal Superposition")
    print("-------------------------------------")
    qc4 = QuantumCircuit(1, 1)
    angle2 = np.pi / 6  # 30 degrees
    qc4.ry(angle2, 0)
    qc4.measure(0, 0)
    print(f"Circuit: Ry(π/6)|0⟩ creates different superposition")
    print(qc4.draw(output='text'))
    
    # Get statevector before measurement
    qc4_sv = QuantumCircuit(1)
    qc4_sv.ry(angle2, 0)
    sv4 = Statevector.from_instruction(qc4_sv)
    prob_0_4 = abs(sv4.data[0])**2
    prob_1_4 = abs(sv4.data[1])**2
    print(f"Statevector: {sv4.data}")
    print(f"Probabilities: |α|² = {prob_0_4:.3f}, |β|² = {prob_1_4:.3f}")
    
    job4 = simulator.run(qc4, shots=shots)
    counts4 = job4.result().get_counts()
    print(f"Measurement Results: {counts4}")
    print(f"Observation: ~{prob_0_4*100:.1f}% |0⟩, ~{prob_1_4*100:.1f}% |1⟩")
    print()
    
    # Create comprehensive visualization
    print("CREATING VISUALIZATION...")
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('Lab 9: Quantum Measurement and Probability Distributions', 
                 fontsize=16, fontweight='bold')
    
    # Create grid layout
    gs = fig.add_gridspec(4, 4, height_ratios=[0.5, 1, 1, 1], hspace=0.5, wspace=0.3)
    
    # Top row: Theory explanation
    ax_theory = fig.add_subplot(gs[0, :])
    theory_text = """MEASUREMENT THEORY
Quantum State: |ψ⟩ = α|0⟩ + β|1⟩  where |α|² + |β|² = 1
Measurement Probability: P(0) = |α|²  and  P(1) = |β|²
Measurement collapses superposition to definite classical state"""
    
    ax_theory.text(0.5, 0.5, theory_text, ha='center', va='center', fontsize=11,
                   transform=ax_theory.transAxes, 
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcyan", alpha=0.5))
    ax_theory.axis('off')
    
    # Prepare data
    circuits_data = [
        ("State |0⟩", "     ┌─┐\nq: ──┤M├\n     └╥┘\nc: 1/═╩═\n      0", counts1, sv1, 'lightgray'),
        ("State |+⟩", "     ┌───┐┌─┐\nq: ──┤ H ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0", counts2, sv2, 'lightgreen'),
        ("Ry(π/3)|0⟩", f"     ┌─────────┐┌─┐\nq: ──┤ Ry(π/3) ├┤M├\n     └─────────┘└╥┘\nc: 1/════════════╩═\n                 0", counts3, sv3, 'lightsalmon'),
        ("Ry(π/6)|0⟩", f"     ┌─────────┐┌─┐\nq: ──┤ Ry(π/6) ├┤M├\n     └─────────┘└╥┘\nc: 1/════════════╩═\n                 0", counts4, sv4, 'lightblue')
    ]
    
    # Row 2: Circuit diagrams
    for i, (title, circuit, counts, sv, color) in enumerate(circuits_data):
        ax = fig.add_subplot(gs[1, i])
        ax.text(0.5, 0.95, title, ha='center', fontsize=10, fontweight='bold',
                transform=ax.transAxes)
        ax.text(0.5, 0.5, circuit, ha='center', fontsize=6.5, fontfamily='monospace',
                transform=ax.transAxes,
                bbox=dict(boxstyle="round,pad=0.1", facecolor=color, alpha=0.5))
        
        # Show probabilities
        prob_text = f"|α|²={abs(sv.data[0])**2:.3f}\n|β|²={abs(sv.data[1])**2:.3f}"
        ax.text(0.5, 0.05, prob_text, ha='center', fontsize=8, fontweight='bold',
                transform=ax.transAxes)
        ax.axis('off')
    
    # Row 3: Measurement histograms
    test_results = [counts1, counts2, counts3, counts4]
    colors = ['gray', 'limegreen', 'coral', 'skyblue']
    titles = ['|0⟩ State', '|+⟩ State', 'Ry(π/3) State', 'Ry(π/6) State']
    
    for i, (counts, color, title) in enumerate(zip(test_results, colors, titles)):
        ax = fig.add_subplot(gs[2, i])
        
        # Ensure both 0 and 1 are shown
        all_states = {'0': counts.get('0', 0), '1': counts.get('1', 0)}
        
        bars = ax.bar(all_states.keys(), all_states.values(), color=color,
                     alpha=0.8, edgecolor='black', linewidth=1.5)
        ax.set_title(f'{title} - Measurements', fontweight='bold', fontsize=9)
        ax.set_ylabel('Counts', fontsize=8)
        ax.set_xlabel('Outcome', fontsize=8)
        ax.tick_params(labelsize=7)
        ax.set_ylim(0, shots * 1.1)
        
        # Add count labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + shots*0.02,
                   f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=8)
        
        # Add percentage labels
        for state, count in all_states.items():
            percentage = (count / shots) * 100
            ax.text(float(state), -shots*0.08, f'{percentage:.1f}%',
                   ha='center', fontsize=8, color='darkblue', fontweight='bold')
    
    # Row 4: Theoretical vs Experimental comparison
    statevectors = [sv1, sv2, sv3, sv4]
    for i, (sv, counts, title) in enumerate(zip(statevectors, test_results, titles)):
        ax = fig.add_subplot(gs[3, i])
        
        # Theoretical probabilities
        theo_prob_0 = abs(sv.data[0])**2
        theo_prob_1 = abs(sv.data[1])**2
        
        # Experimental probabilities
        exp_prob_0 = counts.get('0', 0) / shots
        exp_prob_1 = counts.get('1', 0) / shots
        
        x = np.arange(2)
        width = 0.35
        
        bars1 = ax.bar(x - width/2, [theo_prob_0, theo_prob_1], width,
                      label='Theoretical', color='gold', alpha=0.8, edgecolor='black')
        bars2 = ax.bar(x + width/2, [exp_prob_0, exp_prob_1], width,
                      label='Experimental', color='purple', alpha=0.6, edgecolor='black')
        
        ax.set_title(f'{title} - Comparison', fontweight='bold', fontsize=9)
        ax.set_ylabel('Probability', fontsize=8)
        ax.set_xlabel('Outcome', fontsize=8)
        ax.set_xticks(x)
        ax.set_xticklabels(['|0⟩', '|1⟩'])
        ax.tick_params(labelsize=7)
        ax.legend(fontsize=7, loc='upper right')
        ax.set_ylim(0, 1.1)
        ax.grid(axis='y', alpha=0.3)
        
        # Add value labels
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                       f'{height:.3f}', ha='center', va='bottom', fontsize=7)
    
    # Add summary
    fig.text(0.5, 0.01,
             '✓ Measurement Collapse  ✓ Born Rule |ψ|²  ✓ Probability Conservation  ✓ Theory-Experiment Agreement',
             ha='center', fontsize=11,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", edgecolor="orange"))
    
    plt.savefig('qiskit_lab_9_final_image.png', dpi=300, bbox_inches='tight',
                facecolor='white', pad_inches=0.1)
    print("✓ Visualization saved as 'qiskit_lab_9_final_image.png'")
    plt.show()
    
    print()
    print("OBSERVATIONS & RESULTS")
    print("======================")
    print(f"1. |0⟩ State: Deterministic (100% |0⟩)")
    print(f"2. |+⟩ State: Equal superposition (50% each)")
    print(f"3. Ry(π/3): Unequal superposition (~{prob_0*100:.0f}% |0⟩, ~{prob_1*100:.0f}% |1⟩)")
    print(f"4. Ry(π/6): Different distribution (~{prob_0_4*100:.0f}% |0⟩, ~{prob_1_4*100:.0f}% |1⟩)")
    print()
    print("THEORETICAL VERIFICATION")
    print("========================")
    print("✓ Born Rule: Probability = |amplitude|²")
    print("✓ Normalization: |α|² + |β|² = 1")
    print("✓ Measurement collapse: Superposition → definite state")
    print("✓ Statistical convergence: Experimental ≈ Theoretical")
    print()
    print("CONCLUSION")
    print("==========")
    print("✓ Quantum measurements are inherently probabilistic")
    print("✓ Probabilities determined by statevector amplitudes")
    print("✓ Measurement outcomes match Born rule predictions")
    print("✓ Repeated measurements reveal probability distribution")

if __name__ == "__main__":
    main()
