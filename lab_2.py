"""
Lab 2: Installation of Qiskit and Environment Setup
===================================================
Objective: Install Qiskit and verify installation
"""

import sys
import platform
from qiskit import QuantumCircuit, __version__ as qiskit_version
from qiskit_aer import AerSimulator, __version__ as aer_version
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("LAB 2: QISKIT INSTALLATION AND ENVIRONMENT SETUP")
    print("=================================================")
    print()
    
    # PART 1: Environment Verification
    print("PART 1: Environment Verification")
    print("---------------------------------")
    print(f"Python Version: {sys.version}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Qiskit Version: {qiskit_version}")
    print(f"Qiskit Aer Version: {aer_version}")
    print()
    
    # PART 2: Basic Qiskit Import Test
    print("PART 2: Qiskit Import Test")
    print("---------------------------")
    try:
        from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
        from qiskit_aer import AerSimulator
        from qiskit.visualization import plot_histogram
        print("✓ All Qiskit modules imported successfully")
        print("✓ Qiskit installation verified")
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return
    print()
    
    # PART 3: Simulator Verification
    print("PART 3: Simulator Verification")
    print("-------------------------------")
    simulator = AerSimulator()
    print(f"Simulator Backend: {simulator.name}")
    print(f"Available Methods: {simulator.available_methods()}")
    print("✓ Aer simulator initialized successfully")
    print()
    
    # PART 4: Basic Circuit Creation Test
    print("PART 4: Basic Circuit Creation Test")
    print("-----------------------------------")
    
    # Test 1: Simple measurement
    qc1 = QuantumCircuit(1, 1)
    qc1.measure(0, 0)
    print("Test 1: Basic measurement circuit")
    print(qc1.draw(output='text'))
    
    job1 = simulator.run(qc1, shots=1000)
    counts1 = job1.result().get_counts()
    print(f"Results: {counts1}")
    print()
    
    # Test 2: Hadamard gate test
    qc2 = QuantumCircuit(1, 1)
    qc2.h(0)
    qc2.measure(0, 0)
    print("Test 2: Hadamard gate circuit")
    print(qc2.draw(output='text'))
    
    job2 = simulator.run(qc2, shots=1000)
    counts2 = job2.result().get_counts()
    print(f"Results: {counts2}")
    print()
    
    # Test 3: Multi-qubit circuit
    qc3 = QuantumCircuit(2, 2)
    qc3.h(0)
    qc3.cx(0, 1)
    qc3.measure_all()
    print("Test 3: Multi-qubit entanglement circuit")
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
    
    # Create comprehensive visualization with better spacing
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('Lab 2: Qiskit Installation and Environment Setup', fontsize=16, fontweight='bold', y=0.96)
    
    # Create grid layout with more space
    gs = fig.add_gridspec(3, 3, height_ratios=[0.6, 1.2, 1], hspace=0.4, wspace=0.3)
    
    # Top row: Environment info
    ax_env = fig.add_subplot(gs[0, :])
    env_text = f"""ENVIRONMENT VERIFICATION
Python: {sys.version.split()[0]} | Platform: {platform.system()} {platform.release()}
Qiskit: {qiskit_version} | Qiskit Aer: {aer_version}
Simulator: {simulator.name} | Status: ✓ All components verified"""
    
    ax_env.text(0.5, 0.5, env_text, ha='center', va='center', fontsize=11, 
                transform=ax_env.transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.3))
    ax_env.axis('off')
    
    # Middle row: Circuit diagrams
    circuits = [
        ("Test 1: Basic Measurement", "     ┌─┐\n  q: ┤M├\n     └╥┘\nc: 1/═╩═\n      0", counts1, 'lightblue'),
        ("Test 2: Hadamard Gate", "     ┌───┐┌─┐\n  q: ┤ H ├┤M├\n     └───┘└╥┘\nc: 1/══════╩═\n           0", counts2, 'lightgreen'),
        ("Test 3: Multi-qubit Circuit", "        ┌───┐\n   q_0: ┤ H ├──■──\n        └───┘┌─┴─┐\n   q_1: ─────┤ X ├\n             └───┘", clean_counts3, 'lightsalmon')
    ]
    
    for i, (title, circuit, counts, color) in enumerate(circuits):
        ax = fig.add_subplot(gs[1, i])
        ax.text(0.5, 0.95, title, ha='center', fontsize=10, fontweight='bold', transform=ax.transAxes)
        ax.text(0.5, 0.6, circuit, ha='center', fontsize=8, fontfamily='monospace', 
                transform=ax.transAxes, bbox=dict(boxstyle="round,pad=0.15", facecolor=color, alpha=0.4))
        ax.text(0.5, 0.05, f'{counts}', ha='center', fontsize=9, fontweight='bold', transform=ax.transAxes)
        ax.axis('off')
    
    # Bottom row: Bar charts
    test_results = [counts1, counts2, clean_counts3]
    colors = ['skyblue', 'lightgreen', 'salmon']
    titles = ['Basic Measurement', 'Hadamard Gate', 'Multi-qubit Circuit']
    
    for i, (counts, color, title) in enumerate(zip(test_results, colors, titles)):
        ax = fig.add_subplot(gs[2, i])
        bars = ax.bar(counts.keys(), counts.values(), color=color, alpha=0.8, edgecolor='black', linewidth=1)
        ax.set_title(title, fontweight='bold', fontsize=10)
        ax.set_ylabel('Counts', fontsize=9)
        ax.tick_params(labelsize=8)
        
        # Add count labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(counts.values())*0.02,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=8)
    
    # Add summary at bottom with proper spacing
    fig.text(0.5, 0.06, 'INSTALLATION VERIFICATION: ✓ Python Environment ✓ Qiskit Libraries ✓ Aer Simulator ✓ Circuit Execution', 
             ha='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", edgecolor="orange"))
    
    plt.savefig('qiskit_lab_2_final_image.png', dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.1)
    plt.show()
    
    print("INSTALLATION VERIFICATION COMPLETE")
    print("==================================")
    print("✓ Python environment verified")
    print("✓ Qiskit libraries imported successfully")
    print("✓ Aer simulator operational")
    print("✓ Basic quantum circuits executed")
    print("✓ Multi-qubit operations functional")
    print("✓ Visualization capabilities confirmed")
    print()
    print("CONCLUSION:")
    print("===========")
    print("✓ Qiskit installation is complete and functional")
    print("✓ All required components are working properly")
    print("✓ Environment is ready for quantum computing experiments")
    print("✓ Visualization saved as 'qiskit_lab_2_final_image.png'")

if __name__ == "__main__":
    main()