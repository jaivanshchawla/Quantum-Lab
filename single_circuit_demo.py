"""
Single Quantum Circuit Demo: The Bell State
A comprehensive explanation of quantum entanglement with one simple circuit
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import numpy as np

def create_bell_state_circuit():
    """
    Create the famous Bell State circuit - the simplest example of quantum entanglement
    
    This circuit creates the quantum state: |Φ+⟩ = (|00⟩ + |11⟩)/√2
    
    What this means:
    - 50% chance of measuring both qubits as 0
    - 50% chance of measuring both qubits as 1  
    - 0% chance of measuring different values (01 or 10)
    - The qubits are perfectly correlated!
    """
    
    # Create quantum and classical registers with descriptive names
    qreg = QuantumRegister(2, 'qubit')
    creg = ClassicalRegister(2, 'bit')
    
    # Create the quantum circuit
    circuit = QuantumCircuit(qreg, creg, name='Bell State')
    
    # Step 1: Start with both qubits in |0⟩ state
    circuit.barrier(label='|00⟩')
    
    # Step 2: Apply Hadamard gate to first qubit
    # This creates superposition: |0⟩ → (|0⟩ + |1⟩)/√2
    circuit.h(qreg[0])
    circuit.barrier(label='Superposition')
    
    # Step 3: Apply CNOT gate (Controlled-NOT)
    # This creates entanglement between the qubits
    circuit.cx(qreg[0], qreg[1])
    circuit.barrier(label='Entangled!')
    
    # Step 4: Measure both qubits
    circuit.measure(qreg, creg)
    
    return circuit

def explain_bell_state():
    """Provide a detailed explanation of the Bell state"""
    
    explanation = """
    
    ═══════════════════════════════════════════════════════════════
                        THE BELL STATE EXPLAINED
    ═══════════════════════════════════════════════════════════════
    
    🎯 WHAT IS A BELL STATE?
    The Bell state is the simplest example of quantum entanglement.
    It's a quantum state where two particles are perfectly correlated.
    
    📊 THE MATHEMATICS:
    |Φ+⟩ = (|00⟩ + |11⟩)/√2
    
    This means:
    • 1/√2 probability amplitude for |00⟩ (both qubits = 0)
    • 1/√2 probability amplitude for |11⟩ (both qubits = 1)
    • 0 probability amplitude for |01⟩ or |10⟩ (mixed states)
    
    🔬 STEP-BY-STEP PROCESS:
    
    1. INITIALIZATION: |00⟩
       Both qubits start in the |0⟩ state
    
    2. SUPERPOSITION: H|0⟩ = (|0⟩ + |1⟩)/√2
       Hadamard gate puts first qubit in superposition
       State becomes: (|00⟩ + |10⟩)/√2
    
    3. ENTANGLEMENT: CNOT creates correlation
       If first qubit is |0⟩, second stays |0⟩
       If first qubit is |1⟩, second flips to |1⟩
       Final state: (|00⟩ + |11⟩)/√2
    
    4. MEASUREMENT: Collapse to classical state
       50% chance: measure |00⟩
       50% chance: measure |11⟩
       0% chance: measure |01⟩ or |10⟩
    
    🌟 WHY IS THIS AMAZING?
    • The qubits are perfectly correlated even when separated!
    • Measuring one qubit instantly determines the other
    • This violates classical physics (Einstein called it "spooky action")
    • It's the foundation for quantum computing and quantum cryptography
    
    ═══════════════════════════════════════════════════════════════
    """
    
    return explanation

def simulate_and_visualize():
    """Create comprehensive visualization of the Bell state circuit"""
    
    # Create the circuit
    circuit = create_bell_state_circuit()
    
    # Set up the visualization with cleaner layout
    plt.style.use('default')  # Use white background for better visibility
    fig = plt.figure(figsize=(18, 10))
    fig.suptitle('Bell State Circuit: Quantum Entanglement Explained', 
                 fontsize=22, color='darkblue', fontweight='bold', y=0.95)
    
    # Circuit diagram - larger and centered
    ax1 = plt.subplot(2, 4, (1, 2))
    try:
        circuit.draw(output='mpl', ax=ax1, style='iqp')
        ax1.set_title('Circuit Diagram', fontsize=16, color='darkgreen', pad=25)
    except:
        # Fallback to text representation
        ax1.text(0.1, 0.5, str(circuit), fontsize=14, color='black', 
                family='monospace', transform=ax1.transAxes)
        ax1.set_title('Bell State Circuit', fontsize=16, color='darkgreen')
        ax1.axis('off')
    
    # Simulate the circuit
    simulator = AerSimulator()
    job = simulator.run(circuit, shots=1000)
    result = job.result()
    counts = result.get_counts()
    
    # Results histogram - larger
    ax2 = plt.subplot(2, 4, (3, 4))
    plot_histogram(counts, ax=ax2, color=['#FF6B6B', '#4ECDC4'], 
                   title='Measurement Results (1000 shots)')
    ax2.set_title('Measurement Results (1000 shots)', fontsize=16, color='darkgreen', pad=25)
    
    # Mathematical explanation - cleaner formatting
    ax3 = plt.subplot(2, 4, 5)
    math_text = """Mathematical Description:

