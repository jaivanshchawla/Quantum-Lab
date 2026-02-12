"""
Lab 11: Bell States using Hadamard and CNOT Gates
==================================================
Objective: Implement Bell states and verify correlation
Theory: Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2 created via H and CNOT gates
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("LAB 11: BELL STATES USING HADAMARD AND CNOT GATES")
    print("==================================================")
    print()
    
    # Initialize simulator
    simulator = AerSimulator()
    shots = 1000
    
    # PART 1: Initial State |00⟩ (Before Bell State)
    print("PART 1: Initial State |00⟩")
    print("---------------------------")
    qc1 = QuantumCircuit(2, 2)
    qc1.measure([0, 1], [0, 1])
    print("Circuit: Two qubits in ground state")
    print(qc1.draw(output='text'))
    
    job1 = simulator.run(qc1, shots=shots)
    counts1 = job1.result().get_counts()
    # Clean up results
    clean_counts1 = {}
    for key, value in counts1.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts1[clean_key] = value
    print(f"Results: {clean_counts1}")
    print("Observation: Always measures |00⟩ (100%)")
    print()
    
    # PART 2: After Hadamard Gate (Superposition on Qubit 0)
    print("PART 2: After Hadamard Gate")
    print("----------------------------")
    qc2 = QuantumCircuit(2, 2)
    qc2.h(0)  # Hadamard on qubit 0
    qc2.measure([0, 1], [0, 1])
    print("Circuit: H gate on qubit 0")
    print(qc2.draw(output='text'))
    
    # Get statevector
    qc2_sv = QuantumCircuit(2)
    qc2_sv.h(0)
    sv2 = Statevector.from_instruction(qc2_sv)
    print(f"Statevector: {sv2.data}")
    print("State: |ψ⟩ = (|00⟩ + |10⟩)/√2")
    
    job2 = simulator.run(qc2, shots=shots)
    counts2 = job2.result().get_counts()
    # Clean up results
    clean_counts2 = {}
    for key, value in counts2.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts2[clean_key] = value
    print(f"Results: {clean_counts2}")
    print("Observation: Only |00⟩ and |10⟩ appear (~50% each)")
    print("Note: Qubit 1 remains in |0⟩, qubit 0 in superposition")
    print()
    
    # PART 3: Bell State |Φ+⟩ (H + CNOT)
    print("PART 3: Bell State |Φ+⟩ (H + CNOT)")
    print("-----------------------------------")
    qc3 = QuantumCircuit(2, 2)
    qc3.h(0)      # Hadamard on qubit 0
    qc3.cx(0, 1)  # CNOT gate (control=0, target=1)
    qc3.measure([0, 1], [0, 1])
    print("Circuit: H gate then CNOT gate")
    print(qc3.draw(output='text'))
    
    # Get statevector
    qc3_sv = QuantumCircuit(2)
    qc3_sv.h(0)
    qc3_sv.cx(0, 1)
    sv3 = Statevector.from_instruction(qc3_sv)
    print(f"Statevector: {sv3.data}")
    print("State: |Φ+⟩ = (|00⟩ + |11⟩)/√2 (Bell state)")
    
    job3 = simulator.run(qc3, shots=shots)
    counts3 = job3.result().get_counts()
    # Clean up results
    clean_counts3 = {}
    for key, value in counts3.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts3[clean_key] = value
    print(f"Results: {clean_counts3}")
    print("Observation: Only |00⟩ and |11⟩ appear (~50% each)")
    print("Correlation: Perfect correlation - qubits always match!")
    print()
    
    # PART 4: Verification with Multiple Measurements
    print("PART 4: Verification with Multiple Measurements")
    print("------------------------------------------------")
    print("Running Bell state circuit with different shot counts...")
    shot_counts = [100, 500, 1000, 5000]
    verification_results = []
    
    for shot_count in shot_counts:
        job = simulator.run(qc3, shots=shot_count)
        counts = job.result().get_counts()
        clean_counts = {}
        for key, value in counts.items():
            clean_key = key.split()[0] if ' ' in key else key
            clean_counts[clean_key] = value
        
        count_00 = clean_counts.get('00', 0)
        count_11 = clean_counts.get('11', 0)
        count_01 = clean_counts.get('01', 0)
        count_10 = clean_counts.get('10', 0)
        
        correlation = (count_00 + count_11) / shot_count * 100
        verification_results.append((shot_count, clean_counts, correlation))
        
        print(f"{shot_count:5d} shots: {clean_counts} - Correlation: {correlation:.1f}%")
    print()
    
    # Create comprehensive visualization
    print("CREATING VISUALIZATION...")
    fig = plt.figure(figsize=(20, 20))
    
    # Create grid layout with proper spacing - adding 4th row for statevectors
    gs = fig.add_gridspec(4, 4, height_ratios=[1.5, 1.2, 1.5, 1.5], 
                         hspace=0.65, wspace=0.4,
                         top=0.92, bottom=0.08, left=0.06, right=0.97)
    
    # Add title with proper spacing
    fig.suptitle('Lab 11: Bell States using Hadamard and CNOT Gates',
                 fontsize=18, fontweight='bold', y=0.97)
    
    # Row 1: State progression - measurement histograms
    states_data = [
        ("Initial State |00⟩", clean_counts1, '#95a5a6', 'Deterministic'),
        ("After Hadamard\n(Qubit 0)", clean_counts2, '#3498db', 'Partial Superposition'),
        ("Bell State |Φ+⟩\n(H + CNOT)", clean_counts3, '#2ecc71', 'Entangled'),
        ("Bell State |Φ+⟩\n(5000 shots)", verification_results[3][1], '#e74c3c', 'Verified')
    ]
    
    for i, (title, counts, color, label) in enumerate(states_data):
        ax = fig.add_subplot(gs[0, i])
        
        # Ensure all 4 states are shown
        all_states = ['00', '01', '10', '11']
        values = [counts.get(state, 0) for state in all_states]
        max_val = max(values) if max(values) > 0 else 1000
        
        bars = ax.bar(all_states, values, color=color,
                     alpha=0.85, edgecolor='black', linewidth=2)
        
        ax.set_title(title, fontweight='bold', fontsize=12, pad=20)
        ax.set_ylabel('Measurement Counts', fontsize=10, fontweight='bold')
        ax.set_xlabel('Quantum State', fontsize=10, fontweight='bold')
        ax.tick_params(labelsize=9)
        ax.set_ylim(0, max_val * 1.15)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add count labels on bars
        for bar, val in zip(bars, values):
            height = bar.get_height()
            if height > 0:
                ax.text(bar.get_x() + bar.get_width()/2., height + max_val*0.02,
                       f'{int(height)}', ha='center', va='bottom', 
                       fontweight='bold', fontsize=10)
                # Add percentage
                total = sum(values)
                percentage = (height / total) * 100 if total > 0 else 0
                if percentage > 5:  # Only show if significant
                    ax.text(bar.get_x() + bar.get_width()/2., height/2,
                           f'{percentage:.0f}%', ha='center', va='center',
                           fontsize=9, fontweight='bold', color='white',
                           bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.7))
        
        # Add label at bottom
        ax.text(0.5, -0.35, label, ha='center', fontsize=10,
               fontweight='bold', transform=ax.transAxes,
               bbox=dict(boxstyle='round,pad=0.4', facecolor=color, 
                        edgecolor='black', linewidth=1.5, alpha=0.5))
    
    # Row 2: Circuit diagrams for each state
    circuit_diagrams = [
        ("Initial |00⟩", "     ┌─┐   \nq_0: ┤M├───\n     └╥┘┌─┐\nq_1: ─╫─┤M├\n      ║ └╥┘\nc: 2/═╩══╩═\n      0  1"),
        ("After H Gate", "     ┌───┐┌─┐\nq_0: ┤ H ├┤M├\n     └┬─┬┘└╥┘\nq_1: ─┤M├──╫─\n      └╥┘  ║\nc: 2/══╩═══╩═\n       1   0"),
        ("Bell State |Φ+⟩", "     ┌───┐     ┌─┐\nq_0: ┤ H ├──■──┤M├───\n     └───┘┌─┴─┐└╥┘┌─┐\nq_1: ─────┤ X ├─╫─┤M├\n          └───┘ ║ └╥┘\nc: 2/═══════════╩══╩═\n                0  1"),
        ("Bell State (5000)", "     ┌───┐     ┌─┐\nq_0: ┤ H ├──■──┤M├───\n     └───┘┌─┴─┐└╥┘┌─┐\nq_1: ─────┤ X ├─╫─┤M├\n          └───┘ ║ └╥┘\nc: 2/═══════════╩══╩═\n                0  1")
    ]
    
    for i, (title, circuit) in enumerate(circuit_diagrams):
        ax = fig.add_subplot(gs[1, i])
        ax.axis('off')
        
        colors = ['#95a5a6', '#3498db', '#2ecc71', '#e74c3c']
        
        # Create circuit diagram box
        ax.text(0.5, 0.5, circuit, ha='center', va='center',
               fontsize=7.5, fontfamily='monospace', transform=ax.transAxes,
               bbox=dict(boxstyle='round,pad=0.6', facecolor=colors[i],
                        edgecolor='black', linewidth=2, alpha=0.3))
        
        ax.set_title(f"Circuit: {title}", fontweight='bold', fontsize=11, pad=20)
    
    # Row 3: Statevector information for each step
    statevector_info = [
        ("Step 1: Initial |00⟩", "No gates applied", [1, 0, 0, 0]),
        ("Step 2: After H Gate", "H on qubit 0\n|ψ⟩ = (|00⟩ + |10⟩)/√2", sv2.data),
        ("Step 3: Bell State |Φ+⟩", "H + CNOT gates\n|Φ+⟩ = (|00⟩ + |11⟩)/√2", sv3.data),
        ("Step 4: Verification", "Same Bell state\nwith more shots", sv3.data)
    ]
    
    for i, (title, desc, sv_data) in enumerate(statevector_info):
        ax = fig.add_subplot(gs[2, i])
        ax.axis('off')
        
        colors = ['#95a5a6', '#3498db', '#2ecc71', '#e74c3c']
        
        # Create info box with statevector
        info_text = f"{desc}\n\n"
        info_text += f"Statevector:\n"
        for j, amp in enumerate(sv_data):
            if abs(amp) > 0.01:
                info_text += f"|{j:02b}⟩: {amp.real:.3f}\n"
        
        ax.text(0.5, 0.5, info_text, ha='center', va='center',
               fontsize=9, fontfamily='monospace', transform=ax.transAxes,
               bbox=dict(boxstyle='round,pad=0.6', facecolor=colors[i],
                        edgecolor='black', linewidth=2, alpha=0.4))
        
        ax.set_title(f"{title}", fontweight='bold', fontsize=11, pad=20)
    
    # Row 4: Correlation analysis and verification
    # Left plot: Correlation comparison
    ax_corr = fig.add_subplot(gs[3, :2])
    
    state_names = ['Initial\n|00⟩', 'After H\n(Partial)', 'Bell State\n|Φ+⟩']
    correlations = []
    
    for counts in [clean_counts1, clean_counts2, clean_counts3]:
        same = counts.get('00', 0) + counts.get('11', 0)
        total = sum(counts.values())
        corr = (same / total * 100) if total > 0 else 0
        correlations.append(corr)
    
    bars = ax_corr.bar(state_names, correlations, 
                      color=['#95a5a6', '#3498db', '#2ecc71'],
                      alpha=0.85, edgecolor='black', linewidth=2)
    
    ax_corr.set_title('Correlation Analysis: Qubits Match (00 or 11)', 
                     fontweight='bold', fontsize=12, pad=20)
    ax_corr.set_ylabel('Correlation Percentage (%)', fontsize=11, fontweight='bold')
    ax_corr.set_ylim(0, 110)
    ax_corr.grid(axis='y', alpha=0.3, linestyle='--')
    ax_corr.axhline(y=50, color='red', linestyle='--', linewidth=2, alpha=0.7, label='50% (Random)')
    ax_corr.axhline(y=100, color='green', linestyle='--', linewidth=2, alpha=0.7, label='100% (Perfect)')
    
    for bar, val in zip(bars, correlations):
        height = bar.get_height()
        ax_corr.text(bar.get_x() + bar.get_width()/2., height + 2,
                    f'{val:.1f}%', ha='center', va='bottom', 
                    fontweight='bold', fontsize=11)
    
    ax_corr.legend(fontsize=10, loc='upper left')
    
    # Right plot: Shot count verification
    ax_verify = fig.add_subplot(gs[3, 2:])
    
    shot_labels = [f'{sc}' for sc, _, _ in verification_results]
    corr_values = [corr for _, _, corr in verification_results]
    
    bars = ax_verify.bar(shot_labels, corr_values,
                        color='#e74c3c', alpha=0.85, edgecolor='black', linewidth=2)
    
    ax_verify.set_title('Bell State Verification: Different Shot Counts',
                       fontweight='bold', fontsize=12, pad=20)
    ax_verify.set_xlabel('Number of Shots', fontsize=11, fontweight='bold')
    ax_verify.set_ylabel('Correlation (%)', fontsize=11, fontweight='bold')
    ax_verify.set_ylim(95, 105)
    ax_verify.grid(axis='y', alpha=0.3, linestyle='--')
    ax_verify.axhline(y=100, color='green', linestyle='--', linewidth=2, alpha=0.7, label='Theoretical (100%)')
    
    for bar, val in zip(bars, corr_values):
        height = bar.get_height()
        ax_verify.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                      f'{val:.1f}%', ha='center', va='bottom',
                      fontweight='bold', fontsize=10)
    
    ax_verify.legend(fontsize=10, loc='lower right')
    
    # Add summary footer
    summary_text = '✓ Bell State Created  ✓ Perfect Correlation Verified  ✓ H + CNOT = Entanglement  ✓ Theoretical Predictions Confirmed'
    fig.text(0.5, 0.02, summary_text, ha='center', fontsize=12, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.5", facecolor="#ffffcc", 
                      edgecolor='#ff9800', linewidth=2.5, alpha=0.9))
    
    plt.savefig('qiskit_lab_11_final_image.png', dpi=300, bbox_inches='tight',
                facecolor='white', pad_inches=0.3)
    print("✓ Visualization saved as 'qiskit_lab_11_final_image.png'")
    plt.show()
    
    print()
    print("OBSERVATIONS & RESULTS")
    print("======================")
    print("1. Initial |00⟩: Deterministic state (100% |00⟩)")
    print("2. After H: Partial superposition (50% |00⟩, 50% |10⟩)")
    print("3. Bell State: Entangled state (50% |00⟩, 50% |11⟩)")
    print("4. Verification: Correlation remains ~100% across all shot counts")
    print()
    print("BELL STATE CREATION PROCESS")
    print("============================")
    print("Step 1: Start with |00⟩")
    print("Step 2: Apply H gate to qubit 0 → (|00⟩ + |10⟩)/√2")
    print("Step 3: Apply CNOT(0→1) → (|00⟩ + |11⟩)/√2 = |Φ+⟩")
    print("Result: Maximally entangled Bell state")
    print()
    print("CORRELATION VERIFICATION")
    print("========================")
    print(f"✓ Initial state: {correlations[0]:.1f}% correlation (deterministic)")
    print(f"✓ After H gate: {correlations[1]:.1f}% correlation (independent)")
    print(f"✓ Bell state: {correlations[2]:.1f}% correlation (perfect entanglement)")
    print()
    print("THEORETICAL VERIFICATION")
    print("========================")
    print("✓ Hadamard gate creates superposition")
    print("✓ CNOT gate creates entanglement")
    print("✓ Bell state shows perfect correlation")
    print("✓ Only |00⟩ and |11⟩ outcomes observed")
    print("✓ Results match theoretical predictions")
    print()
    print("CONCLUSION")
    print("==========")
    print("✓ Successfully created Bell state |Φ+⟩ using H and CNOT gates")
    print("✓ Verified perfect correlation between entangled qubits")
    print("✓ Demonstrated quantum entanglement experimentally")
    print("✓ Confirmed theoretical expectations with multiple measurements")

if __name__ == "__main__":
    main()
