import random
from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.compiler import transpile
from eve_interception import intercepted_circuits as eve_circuits

bob_bases = [random.choice(['Z', 'X']) for _ in range(len(eve_circuits))]
bob_results = []

simulator = AerSimulator()

for i in range(len(eve_circuits)):
    circuit = eve_circuits[i].copy()

    creg = ClassicalRegister(1)
    circuit.add_register(creg)

    if bob_bases[i] == 'X':
        circuit.h(0)

    circuit.measure(0, creg[0])

    compiled = transpile(circuit, simulator)
    result = simulator.run(compiled, shots=1).result()
    counts = result.get_counts()
    measured_bit = int(list(counts.keys())[0].replace(' ', ''))
    bob_results.append(measured_bit)

print("Bob's bases:", bob_bases)
print("Bob's results:", bob_results)