Initial State:
|ψ₀⟩ = |00⟩

After Hadamard:
|ψ₁⟩ = (|00⟩ + |10⟩)/√2

After CNOT:
|ψ₂⟩ = (|00⟩ + |11⟩)/√2

This is the Bell State!
Perfect entanglement achieved.
    """
    ax3.text(0.05, 0.95, math_text, fontsize=12, color='darkblue', 
             transform=ax3.transAxes, verticalalignment='top', family='monospace')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis('off')
    ax3.set_title('Mathematical Steps', fontsize=14, color='darkblue', pad=20)
    
    # Step-by-step process - cleaner
    ax4 = plt.subplot(2, 4, 6)
    steps_text = """Physical Process:

1. INITIALIZATION
   Both qubits = |0⟩

2. HADAMARD GATE
   Qubit 0 → superposition
   
3. CNOT GATE
   Creates entanglement
   
4. MEASUREMENT
   Random collapse to
   |00⟩ or |11⟩ only

Result: Perfect correlation!
    """
    ax4.text(0.05, 0.95, steps_text, fontsize=12, color='darkgreen', 
             transform=ax4.transAxes, verticalalignment='top', family='monospace')
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.axis('off')
    ax4.set_title('Physical Steps', fontsize=14, color='darkgreen', pad=20)
    
    # Key insights - organized
    ax5 = plt.subplot(2, 4, 7)
    insights_text = """Key Insights:

✓ Superposition:
  Qubit exists in multiple
  states simultaneously
  
✓ Entanglement:
  Qubits become correlated
  across any distance
  
✓ Measurement:
  Collapses superposition
  to definite state
  
✓ Correlation:
  Measuring one determines
  the other instantly
    """
    ax5.text(0.05, 0.95, insights_text, fontsize=11, color='darkorange', 
             transform=ax5.transAxes, verticalalignment='top', family='monospace')
    ax5.set_xlim(0, 1)
    ax5.set_ylim(0, 1)
    ax5.axis('off')
    ax5.set_title('Quantum Phenomena', fontsize=14, color='darkorange', pad=20)
    
    # Applications - organized
    ax6 = plt.subplot(2, 4, 8)
    apps_text = """Applications:

🔐 Cryptography:
  Quantum key distribution
  Unbreakable encryption
  
🔬 Computing:
  Quantum algorithms
  Parallel processing
  
📡 Communication:
  Quantum teleportation
  Secure networks
  
