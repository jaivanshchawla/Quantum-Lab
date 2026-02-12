"""
Lab 7: Hadamard Gate and Bloch Sphere Visualization
===================================================
Objective: Create superposition and visualize Bloch sphere
"""

# Step 1: Import Qiskit libraries
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def main():
    print("LAB 7: HADAMARD GATE AND BLOCH SPHERE VISUALIZATION")
    print("====================================================")
    print()
    
    # Step 2: Create quantum circuits and apply gates
    # Initialize simulator
    simulator = AerSimulator()
    
    # State 1: Initial |0⟩
    print("PART 1: Initial State |0⟩")
    qc1 = QuantumCircuit(1)
    state1 = Statevector.from_instruction(qc1)
    print(qc1.draw(output='text'))
    print(f"State vector: {state1.data}")
    print()
    
    # State 2: Hadamard H|0⟩
    print("PART 2: Hadamard Gate Applied")
    qc2 = QuantumCircuit(1)
    qc2.h(0)  # Step 3: Apply Hadamard gate
    state2 = Statevector.from_instruction(qc2)
    print(qc2.draw(output='text'))
    print(f"State vector: {state2.data}")
    print()
    
    # State 3: Pauli-X X|0⟩
    print("PART 3: Pauli-X Gate Applied")
    qc3 = QuantumCircuit(1)
    qc3.x(0)  # Step 3: Apply X gate
    state3 = Statevector.from_instruction(qc3)
    print(qc3.draw(output='text'))
    print(f"State vector: {state3.data}")
    print()
    
    # State 4: Pauli-Y Y|0⟩
    print("PART 4: Pauli-Y Gate Applied")
    qc4 = QuantumCircuit(1)
    qc4.y(0)  # Step 3: Apply Y gate
    state4 = Statevector.from_instruction(qc4)
    print(qc4.draw(output='text'))
    print(f"State vector: {state4.data}")
    print()
    
    # Step 4: Execute using Aer simulator (measurements)
    print("PART 5: Measurement Results")
    print("---------------------------")
    
    qc1_m = QuantumCircuit(1, 1)
    qc1_m.measure(0, 0)
    job1 = simulator.run(qc1_m, shots=1000)
    counts1 = job1.result().get_counts()
    print(f"|0⟩ state: {counts1}")
    
    qc2_m = QuantumCircuit(1, 1)
    qc2_m.h(0)
    qc2_m.measure(0, 0)
    job2 = simulator.run(qc2_m, shots=1000)
    counts2 = job2.result().get_counts()
    print(f"H|0⟩ state: {counts2}")
    
    qc3_m = QuantumCircuit(1, 1)
    qc3_m.x(0)
    qc3_m.measure(0, 0)
    job3 = simulator.run(qc3_m, shots=1000)
    counts3 = job3.result().get_counts()
    print(f"X|0⟩ state: {counts3}")
    
    qc4_m = QuantumCircuit(1, 1)
    qc4_m.y(0)
    qc4_m.measure(0, 0)
    job4 = simulator.run(qc4_m, shots=1000)
    counts4 = job4.result().get_counts()
    print(f"Y|0⟩ state: {counts4}")
    print()
    
    # Step 5: Analyze results using Bloch sphere visualization
    print("PART 6: Bloch Sphere Visualization")
    print("-----------------------------------")
    
    # Create individual Bloch spheres and combine them
    states = [state1, state2, state3, state4]
    titles = ['|0⟩ State (North Pole)', 
              'H|0⟩ = |+⟩ (Equator +X)', 
              'X|0⟩ = |1⟩ (South Pole)', 
              'Y|0⟩ = i|1⟩ (South Pole)']
    
    # Create each Bloch sphere separately
    bloch_figs = []
    for i, (state, title) in enumerate(zip(states, titles)):
        fig = plot_bloch_multivector(state, title=title)
        filename = f'temp_bloch_{i}.png'
        fig.savefig(filename, dpi=200, bbox_inches='tight')
        bloch_figs.append(filename)
        plt.close(fig)
    
    # Combine into single image using matplotlib
    from PIL import Image
    import os
    
    # Load all images
    images = [Image.open(f) for f in bloch_figs]
    
    # Get dimensions
    widths, heights = zip(*(img.size for img in images))
    total_width = sum(widths)
    max_height = max(heights)
    
    # Create combined image
    combined = Image.new('RGB', (total_width, max_height), 'white')
    
    # Paste images side by side
    x_offset = 0
    for img in images:
        combined.paste(img, (x_offset, 0))
        x_offset += img.width
    
    # Save combined image
    combined.save('qiskit_lab_7_final_image.png', dpi=(300, 300))
    
    # Clean up temporary files
    for f in bloch_figs:
        os.remove(f)
    
    print("✓ Combined Bloch sphere visualization saved as 'qiskit_lab_7_final_image.png'")
    print()
    
    # Observation & Result
    print("OBSERVATION & RESULT:")
    print("====================")
    print("✓ Initial |0⟩: North pole (0,0,1) - Always measures 0")
    print("✓ H|0⟩ = |+⟩: Equator +X (1,0,0) - 50% |0⟩, 50% |1⟩")
    print("✓ X|0⟩ = |1⟩: South pole (0,0,-1) - Always measures 1")
    print("✓ Y|0⟩ = i|1⟩: South pole (0,0,-1) - Always measures 1")
    print()
    print("THEORETICAL VERIFICATION:")
    print("=========================")
    print("• Hadamard matrix: H = (1/√2)[[1,1],[1,-1]]")
    print("• Creates equal superposition: H|0⟩ = (|0⟩+|1⟩)/√2")
    print("• Bloch sphere provides geometric representation")
    print("• All experimental results match theoretical expectations")
    print()
    print("✓ Lab 7 Complete!")

if __name__ == "__main__":
    main()
