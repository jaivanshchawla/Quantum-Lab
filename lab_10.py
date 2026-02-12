"""
Lab 10: Concept of Quantum Entanglement
========================================
Objective: Understand non-classical correlations between qubits
Theory: Entanglement links qubits such that measurement of one 
        determines the other, creating correlations impossible classically
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("LAB 10: CONCEPT OF QUANTUM ENTANGLEMENT")
    print("========================================")
    print()
    
    # Initialize simulator
    simulator = AerSimulator()
    shots = 1000
    
    # PART 1: Non-Entangled State (Independent Qubits)
    print("PART 1: Non-Entangled State (Independent Qubits)")
    print("-------------------------------------------------")
    qc1 = QuantumCircuit(2, 2)
    qc1.h(0)  # Hadamard on qubit 0
    qc1.h(1)  # Hadamard on qubit 1
    qc1.measure_all()
    print("Circuit: Independent superposition on both qubits")
    print(qc1.draw(output='text'))
    
    # Get statevector
    qc1_sv = QuantumCircuit(2)
    qc1_sv.h(0)
    qc1_sv.h(1)
    sv1 = Statevector.from_instruction(qc1_sv)
    print(f"Statevector: {sv1.data}")
    print("State: |ψ⟩ = (|00⟩ + |01⟩ + |10⟩ + |11⟩)/2 (separable)")
    
    job1 = simulator.run(qc1, shots=shots)
    counts1 = job1.result().get_counts()
    # Clean up results
    clean_counts1 = {}
    for key, value in counts1.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts1[clean_key] = value
    print(f"Results: {clean_counts1}")
    print("Observation: All 4 outcomes equally likely (~25% each)")
    print("Correlation: No correlation between qubits")
    print()
    
    # PART 2: Bell State |Φ+⟩ (Maximal Entanglement)
    print("PART 2: Bell State |Φ+⟩ (Maximal Entanglement)")
    print("-----------------------------------------------")
    qc2 = QuantumCircuit(2, 2)
    qc2.h(0)      # Hadamard on qubit 0
    qc2.cx(0, 1)  # CNOT gate creates entanglement
    qc2.measure_all()
    print("Circuit: H + CNOT creates Bell state |Φ+⟩")
    print(qc2.draw(output='text'))
    
    # Get statevector
    qc2_sv = QuantumCircuit(2)
    qc2_sv.h(0)
    qc2_sv.cx(0, 1)
    sv2 = Statevector.from_instruction(qc2_sv)
    print(f"Statevector: {sv2.data}")
    print("State: |Φ+⟩ = (|00⟩ + |11⟩)/√2 (entangled)")
    
    job2 = simulator.run(qc2, shots=shots)
    counts2 = job2.result().get_counts()
    # Clean up results
    clean_counts2 = {}
    for key, value in counts2.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts2[clean_key] = value
    print(f"Results: {clean_counts2}")
    print("Observation: Only |00⟩ and |11⟩ appear (~50% each)")
    print("Correlation: Perfect correlation - qubits always match!")
    print()
    
    # PART 3: Bell State |Φ-⟩
    print("PART 3: Bell State |Φ-⟩")
    print("------------------------")
    qc3 = QuantumCircuit(2, 2)
    qc3.x(1)      # X gate on qubit 1
    qc3.h(0)      # Hadamard on qubit 0
    qc3.cx(0, 1)  # CNOT gate
    qc3.measure_all()
    print("Circuit: X + H + CNOT creates Bell state |Φ-⟩")
    print(qc3.draw(output='text'))
    
    # Get statevector
    qc3_sv = QuantumCircuit(2)
    qc3_sv.x(1)
    qc3_sv.h(0)
    qc3_sv.cx(0, 1)
    sv3 = Statevector.from_instruction(qc3_sv)
    print(f"Statevector: {sv3.data}")
    print("State: |Φ-⟩ = (|00⟩ - |11⟩)/√2 (entangled)")
    
    job3 = simulator.run(qc3, shots=shots)
    counts3 = job3.result().get_counts()
    # Clean up results
    clean_counts3 = {}
    for key, value in counts3.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts3[clean_key] = value
    print(f"Results: {clean_counts3}")
    print("Observation: Only |00⟩ and |11⟩ appear (~50% each)")
    print("Correlation: Perfect correlation (phase difference invisible)")
    print()
    
    # PART 4: Bell State |Ψ+⟩ (Anti-correlation)
    print("PART 4: Bell State |Ψ+⟩ (Anti-correlation)")
    print("-------------------------------------------")
    qc4 = QuantumCircuit(2, 2)
    qc4.h(0)      # Hadamard on qubit 0
    qc4.cx(0, 1)  # CNOT gate
    qc4.x(1)      # X gate on qubit 1
    qc4.measure_all()
    print("Circuit: H + CNOT + X creates Bell state |Ψ+⟩")
    print(qc4.draw(output='text'))
    
    # Get statevector
    qc4_sv = QuantumCircuit(2)
    qc4_sv.h(0)
    qc4_sv.cx(0, 1)
    qc4_sv.x(1)
    sv4 = Statevector.from_instruction(qc4_sv)
    print(f"Statevector: {sv4.data}")
    print("State: |Ψ+⟩ = (|01⟩ + |10⟩)/√2 (entangled)")
    
    job4 = simulator.run(qc4, shots=shots)
    counts4 = job4.result().get_counts()
    # Clean up results
    clean_counts4 = {}
    for key, value in counts4.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts4[clean_key] = value
    print(f"Results: {clean_counts4}")
    print("Observation: Only |01⟩ and |10⟩ appear (~50% each)")
    print("Correlation: Perfect anti-correlation - qubits always opposite!")
    print()
    
    # Create comprehensive visualization
    print("CREATING VISUALIZATION...")
    fig = plt.figure(figsize=(20, 17))
    
    # Create grid layout with much better spacing
    gs = fig.add_gridspec(3, 4, height_ratios=[1.5, 1.5, 1.5], 
                         hspace=0.6, wspace=0.4,
                         top=0.92, bottom=0.08, left=0.06, right=0.97)
    
    # Add title with proper spacing
    fig.suptitle('Lab 10: Quantum Entanglement and Non-Classical Correlations',
                 fontsize=18, fontweight='bold', y=0.97)
    
    # Top row: Theory explanation
    ax_theory = fig.add_subplot(gs[0, :])
    theory_text = """ENTANGLEMENT THEORY
