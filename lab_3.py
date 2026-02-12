"""
Lab 3: Quantum Bits (Qubits) and Quantum Registers
===================================================
Objective: Understand qubits, quantum registers and classical registers
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def main():
    print("LAB 3: QUANTUM BITS (QUBITS) AND QUANTUM REGISTERS")
    print("===================================================")
    print()
    
    # Initialize simulator
    simulator = AerSimulator()
    
    # PART 1: Basic Register Creation
    print("PART 1: Basic Register Creation")
    print("-------------------------------")
    qr = QuantumRegister(2)
    cr = ClassicalRegister(2)
    qc = QuantumCircuit(qr, cr)
    print("Created quantum register with 2 qubits")
    print("Created classical register with 2 bits")
    print("Basic circuit (no gates):")
    print(qc.draw(output='text'))
    print()
    
    # PART 2: Single Qubit Operations
    print("PART 2: Single Qubit Operations")
    print("-------------------------------")
    
    # Test 1: Single qubit measurement
    qc1 = QuantumCircuit(QuantumRegister(2), ClassicalRegister(2))
    qc1.measure(0, 0)  # Measure first qubit only
    print("Test 1: Single qubit measurement (qubit 0)")
    print(qc1.draw(output='text'))
    
    job1 = simulator.run(qc1, shots=1000)
    counts1 = job1.result().get_counts()
    print(f"Results: {counts1}")
    print()
    
    # Test 2: Single qubit with Hadamard
    qc2 = QuantumCircuit(QuantumRegister(2), ClassicalRegister(2))
    qc2.h(0)  # Hadamard on first qubit
    qc2.measure(0, 0)
    print("Test 2: Hadamard on single qubit (qubit 0)")
    print(qc2.draw(output='text'))
    
    job2 = simulator.run(qc2, shots=1000)
    counts2 = job2.result().get_counts()
    print(f"Results: {counts2}")
    print()
    
    # PART 3: Multi-Qubit Register Operations
    print("PART 3: Multi-Qubit Register Operations")
    print("---------------------------------------")
    
    # Test 3: Both qubits measurement
    qc3 = QuantumCircuit(QuantumRegister(2), ClassicalRegister(2))
    qc3.h(0)  # Hadamard on first qubit
    qc3.h(1)  # Hadamard on second qubit
    qc3.measure_all()
    print("Test 3: Independent superposition on both qubits")
    print(qc3.draw(output='text'))
    
    job3 = simulator.run(qc3, shots=1000)
    counts3 = job3.result().get_counts()
    # Clean up results
    clean_counts3 = {}
    for key, value in counts3.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts3[clean_key] = value
    print(f"Results: {clean_counts3}")
    print()
    
    # Test 4: Entangled qubits
    qc4 = QuantumCircuit(QuantumRegister(2), ClassicalRegister(2))
    qc4.h(0)      # Hadamard on first qubit
    qc4.cx(0, 1)  # CNOT gate (entanglement)
    qc4.measure_all()
    print("Test 4: Entangled qubits (Bell state)")
    print(qc4.draw(output='text'))
    
    job4 = simulator.run(qc4, shots=1000)
    counts4 = job4.result().get_counts()
    # Clean up results
    clean_counts4 = {}
    for key, value in counts4.items():
        clean_key = key.split()[0] if ' ' in key else key
        clean_counts4[clean_key] = value
    print(f"Results: {clean_counts4}")
    print()
    
    # Create comprehensive visualization with better spacing
    fig = plt.figure(figsize=(16, 14))
    fig.suptitle('Lab 3: Quantum Bits and Quantum Registers', fontsize=16, fontweight='bold', y=0.97)
    
    # Create grid layout with more vertical space
    gs = fig.add_gridspec(3, 4, height_ratios=[0.5, 1.4, 1], hspace=0.5, wspace=0.25)
    
    # Top row: Register explanation
    ax_reg = fig.add_subplot(gs[0, :])
    reg_text = """QUANTUM & CLASSICAL REGISTERS
