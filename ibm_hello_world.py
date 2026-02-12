"""
IBM Qiskit Hello World Program
The classic introduction to quantum computing with Qiskit
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def hello_world_quantum():
    """
    IBM's Hello World for Quantum Computing
    Creates a simple quantum circuit with superposition and measurement
    """
    
    print("=" * 60)
    print("🌟 IBM QISKIT HELLO WORLD PROGRAM 🌟")
    print("=" * 60)
    print("Welcome to quantum computing with Qiskit!")
    print("This is your first quantum circuit.\n")
    
    # Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    
    # Add a Hadamard gate to create superposition
    qc.h(0)
    
    # Measure the qubit
    qc.measure(0, 0)
    
    print("🎨 QUANTUM CIRCUIT:")
    print("This circuit puts a qubit in superposition and measures it")
    print(qc)
    
    print(f"\n📊 CIRCUIT DETAILS:")
    print(f"   • Qubits: {qc.num_qubits}")
    print(f"   • Classical bits: {qc.num_clbits}")
    print(f"   • Gates: {len(qc.data)}")
    print(f"   • Depth: {qc.depth()}")
    
    # Simulate the circuit
    print(f"\n🔬 RUNNING SIMULATION...")
    print("Executing the quantum circuit 1000 times...")
    
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    
    print(f"\n📈 RESULTS:")
    print("Each measurement collapses the superposition randomly:")
    
    for outcome, count in counts.items():
        percentage = (count / 1000) * 100
        print(f"   |{outcome}⟩: {count:4d} times ({percentage:5.1f}%)")
    
    # Expected: roughly 50% |0⟩ and 50% |1⟩
    if '0' in counts and '1' in counts:
        diff = abs(counts.get('0', 0) - counts.get('1', 0))
        if diff < 100:  # Within reasonable statistical variation
            print(f"\n✅ SUCCESS! Results show quantum superposition:")
            print(f"   • Roughly equal |0⟩ and |1⟩ outcomes")
            print(f"   • This proves the qubit was in superposition!")
        else:
            print(f"\n⚠️  Unusual results - large deviation from 50/50")
    
    return qc, counts

def hello_world_with_visualization():
    """
    Enhanced Hello World with visualization
    """
    print(f"\n" + "=" * 60)
    print("🎨 ENHANCED HELLO WORLD WITH VISUALIZATION")
    print("=" * 60)
    
    # Create the circuit
    qc, counts = hello_world_quantum()
    
    # Create visualization
    print(f"\n📊 Creating visualization...")
    
    try:
        # Use default (white) background for better visibility
        plt.style.use('default')
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle('IBM Qiskit Hello World Results', fontsize=16, color='darkblue', fontweight='bold')
        
        # Circuit diagram with better visibility
        try:
            qc.draw(output='mpl', ax=ax1, style='iqp')
            ax1.set_title('Quantum Circuit', color='darkgreen', fontsize=14, fontweight='bold')
            ax1.grid(True, alpha=0.3)
        except:
            ax1.text(0.5, 0.5, str(qc), ha='center', va='center', 
                    fontsize=12, color='black', family='monospace')
            ax1.set_title('Quantum Circuit', color='darkgreen', fontsize=14, fontweight='bold')
            ax1.axis('off')
        
        # Results histogram with better colors
        plot_histogram(counts, ax=ax2, color=['#FF6B6B', '#4ECDC4'], 
                       title='Measurement Results')
        ax2.set_title('Measurement Results', color='darkgreen', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('hello_world_quantum.png', dpi=300, bbox_inches='tight', 
                    facecolor='white', edgecolor='none')
        plt.show()
        
        print(f"💾 Visualization saved as 'hello_world_quantum.png'")
        
    except Exception as e:
        print(f"⚠️  Visualization error: {e}")
        print("But the quantum simulation worked perfectly!")

def explain_hello_world():
    """
    Explain what the Hello World program demonstrates
    """
    print(f"\n" + "=" * 60)
    print("📚 WHAT THIS PROGRAM DEMONSTRATES")
    print("=" * 60)
    
    explanation = """
🎯 QUANTUM CONCEPTS SHOWN:

1. QUANTUM SUPERPOSITION
   • The Hadamard gate puts the qubit in superposition
   • Before measurement: qubit is both |0⟩ AND |1⟩ simultaneously
   • This is impossible in classical physics!

2. QUANTUM MEASUREMENT
   • Measurement collapses the superposition
   • Each measurement randomly gives |0⟩ or |1⟩
   • Over many measurements: ~50% each outcome

3. QUANTUM RANDOMNESS
   • True randomness from quantum mechanics
   • Not pseudo-random like classical computers
   • Each run gives slightly different results

🔬 THE PHYSICS:
   • Initial state: |0⟩
   • After Hadamard: (|0⟩ + |1⟩)/√2
   • Measurement probability: 50% for each outcome

🌟 WHY THIS MATTERS:
   • Foundation of quantum computing
   • Shows quantum vs classical behavior
   • Building block for quantum algorithms
   • Demonstrates quantum advantage potential

💡 NEXT STEPS:
   • Try multiple qubits
   • Add entanglement (CNOT gates)
   • Explore quantum algorithms
   • Build more complex circuits
    """
    
    print(explanation)

def compare_classical_vs_quantum():
    """
    Compare classical and quantum "Hello World" programs
    """
    print(f"\n" + "=" * 60)
    print("⚖️  CLASSICAL vs QUANTUM COMPARISON")
    print("=" * 60)
    
    print("🖥️  CLASSICAL HELLO WORLD:")
    print('   print("Hello, World!")')
    print("   • Deterministic output")
    print("   • Same result every time")
    print("   • No randomness involved")
    
    print(f"\n🌌 QUANTUM HELLO WORLD:")
    print("   circuit.h(0)  # Superposition")
    print("   circuit.measure(0, 0)  # Random collapse")
    print("   • Probabilistic output")
    print("   • Different results each run")
    print("   • True quantum randomness")
    
    print(f"\n🎯 KEY DIFFERENCE:")
    print("   Classical: Predictable, deterministic")
    print("   Quantum: Probabilistic, fundamentally random")
    print("   This randomness enables quantum algorithms!")

def main():
    """
    Main function to run IBM's Hello World program
    """
    
    # Run the basic Hello World
    qc, counts = hello_world_quantum()
    
    # Enhanced version with visualization
    hello_world_with_visualization()
    
    # Explain the concepts
    explain_hello_world()
    
    # Compare with classical
    compare_classical_vs_quantum()
    
    print(f"\n" + "=" * 60)
    print("🎉 CONGRATULATIONS!")
    print("=" * 60)
    print("You've successfully run your first quantum program!")
    print("You've witnessed quantum superposition in action!")
    print("Welcome to the quantum computing world! 🚀")
    print("=" * 60)

if __name__ == "__main__":
    main()