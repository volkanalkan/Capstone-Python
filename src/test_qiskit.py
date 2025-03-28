from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.compiler import transpile

# Quantum circuit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Transpile & simulate
backend = AerSimulator()
compiled_circuit = transpile(qc, backend)
result = backend.run(compiled_circuit, shots=1024).result()

# Get counts & plot
counts = result.get_counts()
print(counts)
plot_histogram(counts).show()
