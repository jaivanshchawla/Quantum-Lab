"""
Lab 5: Hello Quantum World Program
==================================
Objective: Execute Hello Quantum World program and analyze output
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("LAB 5: HELLO QUANTUM WORLD PROGRAM")
    print("===================================")
    print()
    
    # Initialize simulator
    simulator = AerSimulator()
    
    # PART 1: Classic Hello Quantum World
    print("PART 1: Hello Quantum World")
    print("---------------------------")
    qc1 = QuantumCircuit(1, 1)
    qc1.h(0)  # Hadamard gate creates superposition
    qc1.measure(0, 0)
    print("Circuit: Hadamard gate + measurement")
    print(qc1.draw(output='text'))
    
    job1 = simulator.run(qc1, shots=1000)
    counts1 = job1.result().get_counts()
    print(f"Results: {counts1}")
    print()
    
    # PART 2: Multiple Runs Analysis
    print("PART 2: Multiple Runs Analysis")
    print("-------------------------------")
    runs = []
    for i in range(5):
        job = simulator.run(qc1, shots=100)
        counts = job.result().get_counts()
        prob_0 = counts.get('0', 0) / 100
        prob_1 = counts.get('1', 0) / 100
        runs.append((prob_0, prob_1))
        print(f"Run {i+1}: |0⟩={prob_0:.2f}, |1⟩={prob_1:.2f}")
    print()
    
    # PART 3: Different Shot Counts
    print("PART 3: Different Shot Counts")
    print("------------------------------")
    shot_counts = [10, 100, 1000, 10000]
    shot_results = []
    
    for shots in shot_counts:
        job = simulator.run(qc1, shots=shots)
        counts = job.result().get_counts()
        prob_0 = counts.get('0', 0) / shots
        prob_1 = counts.get('1', 0) / shots
        shot_results.append((shots, prob_0, prob_1, counts))
        print(f"{shots:5d} shots: |0⟩={prob_0:.3f}, |1⟩={prob_1:.3f} - {counts}")
    print()
    
    # PART 4: Theoretical vs Experimental
    print("PART 4: Theoretical vs Experimental")
    print("------------------------------------")
    theoretical_prob = 0.5
    job_large = simulator.run(qc1, shots=10000)
    counts_large = job_large.result().get_counts()
    exp_prob_0 = counts_large.get('0', 0) / 10000
    exp_prob_1 = counts_large.get('1', 0) / 10000
    
    print(f"Theoretical: |0⟩=0.500, |1⟩=0.500")
    print(f"Experimental: |0⟩={exp_prob_0:.3f}, |1⟩={exp_prob_1:.3f}")
    print(f"Deviation: |0⟩={abs(exp_prob_0-0.5):.3f}, |1⟩={abs(exp_prob_1-0.5):.3f}")
    print()
    
    # Create compact visualization
    fig = plt.figure(figsize=(14, 8))
    fig.suptitle('Lab 5: Hello Quantum World Program', fontsize=14, fontweight='bold', y=0.95)
    
    # Create 2x3 grid layout
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)
    
    # Top left: Circuit diagram
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.text(0.5, 0.9, 'Hello Quantum World', ha='center', fontsize=11, fontweight='bold', transform=ax1.transAxes)
    circuit_text = "     ┌───┐┌─┐\n  q: ┤ H ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0"
    ax1.text(0.5, 0.5, circuit_text, ha='center', fontsize=8, fontfamily='monospace', 
             transform=ax1.transAxes, bbox=dict(boxstyle="round,pad=0.1", facecolor="lightblue", alpha=0.4))
    ax1.text(0.5, 0.05, f'{counts1}', ha='center', fontsize=9, fontweight='bold', transform=ax1.transAxes)
    ax1.axis('off')
    
    # Top middle: Multiple runs
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_title('Multiple Runs (100 shots each)', fontweight='bold', fontsize=10)
    run_numbers = range(1, 6)
    probs_0 = [run[0] for run in runs]
    probs_1 = [run[1] for run in runs]
    
    x = np.arange(len(run_numbers))
    width = 0.35
    ax2.bar(x - width/2, probs_0, width, label='|0⟩', color='skyblue', alpha=0.8)
    ax2.bar(x + width/2, probs_1, width, label='|1⟩', color='lightcoral', alpha=0.8)
    ax2.set_ylabel('Probability')
    ax2.set_xlabel('Run Number')
    ax2.set_xticks(x)
    ax2.set_xticklabels(run_numbers)
    ax2.legend()
    ax2.set_ylim(0, 1)
    ax2.axhline(y=0.5, color='red', linestyle='--', alpha=0.7, label='Theoretical')
    
    # Top right: Shot count analysis
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.set_title('Shot Count Analysis', fontweight='bold', fontsize=10)
    shots_list = [result[0] for result in shot_results]
    probs_0_shots = [result[1] for result in shot_results]
    probs_1_shots = [result[2] for result in shot_results]
    
    ax3.semilogx(shots_list, probs_0_shots, 'o-', label='|0⟩', color='blue', markersize=6)
    ax3.semilogx(shots_list, probs_1_shots, 's-', label='|1⟩', color='red', markersize=6)
    ax3.axhline(y=0.5, color='green', linestyle='--', alpha=0.7, label='Theoretical')
    ax3.set_ylabel('Probability')
    ax3.set_xlabel('Number of Shots')
    ax3.legend()
    ax3.set_ylim(0.3, 0.7)
    ax3.grid(True, alpha=0.3)
    
    # Bottom: Main result bar chart
    ax4 = fig.add_subplot(gs[1, :])
    ax4.set_title('Hello Quantum World Results (1000 shots)', fontweight='bold', fontsize=12)
    
    states = list(counts1.keys())
    values = list(counts1.values())
    bars = ax4.bar(states, values, color=['skyblue', 'lightcoral'], alpha=0.8, edgecolor='black', linewidth=2)
    
    # Add theoretical line
    ax4.axhline(y=500, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Theoretical (500)')
    
    # Add count labels on bars
    for bar in bars:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 10,
                 f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    ax4.set_ylabel('Counts', fontsize=10)
    ax4.set_xlabel('Measurement Outcome', fontsize=10)
    ax4.legend()
    ax4.set_ylim(0, 600)
    
    # Add compact summary
    fig.text(0.5, 0.08, 'SUPERPOSITION: H|0⟩ = (|0⟩ + |1⟩)/√2 → Equal probability outcomes', 
             ha='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.2", facecolor="lightyellow", edgecolor="orange"))
    fig.text(0.5, 0.03, 'QUANTUM RANDOMNESS: ✓ True randomness ✓ Statistical convergence ✓ Theoretical verification', 
             ha='center', fontsize=10, fontweight='bold', color='darkgreen')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.88, bottom=0.15)
    plt.savefig('qiskit_lab_5_final_image.png', dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.05)
    plt.show()
    
    print("HELLO QUANTUM WORLD ANALYSIS COMPLETE")
    print("======================================")
    print("✓ Hadamard gate creates equal superposition")
    print("✓ Measurement gives ~50% probability for each outcome")
    print("✓ Multiple runs show statistical variation")
    print("✓ Larger shot counts converge to theoretical values")
    print("✓ True quantum randomness demonstrated")
    print()
    print("THEORETICAL VERIFICATION:")
    print("=========================")
    print("• H|0⟩ = (|0⟩ + |1⟩)/√2 (equal superposition)")
    print("• P(0) = |⟨0|(|0⟩ + |1⟩)/√2|² = 1/2 = 0.5")
    print("• P(1) = |⟨1|(|0⟩ + |1⟩)/√2|² = 1/2 = 0.5")
    print("• Quantum measurement is fundamentally probabilistic")
    print()
    print("CONCLUSION:")
    print("===========")
    print("✓ Hello Quantum World demonstrates quantum superposition")
    print("✓ Hadamard gate is the key to quantum randomness")
    print("✓ Statistical analysis confirms theoretical predictions")
    print("✓ Visualization saved as 'qiskit_lab_5_final_image.png'")

if __name__ == "__main__":
    main()