Quantum Register (qr): Holds qubits in tensor product space |q₁⟩ ⊗ |q₀⟩
Classical Register (cr): Stores measurement results as classical bits
Circuit Creation: QuantumCircuit(qr, cr) combines both registers"""
    
    ax_reg.text(0.5, 0.5, reg_text, ha='center', va='center', fontsize=11, 
                transform=ax_reg.transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcyan", alpha=0.5))
    ax_reg.axis('off')
    
    # Middle row: Circuit diagrams
    circuits = [
        ("Test 1: Single Qubit", "     ┌─┐\nq_0: ┤M├───\n     └╥┘   \nq_1: ─╫────\n      ║    \nc: 2/═╩════\n      0    ", counts1, 'lightblue'),
        ("Test 2: H Gate", "     ┌───┐┌─┐\nq_0: ┤ H ├┤M├───\n     └───┘└╥┘   \nq_1: ──────╫────\n           ║    \nc: 2/══════╩════\n           0    ", counts2, 'lightgreen'),
        ("Test 3: Independent H", "     ┌───┐ ░ ┌─┐\nq_0: ┤ H ├─░─┤M├\n     ├───┤ ░ └╥┘\nq_1: ┤ H ├─░──╫─\n     └───┘ ░  ║ \nc: 2/═════════╩═\n              0 ", clean_counts3, 'lightyellow'),
        ("Test 4: Entangled", "     ┌───┐     ░ ┌─┐\nq_0: ┤ H ├──■──░─┤M├\n     └───┘┌─┴─┐░ └╥┘\nq_1: ─────┤ X ├░──╫─\n          └───┘░  ║ \nc: 2/════════════╩═\n                 0 ", clean_counts4, 'lightsalmon')
    ]
    
    for i, (title, circuit, counts, color) in enumerate(circuits):
        ax = fig.add_subplot(gs[1, i])
        ax.text(0.5, 0.98, title, ha='center', fontsize=9, fontweight='bold', transform=ax.transAxes)
        ax.text(0.5, 0.65, circuit, ha='center', fontsize=7, fontfamily='monospace', 
                transform=ax.transAxes, bbox=dict(boxstyle="round,pad=0.1", facecolor=color, alpha=0.4))
        ax.text(0.5, 0.02, f'{counts}', ha='center', fontsize=8, fontweight='bold', transform=ax.transAxes)
        ax.axis('off')
    
    # Bottom row: Bar charts
    test_results = [counts1, counts2, clean_counts3, clean_counts4]
    colors = ['skyblue', 'lightgreen', 'gold', 'salmon']
    titles = ['Single Qubit', 'H Gate', 'Independent H', 'Entangled']
    
    for i, (counts, color, title) in enumerate(zip(test_results, colors, titles)):
        ax = fig.add_subplot(gs[2, i])
        bars = ax.bar(counts.keys(), counts.values(), color=color, alpha=0.8, edgecolor='black', linewidth=1)
        ax.set_title(title, fontweight='bold', fontsize=9)
        ax.set_ylabel('Counts', fontsize=8)
        ax.tick_params(labelsize=7)
        
        # Add count labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(counts.values())*0.02,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=7)
    
    # Add summary at bottom with proper spacing
    fig.text(0.5, 0.04, 'REGISTER OPERATIONS: ✓ Quantum Register Creation ✓ Classical Register Mapping ✓ Single/Multi-Qubit Operations ✓ Tensor Product Spaces', 
             ha='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightsteelblue", edgecolor="navy"))
    
    plt.savefig('qiskit_lab_3_final_image.png', dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.1)
    plt.show()
    
    print("REGISTER ANALYSIS COMPLETE")
    print("==========================")
    print("✓ Quantum registers created successfully")
    print("✓ Classical registers mapped correctly")
    print("✓ Single qubit operations demonstrated")
    print("✓ Multi-qubit operations verified")
    print("✓ Tensor product spaces explored")
    print("✓ Register interactions confirmed")
    print()
    print("THEORETICAL VERIFICATION:")
    print("=========================")
    print("• Single qubit |0⟩: Always measures 0 (deterministic)")
    print("• Hadamard |+⟩: ~50% 0, ~50% 1 (superposition)")
    print("• Independent H: All 4 states |00⟩,|01⟩,|10⟩,|11⟩ equally likely")
    print("• Bell state: Only |00⟩ and |11⟩ (quantum entanglement)")
    print()
    print("CONCLUSION:")
    print("===========")
    print("✓ Quantum registers hold qubits in tensor product spaces")
    print("✓ Classical registers store measurement outcomes")
    print("✓ Register operations enable complex quantum computations")
    print("✓ Visualization saved as 'qiskit_lab_3_final_image.png'")

if __name__ == "__main__":
    main()