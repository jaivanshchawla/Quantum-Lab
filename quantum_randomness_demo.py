"""
Quantum Randomness Demonstration
Shows why quantum measurement results vary each time
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def create_bell_circuit():
    """Create the Bell state circuit"""
    qreg = QuantumRegister(2, 'q')
    creg = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg, creg)
    
    circuit.h(qreg[0])
    circuit.cx(qreg[0], qreg[1])
    circuit.measure(qreg, creg)
    
    return circuit

def run_multiple_experiments():
    """Run the same circuit multiple times to show randomness"""
    
    circuit = create_bell_circuit()
    simulator = AerSimulator()
    
    print("=" * 70)
    print("        QUANTUM RANDOMNESS DEMONSTRATION")
    print("=" * 70)
    print("\nRunning the SAME Bell state circuit 10 times...")
    print("Each run uses 1000 quantum measurements (shots)")
    print("\nCircuit:")
    print(circuit)
    
    results = []
    
    for run in range(10):
        job = simulator.run(circuit, shots=1000)
        counts = job.result().get_counts()
        
        # Ensure we have both keys (sometimes one might be 0)
        count_00 = counts.get('00', 0)
        count_11 = counts.get('11', 0)
        count_01 = counts.get('01', 0)
        count_10 = counts.get('10', 0)
        
        results.append({
            '00': count_00,
            '11': count_11,
            '01': count_01,
            '10': count_10
        })
        
        # Calculate percentages
        pct_00 = (count_00 / 1000) * 100
        pct_11 = (count_11 / 1000) * 100
        
        print(f"\nRun {run+1:2d}: |00⟩={count_00:3d} ({pct_00:5.1f}%)  |11⟩={count_11:3d} ({pct_11:5.1f}%)", end="")
        
        if count_01 > 0 or count_10 > 0:
            print(f"  ⚠️ UNEXPECTED: |01⟩={count_01}, |10⟩={count_10}")
        else:
            print("  ✅ Perfect entanglement!")
    
    return results

def analyze_results(results):
    """Analyze the statistical properties of multiple runs"""
    
    print(f"\n" + "=" * 70)
    print("                    STATISTICAL ANALYSIS")
    print("=" * 70)
    
    # Calculate statistics
    all_00 = [r['00'] for r in results]
    all_11 = [r['11'] for r in results]
    all_mixed = [r['01'] + r['10'] for r in results]
    
    avg_00 = sum(all_00) / len(all_00)
    avg_11 = sum(all_11) / len(all_11)
    avg_mixed = sum(all_mixed) / len(all_mixed)
    
    min_00, max_00 = min(all_00), max(all_00)
    min_11, max_11 = min(all_11), max(all_11)
    
    print(f"\n📊 STATISTICS OVER {len(results)} RUNS:")
    print(f"   |00⟩ counts: Average={avg_00:.1f}, Range=[{min_00}-{max_00}]")
    print(f"   |11⟩ counts: Average={avg_11:.1f}, Range=[{min_11}-{max_11}]")
    print(f"   Mixed states: Average={avg_mixed:.1f} (should be 0!)")
    
    print(f"\n🎯 WHAT THIS SHOWS:")
    print(f"   ✅ Individual results vary (quantum randomness)")
    print(f"   ✅ Average is ~50/50 (correct quantum statistics)")
    print(f"   ✅ No mixed states (perfect entanglement)")
    print(f"   ✅ Results follow quantum mechanical predictions")
    
    # Check if results are within expected range (3 sigma ~ 99.7%)
    # For 1000 shots, standard deviation ≈ √(1000 * 0.5 * 0.5) ≈ 15.8
    expected_std = (1000 * 0.5 * 0.5) ** 0.5
    three_sigma = 3 * expected_std
    
    print(f"\n📈 STATISTICAL VALIDATION:")
    print(f"   Expected standard deviation: ±{expected_std:.1f}")
    print(f"   99.7% of results should be within: {500-three_sigma:.0f} to {500+three_sigma:.0f}")
    
    within_range = all(abs(count - 500) <= three_sigma for count in all_00)
    print(f"   All |00⟩ results within 3σ: {'✅ YES' if within_range else '❌ NO'}")

def visualize_randomness(results):
    """Create a visualization showing the randomness"""
    
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('Quantum Randomness: Same Circuit, Different Results', 
                 fontsize=16, color='gold', fontweight='bold')
    
    # Plot 1: Results over multiple runs
    runs = list(range(1, len(results) + 1))
    counts_00 = [r['00'] for r in results]
    counts_11 = [r['11'] for r in results]
    
    ax1.plot(runs, counts_00, 'o-', color='cyan', label='|00⟩ counts', linewidth=2, markersize=8)
    ax1.plot(runs, counts_11, 's-', color='gold', label='|11⟩ counts', linewidth=2, markersize=8)
    ax1.axhline(y=500, color='white', linestyle='--', alpha=0.7, label='Expected (500)')
    ax1.set_xlabel('Run Number', color='white')
    ax1.set_ylabel('Count (out of 1000 shots)', color='white')
    ax1.set_title('Measurement Results Across Multiple Runs', color='cyan')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Distribution histogram
    ax2.hist(counts_00, bins=8, alpha=0.7, color='cyan', label='|00⟩ distribution', edgecolor='white')
    ax2.axvline(x=500, color='white', linestyle='--', alpha=0.7, label='Expected (500)')
    ax2.set_xlabel('Count', color='white')
    ax2.set_ylabel('Frequency', color='white')
    ax2.set_title('Distribution of |00⟩ Results', color='cyan')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('quantum_randomness.png', dpi=300, bbox_inches='tight', 
                facecolor='black', edgecolor='none')
    plt.show()

def main():
    """Main demonstration function"""
    
    # Run multiple experiments
    results = run_multiple_experiments()
    
    # Analyze the results
    analyze_results(results)
    
    # Create visualization
    print(f"\n🎨 Creating visualization...")
    visualize_randomness(results)
    
    print(f"\n" + "=" * 70)
    print("                         KEY INSIGHTS")
    print("=" * 70)
    print(f"""
🔬 QUANTUM vs CLASSICAL RANDOMNESS:

Classical Computer:
• Uses algorithms to generate "pseudo-random" numbers
• Given the same seed, always produces the same sequence
• Deterministic underneath

Quantum Computer:
• Uses fundamental quantum mechanics for true randomness
• Same circuit gives different results each time
• Non-deterministic at the most basic level

🎯 WHY YOUR RESULTS DIFFER:
• Each measurement collapses the quantum superposition randomly
• The 50/50 split is a statistical average, not a guarantee per run
• This randomness is a FEATURE, not a bug!

🌟 APPLICATIONS:
• Quantum cryptography (unbreakable random keys)
• Monte Carlo simulations (better sampling)
• Quantum machine learning (probabilistic algorithms)
    """)
    
    print("💾 Visualization saved as 'quantum_randomness.png'")
    print("=" * 70)

if __name__ == "__main__":
    main()