🎯 Sensing:
  Ultra-precise measurements
  Quantum metrology
    """
    ax6.text(0.05, 0.95, apps_text, fontsize=11, color='purple', 
             transform=ax6.transAxes, verticalalignment='top', family='monospace')
    ax6.set_xlim(0, 1)
    ax6.set_ylim(0, 1)
    ax6.axis('off')
    ax6.set_title('Real-World Uses', fontsize=14, color='purple', pad=20)
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.90)
    plt.savefig('bell_state_explained.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.90)
    plt.savefig('bell_state_explained.png', dpi=300, bbox_inches='tight', 
                facecolor='black', edgecolor='none')
    plt.show()
    
    return counts

def main():
    """Main function to run the Bell state demonstration"""
    
    print("=" * 80)
    print("           🌟 QUANTUM ENTANGLEMENT: THE BELL STATE CIRCUIT 🌟")
    print("=" * 80)
    print("\n📖 WHAT YOU'RE ABOUT TO SEE:")
    print("   • A simple 2-qubit quantum circuit that creates entanglement")
    print("   • Text-based circuit diagram showing quantum gates")
    print("   • Simulation results proving quantum correlation")
    print("   • Visual explanation saved as an image file")
    
    # Create and display the circuit
    circuit = create_bell_state_circuit()
    
    print(f"\n🎨 CIRCUIT DIAGRAM (Text Format):")
    print("   This shows the quantum gates applied to our qubits:")
    print(circuit)
    
    print(f"\n📊 CIRCUIT TECHNICAL DETAILS:")
    print(f"   • Total Qubits: {circuit.num_qubits} (quantum bits that can be 0, 1, or both)")
    print(f"   • Classical Bits: {circuit.num_clbits} (normal bits to store measurement results)")
    print(f"   • Quantum Gates: {len(circuit.data)} (operations that manipulate qubits)")
    print(f"   • Circuit Depth: {circuit.depth()} (number of sequential gate operations)")
    
    # Show the explanation
    print(explain_bell_state())
    
    # Simulate and show results
    print("🔬 RUNNING QUANTUM SIMULATION...")
    print("   • Executing the circuit 1000 times")
    print("   • Each execution measures both qubits")
    print("   • Results will show quantum entanglement in action")
    print("   • Opening visual explanation window...")
    
    counts = simulate_and_visualize()
    
    print(f"\n📈 SIMULATION RESULTS EXPLAINED:")
    print("   These numbers show how many times each state was measured:")
    
    total_shots = sum(counts.values())
    for state, count in sorted(counts.items()):
        percentage = (count / total_shots) * 100
        if state == '00':
            print(f"   |{state}⟩: {count:4d} shots ({percentage:.1f}%) ← Both qubits measured as 0")
        elif state == '11':
            print(f"   |{state}⟩: {count:4d} shots ({percentage:.1f}%) ← Both qubits measured as 1")
        elif state in ['01', '10']:
            print(f"   |{state}⟩: {count:4d} shots ({percentage:.1f}%) ← Mixed state (shouldn't happen!)")
    
    print(f"\n✨ WHAT THE RESULTS MEAN:")
    if '01' in counts or '10' in counts:
        print("   ⚠️  UNEXPECTED: Mixed states detected!")
        print("       This suggests the entanglement didn't work properly.")
    else:
        print("   ✅ PERFECT ENTANGLEMENT CONFIRMED!")
        print("       • Only |00⟩ and |11⟩ states were measured")
        print("       • No mixed states (|01⟩ or |10⟩) appeared")
        print("       • The qubits are perfectly correlated")
        print("       • This proves quantum entanglement is working!")
    
    print(f"\n🎯 KEY TAKEAWAY:")
    print("   This simple 2-gate circuit demonstrates quantum entanglement -")
    print("   one of the most profound phenomena in quantum mechanics!")
    print("   The qubits 'know' about each other instantly, no matter the distance!")
    
    print(f"\n💾 VISUAL FILES CREATED:")
    print("   📊 'bell_state_explained.png' - Comprehensive visual explanation")
    print("      (Check your file explorer - a detailed diagram was saved)")
    
    print(f"\n🔍 UNDERSTANDING THE VISUAL OUTPUT:")
    print("   The popup window shows:")
    print("   • Circuit Diagram: Visual representation of quantum gates")
    print("   • Measurement Results: Bar chart of the simulation outcomes")
    print("   • Mathematical Steps: The quantum state at each stage")
    print("   • Physical Process: What happens to the qubits")
    print("   • Key Insights: Why this matters for quantum physics")
    print("   • Applications: How this is used in real quantum technology")
    
    print("=" * 80)

if __name__ == "__main__":
    main()