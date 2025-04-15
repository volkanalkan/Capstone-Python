import random
from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.compiler import transpile
from bb84_simulation import bits as alice_bits, bases as alice_bases, circuits as alice_circuits

# Bob'un rastgele seçtiği bazlar
bob_bases = [random.choice(['Z', 'X']) for _ in range(len(alice_bits))]
bob_results = []

# Simülasyon için backend
simulator = AerSimulator()

for i in range(len(alice_circuits)):
    circuit = alice_circuits[i].copy()

    # Ölçüm register'ı ekleniyor (1 klasik bit)
    creg = ClassicalRegister(1)
    circuit.add_register(creg)

    # Eğer Bob X bazında ölçmek istiyorsa Hadamard uygula
    if bob_bases[i] == 'X':
        circuit.h(0)

    # Ölçüm işlemi
    circuit.measure(0, creg[0])

    # Derle ve simüle et
    compiled = transpile(circuit, simulator)
    result = simulator.run(compiled, shots=1).result()
    counts = result.get_counts()
    measured_bit = int(list(counts.keys())[0].split()[-1])  # Ölçülen son bit alınır
    bob_results.append(measured_bit)

# Sonuçları yazdır
print("Bob's bases:", bob_bases)
print("Bob's results:", bob_results)