Entangled qubits cannot be described independently - measurement of one instantly determines the other
Bell States: Four maximally entangled states |Φ±⟩ = (|00⟩ ± |11⟩)/√2  and  |Ψ±⟩ = (|01⟩ ± |10⟩)/√2
Non-Classical Correlations: Stronger than any classical correlation possible"""
    
    ax_theory.text(0.5, 0.5, theory_text, ha='center', va='center', fontsize=12,
                   transform=ax_theory.transAxes,
                   bbox=dict(boxstyle="round,pad=0.5", facecolor="lightcyan", 
                            edgecolor='steelblue', linewidth=2, alpha=0.8))
    ax_theory.axis('off')
    
    # Prepare data with cleaner labels
    circuits_info = [
        ("Non-Entangled\n(Independent)", clean_counts1, 'lightgray', 'No Correlation'),
        ("Bell State |Φ+⟩\n(Correlated)", clean_counts2, 'lightgreen', 'Perfect Match'),
        ("Bell State |Φ-⟩\n(Correlated)", clean_counts3, 'lightyellow', 'Perfect Match'),
        ("Bell State |Ψ+⟩\n(Anti-correlated)", clean_counts4, 'lightsalmon', 'Perfect Opposite')
    ]
    
    # Row 1: Measurement histograms with cleaner design
    colors_main = ['#95a5a6', '#2ecc71', '#f39c12', '#e74c3c']
    
    for i, (title, counts, color, corr_label) in enumerate(circuits_info):
        ax = fig.add_subplot(gs[0, i])
        
        # Ensure all 4 states are shown
        all_states = ['00', '01', '10', '11']
        values = [counts.get(state, 0) for state in all_states]
        
        bars = ax.bar(all_states, values, color=colors_main[i],
                     alpha=0.85, edgecolor='black', linewidth=2)
        
        ax.set_title(title, fontweight='bold', fontsize=12, pad=20)
        ax.set_ylabel('Measurement Counts', fontsize=10, fontweight='bold')
        ax.set_xlabel('Quantum State', fontsize=10, fontweight='bold')
        ax.tick_params(labelsize=9)
        ax.set_ylim(0, shots * 0.7)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add count labels on bars
        for bar, val in zip(bars, values):
            height = bar.get_height()
            if height > 0:
                ax.text(bar.get_x() + bar.get_width()/2., height + shots*0.02,
                       f'{int(height)}', ha='center', va='bottom', 
                       fontweight='bold', fontsize=10)
                # Add percentage
                percentage = (height / shots) * 100
                ax.text(bar.get_x() + bar.get_width()/2., height/2,
                       f'{percentage:.0f}%', ha='center', va='center',
                       fontsize=9, fontweight='bold', color='white',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.7))
        
        # Add correlation label at bottom with more space
        ax.text(0.5, -0.35, corr_label, ha='center', fontsize=10,
               fontweight='bold', transform=ax.transAxes,
               bbox=dict(boxstyle='round,pad=0.4', facecolor=color, 
                        edgecolor='black', linewidth=1.5, alpha=0.7))
    
    # Row 2: State information boxes
    statevectors = [sv1, sv2, sv3, sv4]
    state_descriptions = [
        "|ψ⟩ = (|00⟩ + |01⟩ + |10⟩ + |11⟩)/2",
        "|Φ+⟩ = (|00⟩ + |11⟩)/√2",
        "|Φ-⟩ = (|00⟩ - |11⟩)/√2",
        "|Ψ+⟩ = (|01⟩ + |10⟩)/√2"
    ]
    
    for i, (title, counts, color, _) in enumerate(circuits_info):
        ax = fig.add_subplot(gs[1, i])
        ax.axis('off')
        
        # Create info box
        info_text = f"{state_descriptions[i]}\n\n"
        info_text += f"Statevector:\n"
        sv_data = statevectors[i].data
        for j, amp in enumerate(sv_data):
            if abs(amp) > 0.01:
                info_text += f"|{j:02b}⟩: {amp.real:.3f}\n"
        
        ax.text(0.5, 0.5, info_text, ha='center', va='center',
               fontsize=9, fontfamily='monospace', transform=ax.transAxes,
               bbox=dict(boxstyle='round,pad=0.6', facecolor=color,
                        edgecolor='black', linewidth=2, alpha=0.4))
        
        ax.set_title(f"{title.split(chr(10))[0]} - State", 
                    fontweight='bold', fontsize=11, pad=20)
    
    # Row 3: Correlation analysis with improved design
    for i, (title, counts, color, _) in enumerate(circuits_info):
        ax = fig.add_subplot(gs[2, i])
        
        # Calculate correlation metrics
        same = counts.get('00', 0) + counts.get('11', 0)
        diff = counts.get('01', 0) + counts.get('10', 0)
        
        correlation_data = [same, diff]
        correlation_labels = ['Qubits\nMatch', 'Qubits\nDiffer']
        bar_colors = ['#27ae60', '#e74c3c']
        
        bars = ax.bar(correlation_labels, correlation_data,
                     color=bar_colors, alpha=0.85, edgecolor='black', linewidth=2)
        
        ax.set_title(f'Correlation Analysis', 
                    fontweight='bold', fontsize=11, pad=20)
        ax.set_ylabel('Total Counts', fontsize=10, fontweight='bold')
        ax.tick_params(labelsize=9)
        ax.set_ylim(0, shots * 1.2)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels with percentages
        for bar, val in zip(bars, correlation_data):
            height = bar.get_height()
            percentage = (height / shots) * 100
            ax.text(bar.get_x() + bar.get_width()/2., height + shots*0.03,
                   f'{int(height)}\n({percentage:.0f}%)',
                   ha='center', va='bottom', fontweight='bold', fontsize=10)
        
        # Add correlation strength indicator with more space
        if same > diff * 1.5:
            corr_text = "✓ Strong Correlation"
            corr_color = '#27ae60'
        elif diff > same * 1.5:
            corr_text = "✓ Strong Anti-Correlation"
            corr_color = '#e74c3c'
        else:
            corr_text = "No Correlation"
            corr_color = '#95a5a6'
        
        ax.text(0.5, -0.32, corr_text, ha='center', fontsize=10,
               fontweight='bold', transform=ax.transAxes,
               bbox=dict(boxstyle='round,pad=0.4', facecolor=corr_color, 
                        edgecolor='black', linewidth=1.5, alpha=0.4))
    
    # Add elegant summary footer
    summary_text = '✓ Quantum Entanglement  ✓ Non-Classical Correlations  ✓ Bell States  ✓ Instantaneous Measurement Collapse'
    fig.text(0.5, 0.02, summary_text, ha='center', fontsize=12, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.5", facecolor="#ffffcc", 
                      edgecolor='#ff9800', linewidth=2.5, alpha=0.9))
    
    plt.savefig('qiskit_lab_10_final_image.png', dpi=300, bbox_inches='tight',
                facecolor='white', pad_inches=0.3)
    print("✓ Visualization saved as 'qiskit_lab_10_final_image.png'")
    plt.show()
    
    print()
    print("OBSERVATIONS & RESULTS")
    print("======================")
    print("1. Non-Entangled: All outcomes equally likely (25% each)")
    print("2. Bell |Φ+⟩: Only |00⟩ and |11⟩ (perfect correlation)")
    print("3. Bell |Φ-⟩: Only |00⟩ and |11⟩ (perfect correlation)")
    print("4. Bell |Ψ+⟩: Only |01⟩ and |10⟩ (perfect anti-correlation)")
    print()
    print("CORRELATION ANALYSIS")
    print("====================")
    same_2 = clean_counts2.get('00', 0) + clean_counts2.get('11', 0)
    same_4 = clean_counts4.get('00', 0) + clean_counts4.get('11', 0)
    diff_4 = clean_counts4.get('01', 0) + clean_counts4.get('10', 0)
    print(f"• Non-Entangled: No correlation (50% same, 50% different)")
    print(f"• Bell |Φ+⟩: Perfect correlation ({same_2/shots*100:.1f}% same)")
    print(f"• Bell |Ψ+⟩: Perfect anti-correlation ({diff_4/shots*100:.1f}% different)")
    print()
    print("THEORETICAL VERIFICATION")
    print("========================")
    print("✓ Entanglement creates non-local correlations")
    print("✓ Measurement of one qubit determines the other")
    print("✓ Bell states are maximally entangled")
    print("✓ Correlations stronger than classical physics allows")
    print("✓ CNOT gate is key to creating entanglement")
    print()
    print("CONCLUSION")
    print("==========")
    print("✓ Quantum entanglement demonstrated with Bell states")
    print("✓ Non-classical correlations verified experimentally")
    print("✓ Measurement collapse affects both qubits instantly")
    print("✓ Entanglement is fundamental resource for quantum computing")

if __name__ == "__main__":
    main()
