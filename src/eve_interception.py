import random
from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.compiler import transpile
from bb84_simulation import circuits as alice_circuits

eve_bases = [random.choice(['Z', 'X']) for _ in range(len(alice_circuits))]
eve_results = []
intercepted_circuits = []

simulator = AerSimulator()

for i in range(len(alice_circuits)):
    circuit = alice_circuits[i].copy()

    creg = ClassicalRegister(1)
    circuit.add_register(creg)

    if eve_bases[i] == 'X':
        circuit.h(0)

    circuit.measure(0, creg[0])
    compiled = transpile(circuit, simulator)
    result = simulator.run(compiled, shots=1).result()
    counts = result.get_counts()
    measured_bit = int(list(counts.keys())[0].replace(' ', ''))
    eve_results.append(measured_bit)

    new_qc = QuantumCircuit(1, 1)
    if measured_bit == 1:
        new_qc.x(0)
    if eve_bases[i] == 'X':
        new_qc.h(0)

    intercepted_circuits.append(new_qc)

print("Eve's bases:", eve_bases)
print("Eve's results:", eve_results)

if __name__ == "__main__":
    pass

__all__ = ["intercepted_circuits"]