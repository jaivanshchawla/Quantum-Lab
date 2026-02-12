"""
Lab 7: Hadamard Gate and Bloch Sphere Visualization
===================================================
Objective: Create superposition and visualize Bloch sphere
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("LAB 7: HADAMARD GATE AND BLOCH SPHERE VISUALIZATION")
    print("====================================================")
    print()
    
    # Initialize simulator
    simulator = AerSimulator()
    
    # PART 1: Initial State |0⟩
    print("PART 1: Initial State |0⟩")
    print("-------------------------")
    qc1 = QuantumCircuit(1)
    state1 = Statevector.from_instruction(qc1)
    print("Circuit: No gates (initial state)")
    print(qc1.draw(output='text'))
    print(f"State vector: {state1.data}")
    print("Bloch coordinates: (x=0, y=0, z=1) - North pole")
    print()
    
    # PART 2: Hadamard Gate Applied
    print("PART 2: Hadamard Gate Applied")
    print("-----------------------------")
    qc2 = QuantumCircuit(1)
    qc2.h(0)
    state2 = Statevector.from_instruction(qc2)
    print("Circuit: H gate")
    print(qc2.draw(output='text'))
    print(f"State vector: {state2.data}")
    print("Bloch coordinates: (x=1, y=0, z=0) - Equator (+X)")
    print()
    
    # PART 3: X Gate Applied
    print("PART 3: X Gate Applied")
    print("----------------------")
    qc3 = QuantumCircuit(1)
    qc3.x(0)
    state3 = Statevector.from_instruction(qc3)
    print("Circuit: X gate")
    print(qc3.draw(output='text'))
    print(f"State vector: {state3.data}")
    print("Bloch coordinates: (x=0, y=0, z=-1) - South pole")
    print()
    
    # PART 4: Y Gate Applied
    print("PART 4: Y Gate Applied")
    print("----------------------")
    qc4 = QuantumCircuit(1)
    qc4.y(0)
    state4 = Statevector.from_instruction(qc4)
    print("Circuit: Y gate")
    print(qc4.draw(output='text'))
    print(f"State vector: {state4.data}")
    print("Bloch coordinates: (x=0, y=0, z=-1) - South pole (via Y)")
    print()
    
    # PART 5: Measurement Results
    print("PART 5: Measurement Results")
    print("---------------------------")
    
    # Measure initial state
    qc1_m = QuantumCircuit(1, 1)
    qc1_m.measure(0, 0)
    job1 = simulator.run(qc1_m, shots=1000)
    counts1 = job1.result().get_counts()
    print(f"|0⟩ state: {counts1}")
    
    # Measure after Hadamard
    qc2_m = QuantumCircuit(1, 1)
    qc2_m.h(0)
    qc2_m.measure(0, 0)
    job2 = simulator.run(qc2_m, shots=1000)
    counts2 = job2.result().get_counts()
    print(f"H|0⟩ state: {counts2}")
    
    # Measure after X
    qc3_m = QuantumCircuit(1, 1)
    qc3_m.x(0)
    qc3_m.measure(0, 0)
    job3 = simulator.run(qc3_m, shots=1000)
    counts3 = job3.result().get_counts()
    print(f"X|0⟩ state: {counts3}")
    
    # Measure after Y
    qc4_m = QuantumCircuit(1, 1)
    qc4_m.y(0)
    qc4_m.measure(0, 0)
    job4 = simulator.run(qc4_m, shots=1000)
    counts4 = job4.result().get_counts()
    print(f"Y|0⟩ state: {counts4}")
    print()
    
    # Create comprehensive visualization (matplotlib)
    fig = plt.figure(figsize=(16, 10))
    fig.suptitle('Lab 7: Hadamard Gate and Quantum States', fontsize=16, fontweight='bold', y=0.95)
    
    # Create grid layout
    gs = fig.add_gridspec(2, 4, height_ratios=[1.2, 1], hspace=0.3, wspace=0.3)
    
    # Top row: Circuit diagrams with state vectors
    circuits_info = [
        ("Initial |0⟩", "  \nq:", state1.data, 'lightblue', "(0,0,1)"),
        ("Hadamard H|0⟩", "     ┌───┐\n  q: ┤ H ├\n     └───┘", state2.data, 'lightgreen', "(1,0,0)"),
        ("Pauli-X X|0⟩", "     ┌───┐\n  q: ┤ X ├\n     └───┘", state3.data, 'lightyellow', "(0,0,-1)"),
        ("Pauli-Y Y|0⟩", "     ┌───┐\n  q: ┤ Y ├\n     └───┘", state4.data, 'lightsalmon', "(0,0,-1)")
    ]
    
    for i, (title, circuit, state_vec, color, bloch_coords) in enumerate(circuits_info):
        ax = fig.add_subplot(gs[0, i])
        ax.text(0.5, 0.95, title, ha='center', fontsize=10, fontweight='bold', transform=ax.transAxes)
        ax.text(0.5, 0.7, circuit, ha='center', fontsize=7, fontfamily='monospace', 
                transform=ax.transAxes, bbox=dict(boxstyle="round,pad=0.1", facecolor=color, alpha=0.4))
        
        # Display state vector
        state_str = f"State: {state_vec[0]:.3f}|0⟩"
        if len(state_vec) > 1:
            state_str += f" + {state_vec[1]:.3f}|1⟩"
        ax.text(0.5, 0.45, state_str, ha='center', fontsize=8, transform=ax.transAxes)
        
        # Display Bloch coordinates
        ax.text(0.5, 0.3, f"Bloch: {bloch_coords}", ha='center', fontsize=8, 
                transform=ax.transAxes, style='italic')
        
        # Display measurement results
        ax.text(0.5, 0.1, f'{[counts1, counts2, counts3, counts4][i]}', 
                ha='center', fontsize=9, fontweight='bold', transform=ax.transAxes)
        ax.axis('off')
    
    # Bottom row: Measurement bar charts
    test_results = [counts1, counts2, counts3, counts4]
    colors_bar = ['skyblue', 'lightgreen', 'gold', 'salmon']
    titles_bar = ['|0⟩ Measurements', 'H|0⟩ Measurements', 'X|0⟩ Measurements', 'Y|0⟩ Measurements']
    
    for i, (counts, color, title) in enumerate(zip(test_results, colors_bar, titles_bar)):
        ax = fig.add_subplot(gs[1, i])
        
        states_list = list(counts.keys())
        values = list(counts.values())
        bars = ax.bar(states_list, values, color=color, alpha=0.8, edgecolor='black', linewidth=1)
        
        ax.set_title(title, fontweight='bold', fontsize=9)
        ax.set_ylabel('Counts', fontsize=8)
        ax.set_xlabel('Measurement', fontsize=8)
        ax.tick_params(labelsize=7)
        ax.set_ylim(0, 1100)
        ax.grid(True, alpha=0.3, axis='y')
        
        # Add count labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 20,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=8)
    
    # Add theory summary
    fig.text(0.5, 0.08, 'HADAMARD MATRIX: H = (1/√2)[[1,1],[1,-1]] | Creates equal superposition: H|0⟩ = (|0⟩+|1⟩)/√2 = |+⟩', 
             ha='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", edgecolor="orange"))
    fig.text(0.5, 0.03, 'BLOCH SPHERE: Geometric representation | North pole=|0⟩ | South pole=|1⟩ | Equator=superposition | Coordinates=(x,y,z)', 
             ha='center', fontsize=10, fontweight='bold', color='darkgreen')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.88, bottom=0.15)
    plt.savefig('qiskit_lab_7_final_image.png', dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.05)
    plt.close()
    
    print("✓ Main visualization saved as 'qiskit_lab_7_final_image.png'")
    print()
    
    # Create Bloch sphere visualizations using Qiskit
    print("PART 6: Bloch Sphere Visualizations")
    print("------------------------------------")
    
    # Plot each state on Bloch sphere separately
    states_to_plot = [state1, state2, state3, state4]
    state_titles = ['|0⟩ State (North Pole)', 'H|0⟩ = |+⟩ (Equator +X)', 'X|0⟩ = |1⟩ (South Pole)', 'Y|0⟩ = i|1⟩ (South Pole)']
    
    for i, (state, title) in enumerate(zip(states_to_plot, state_titles)):
        fig_bloch = plot_bloch_multivector(state, title=title)
        fig_bloch.savefig(f'qiskit_lab_7_bloch_{i+1}.png', dpi=300, bbox_inches='tight', facecolor='white')
        plt.close(fig_bloch)
        print(f"✓ Bloch sphere {i+1} saved as 'qiskit_lab_7_bloch_{i+1}.png'")
    
    print()
    
    print("HADAMARD AND BLOCH SPHERE ANALYSIS COMPLETE")
    print("============================================")
    print("✓ Initial state |0⟩ at North pole of Bloch sphere")
    print("✓ Hadamard creates superposition at equator")
    print("✓ X gate flips to South pole |1⟩")
    print("✓ Y gate also reaches South pole with phase")
    print("✓ Measurement results verify quantum states")
    print()
    print("THEORETICAL VERIFICATION:")
    print("=========================")
    print("• |0⟩: Bloch vector (0,0,1) → Always measures 0")
    print("• H|0⟩ = |+⟩: Bloch vector (1,0,0) → 50% each")
    print("• X|0⟩ = |1⟩: Bloch vector (0,0,-1) → Always measures 1")
    print("• Y|0⟩ = i|1⟩: Bloch vector (0,0,-1) → Always measures 1")
    print()
    print("OUTPUT FILES:")
    print("=============")
    print("✓ qiskit_lab_7_final_image.png - Main visualization")
    print("✓ qiskit_lab_7_bloch_1.png - |0⟩ state Bloch sphere")
    print("✓ qiskit_lab_7_bloch_2.png - H|0⟩ state Bloch sphere")
    print("✓ qiskit_lab_7_bloch_3.png - X|0⟩ state Bloch sphere")
    print("✓ qiskit_lab_7_bloch_4.png - Y|0⟩ state Bloch sphere")
    print()
    print("CONCLUSION:")
    print("===========")
    print("✓ Hadamard gate creates equal superposition")
    print("✓ Bloch sphere provides geometric visualization")
    print("✓ Different gates move state to different positions")
    print("✓ Multiple visualizations created successfully")

if __name__ == "__main__":
    main()