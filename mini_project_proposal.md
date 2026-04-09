# Quantum Computing Labs — Complete Reference & Mini Project Proposal

## Table of Contents
1. [Lab-by-Lab Deep Dive](#lab-by-lab-deep-dive)
2. [Concept Progression Map](#concept-progression-map)
3. [Shared Infrastructure](#shared-infrastructure)
4. [Mini Project Proposals](#mini-project-proposals)

---

# Lab-by-Lab Deep Dive

## Lab 1 — Introduction to Quantum Computing and Qiskit

**File:** `lab_1.py`
**Objective:** Introduce the three foundational quantum phenomena: qubit states, superposition, and entanglement.

### Parts Covered

**Part 1 — Basic Qubit |0⟩**
- Circuit: 1 qubit, 1 classical bit, no gates, just measurement
- Expected result: 100% |0⟩ (deterministic ground state)
- Actual result: `{'0': 1000}` (1000 shots, always 0)
- Concept: A qubit starts in the ground state |0⟩ by default. Without any gate, measurement always collapses to 0.

**Part 2 — Superposition via Hadamard**
- Circuit: H gate on qubit 0, then measure
- Gate: `qc.h(0)` — Hadamard gate
- State created: |+⟩ = (|0⟩ + |1⟩)/√2
- Expected result: ~50% |0⟩, ~50% |1⟩
- Actual result: approximately `{'0': 503, '1': 497}` (varies per run)
- Concept: The Hadamard gate puts the qubit into equal superposition. Measurement randomly collapses it.

**Part 3 — Entanglement via Bell State**
- Circuit: 2 qubits, H on qubit 0, CNOT(control=0, target=1), measure_all
- Gates: `qc.h(0)`, `qc.cx(0, 1)`
- State created: |Φ+⟩ = (|00⟩ + |11⟩)/√2
- Expected result: ~50% |00⟩, ~50% |11⟩, never |01⟩ or |10⟩
- Actual result: approximately `{'00': 498, '11': 502}`
- Concept: CNOT entangles the two qubits. Once entangled, measuring one instantly determines the other.

### Visualization
- 3-panel matplotlib figure (15×5 inches)
- Panel 1: Bar chart for basic qubit (single blue bar at |0⟩)
- Panel 2: Bar chart for superposition (two green bars ~equal height)
- Panel 3: Bar chart for Bell state (two red bars at |00⟩ and |11⟩ only)
- Output file: `lab1_results.png`

### Key Takeaways
- Qiskit circuit creation: `QuantumCircuit(n_qubits, n_classical_bits)`
- Running on simulator: `AerSimulator().run(circuit, shots=1000)`
- Getting results: `job.result().get_counts()`
- The CNOT gate is the key to creating entanglement


---

## Lab 2 — Qiskit Installation and Environment Setup

**File:** `lab_2.py`
**Objective:** Verify the Qiskit installation, confirm all components work, and run basic test circuits.

### Parts Covered

**Part 1 — Environment Verification**
- Prints Python version, platform (OS), Qiskit version, Qiskit Aer version
- Uses `sys.version`, `platform.system()`, `qiskit.__version__`, `aer.__version__`
- Confirms the development environment is correctly configured

**Part 2 — Import Test**
- Imports: `QuantumCircuit`, `QuantumRegister`, `ClassicalRegister`, `AerSimulator`, `plot_histogram`
- Catches `ImportError` and reports if any module is missing
- Confirms all required Qiskit modules are accessible

**Part 3 — Simulator Verification**
- Instantiates `AerSimulator()`
- Prints `simulator.name` and `simulator.available_methods()`
- Confirms the Aer backend is operational

**Part 4 — Basic Circuit Tests**
- Test 1: Single qubit measurement — `{'0': 1000}` (deterministic)
- Test 2: Hadamard gate — `{'0': ~500, '1': ~500}` (superposition)
- Test 3: Multi-qubit Bell state — `{'00': ~500, '11': ~500}` (entanglement)
- Each test verifies a different layer of Qiskit functionality

### Visualization
- 3-row matplotlib grid (16×12 inches) using `fig.add_gridspec(3, 3)`
- Row 1: Environment info text box (green background)
- Row 2: Circuit diagram text boxes for each test (colored backgrounds)
- Row 3: Bar charts for each test result
- Footer: Installation verification summary banner
- Output file: `qiskit_lab_2_final_image.png`

### Key Takeaways
- How to check Qiskit version programmatically
- `AerSimulator.available_methods()` lists statevector, density_matrix, etc.
- Result key cleanup: `key.split()[0]` strips register labels from multi-register measurements
- `gridspec` with `height_ratios` for non-uniform subplot sizing


---

## Lab 3 — Quantum Bits (Qubits) and Quantum Registers

**File:** `lab_3.py`
**Objective:** Understand how quantum registers and classical registers are created and used together.

### Theory
- A **QuantumRegister** holds qubits in a tensor product space: |q₁⟩ ⊗ |q₀⟩
- A **ClassicalRegister** stores measurement outcomes as classical bits
- `QuantumCircuit(qr, cr)` combines both into a circuit

### Parts Covered

**Part 1 — Register Creation**
- `qr = QuantumRegister(2)` — creates 2-qubit register
- `cr = ClassicalRegister(2)` — creates 2-bit classical register
- `qc = QuantumCircuit(qr, cr)` — empty circuit, no gates
- Demonstrates the structure before any operations

**Part 2 — Single Qubit Operations**
- Test 1: Measure only qubit 0 → `{'00': 1000}` (qubit 1 stays |0⟩)
- Test 2: H on qubit 0, measure qubit 0 → `{'00': ~500, '10': ~500}` (qubit 1 still |0⟩)
- Shows that operations on one qubit don't affect others unless entangled

**Part 3 — Multi-Qubit Register Operations**
- Test 3: H on both qubits → all 4 states equally likely (~25% each)
  - State: |ψ⟩ = (|00⟩ + |01⟩ + |10⟩ + |11⟩)/2
- Test 4: H on qubit 0 + CNOT → Bell state |Φ+⟩
  - Only |00⟩ and |11⟩ appear (~50% each)

### Visualization
- 3-row matplotlib grid (16×14 inches) using `fig.add_gridspec(3, 4)`
- Row 1: Register explanation text box
- Row 2: 4 circuit diagram text boxes
- Row 3: 4 bar charts (one per test)
- Footer: Register operations summary
- Output file: `qiskit_lab_3_final_image.png`

### Key Takeaways
- `QuantumRegister` and `ClassicalRegister` give named access to qubits/bits
- `qc.measure(qubit_index, classical_index)` maps specific qubits to bits
- `qc.measure_all()` adds a barrier and measures all qubits
- Tensor product ordering: rightmost qubit is qubit 0 in Qiskit's convention


---

## Lab 4 — Creating a Simple Quantum Circuit

**File:** `lab_4.py`
**Objective:** Design and simulate basic single-qubit circuits using X, Y, Z, and composite gates.

### Theory — Pauli Gate Matrices
```
X = [[0, 1],    Y = [[0, -i],   Z = [[1,  0],
     [1, 0]]         [i,  0]]        [0, -1]]
```
All three are unitary (U†U = I) and Hermitian (U† = U).

### Parts Covered

**Part 1 — X Gate (NOT gate)**
- Circuit: X gate on qubit 0, then measure
- Effect: |0⟩ → |1⟩ (bit flip)
- Result: `{'1': 1000}` — always measures 1
- Matrix action: X|0⟩ = [0,1;1,0][1,0]ᵀ = [0,1]ᵀ = |1⟩

**Part 2 — Y Gate**
- Circuit: Y gate on qubit 0, then measure
- Effect: |0⟩ → i|1⟩ (bit flip + phase i)
- Result: `{'1': 1000}` — always measures 1 (phase is not observable)
- Matrix action: Y|0⟩ = [0,-i;i,0][1,0]ᵀ = [0,i]ᵀ → |1⟩ with phase i

**Part 3 — Z Gate**
- Circuit: Z gate on qubit 0, then measure
- Effect: |0⟩ → |0⟩ (phase flip only, |0⟩ unchanged)
- Result: `{'0': 1000}` — always measures 0
- Matrix action: Z|0⟩ = [1,0;0,-1][1,0]ᵀ = [1,0]ᵀ = |0⟩
- Note: Z only affects |1⟩ → -|1⟩, invisible when starting from |0⟩

**Part 4 — Composite H + X**
- Circuit: H gate then X gate
- Effect: H|0⟩ = |+⟩, then X|+⟩ = X(|0⟩+|1⟩)/√2 = (|1⟩+|0⟩)/√2 = |+⟩
- Result: ~50% |0⟩, ~50% |1⟩ (still superposition)
- Demonstrates gate composition and that X preserves the |+⟩ state

### Visualization
- 2×4 matplotlib subplot grid (14×8 inches)
- Row 1: Circuit diagram text boxes for each gate
- Row 2: Bar charts for each measurement result
- Footer: Gate summary and unitary operations banner
- Output file: `qiskit_lab_4_final_image.png`

### Key Takeaways
- `qc.x(0)`, `qc.y(0)`, `qc.z(0)` apply Pauli gates
- Phase differences (Y vs X) are invisible in measurement statistics
- Gate order matters: H then X ≠ X then H in general
- Z gate on |0⟩ is a no-op in measurement terms


---

## Lab 5 — Hello Quantum World Program

**File:** `lab_5.py`
**Objective:** Execute the canonical "Hello Quantum World" circuit and perform statistical analysis of quantum randomness.

### The Circuit
- Single qubit, Hadamard gate, measure
- State: H|0⟩ = (|0⟩ + |1⟩)/√2 = |+⟩
- Theoretical probability: P(0) = P(1) = 0.5 exactly

### Parts Covered

**Part 1 — Basic Hello Quantum World**
- 1000 shots of H + measure
- Result: approximately `{'0': 503, '1': 497}` (varies)
- Demonstrates quantum randomness in action

**Part 2 — Multiple Runs Analysis**
- 5 independent runs of 100 shots each
- Records P(0) and P(1) for each run
- Shows natural statistical variation between runs
- Example: Run 1: P(0)=0.52, Run 2: P(0)=0.48, etc.
- Demonstrates that quantum randomness is genuine, not pseudo-random

**Part 3 — Shot Count Analysis**
- Runs with 10, 100, 1000, 10000 shots
- Tracks how P(0) and P(1) converge toward 0.5 as shots increase
- 10 shots: high variance (e.g., 0.6/0.4)
- 10000 shots: very close to 0.5/0.5
- Demonstrates the Law of Large Numbers applied to quantum measurement

**Part 4 — Theoretical vs Experimental**
- 10000-shot run for high-precision comparison
- Theoretical: P(0) = 0.500, P(1) = 0.500
- Experimental: typically within ±0.01 of theoretical
- Deviation printed for both outcomes

### Visualization
- 2×3 matplotlib grid (14×8 inches)
- Top-left: Circuit diagram text box
- Top-middle: Multiple runs grouped bar chart (|0⟩ and |1⟩ per run)
- Top-right: Shot count convergence plot (semi-log x-axis)
- Bottom (full width): Main 1000-shot result bar chart with theoretical line at y=500
- Output file: `qiskit_lab_5_final_image.png`

### Key Takeaways
- Quantum randomness is fundamentally different from classical pseudo-randomness
- More shots → results converge to theoretical probabilities (Born rule)
- `ax.semilogx()` for log-scale shot count plots
- `ax.axhline(y=500)` to draw theoretical reference lines
- Statistical convergence rate is O(1/√N) — need 100x more shots for 10x precision

