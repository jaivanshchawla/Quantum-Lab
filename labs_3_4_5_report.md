# Quantum Computing Experiments: Labs 3, 4, and 5

## Experiment 3: Quantum Bits (Qubits) and Quantum Registers

### Objective
Understand qubits, quantum registers and classical registers.

### Detailed Theory
Quantum registers hold qubits forming tensor product spaces. Classical registers store measurement results.

In quantum computing, a quantum register is a collection of qubits that form the computational basis for quantum algorithms. When multiple qubits are combined in a quantum register, they exist in a tensor product space, meaning the total state space grows exponentially (2^n states for n qubits). Classical registers serve as the interface between quantum and classical worlds, storing the binary measurement outcomes when qubits collapse from superposition. The separation between quantum and classical registers is fundamental to quantum circuit design, as it allows us to preserve quantum information during computation while extracting classical results when needed.

### Procedure
1. Import Qiskit libraries
2. Create quantum and classical registers
3. Apply required gates
4. Execute using Aer simulator
5. Analyze results using histogram/statevector

### Program (Qiskit Implementation)
```python
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr, cr)
qc.draw('text')
```

### Conclusion
The experiment successfully demonstrated the creation of a 2-qubit quantum register paired with a 2-bit classical register, establishing the foundational structure for quantum circuits. The circuit visualization confirms proper initialization of the quantum-classical register architecture, ready for gate operations and measurements.

---

## Experiment 4: Creating a Simple Quantum Circuit

### Objective
Design and simulate a basic quantum circuit.

### Detailed Theory
Quantum circuits are sequences of unitary gates followed by measurement operations.

A quantum circuit represents a computational model where quantum gates manipulate qubit states through unitary transformations, preserving the total probability of the quantum system. The X gate (Pauli-X or NOT gate) used in this experiment is analogous to the classical NOT gate, flipping the qubit state from |0⟩ to |1⟩ or vice versa. Measurement operations collapse the quantum superposition into classical bits, projecting the quantum state onto the computational basis. This simple circuit demonstrates the complete quantum computation cycle: initialization, gate application, and measurement.

### Procedure
1. Import Qiskit libraries
2. Create quantum and classical registers
3. Apply required gates
4. Execute using Aer simulator
5. Analyze results using histogram/statevector

### Program (Qiskit Implementation)
```python
from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend).result()
print(result.get_counts())
```

### Conclusion
The circuit produced deterministic output {'1': 1024} (or similar count), confirming that the X gate successfully flipped the initial |0⟩ state to |1⟩. This validates the fundamental quantum gate operation and measurement process, demonstrating 100% probability of measuring state |1⟩ after applying the X gate.

---

## Experiment 5: Hello Quantum World Program

### Objective
Execute Hello Quantum World program and analyze output.

### Detailed Theory
Applying Hadamard gate creates equal superposition giving ~50% probability for 0 and 1.

The Hadamard gate is one of the most important single-qubit gates in quantum computing, transforming basis states into equal superpositions: H|0⟩ = (|0⟩ + |1⟩)/√2. This creates a quantum state where the qubit exists simultaneously in both |0⟩ and |1⟩ states with equal amplitude. Upon measurement, the superposition collapses randomly to either outcome with 50% probability each, demonstrating true quantum randomness. This experiment represents the quintessential "Hello World" of quantum computing, showcasing superposition—a fundamental quantum mechanical principle that distinguishes quantum from classical computation.

### Procedure
1. Import Qiskit libraries
2. Create quantum and classical registers
3. Apply required gates
4. Execute using Aer simulator
5. Analyze results using histogram/statevector

### Program (Qiskit Implementation)
```python
from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
backend = Aer.get_backend('qasm_simulator')
print(execute(qc, backend, shots=1000).result().get_counts())
```

### Conclusion
The experiment yielded approximately equal counts for both outcomes (e.g., {'0': 503, '1': 497}), confirming the Hadamard gate successfully created an equal superposition state. The near 50-50 distribution across 1000 shots validates quantum superposition and demonstrates genuine quantum randomness, a key resource for quantum algorithms.
