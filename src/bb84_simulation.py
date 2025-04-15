from qiskit import QuantumCircuit
import random

def generate_bits_and_bases(n):
    bits = [random.randint(0, 1) for _ in range(n)]
    bases = [random.choice(['Z', 'X']) for _ in range(n)]
    return bits, bases

def create_bb84_circuit(bits, bases):
    circuit_list = []
    for bit, basis in zip(bits, bases):
        qc = QuantumCircuit(1, 1)
        if bit == 1:
            qc.x(0)  
        if basis == 'X':
            qc.h(0)  
        qc.barrier()
        circuit_list.append(qc)
    return circuit_list

n = 10
bits, bases = generate_bits_and_bases(n)
circuits = create_bb84_circuit(bits, bases)

if __name__ == "__main__":
    print("Alice's bits:", bits)
    print("Alice's bases:", bases)
    print()

    for i, qc in enumerate(circuits):
        print(f"Circuit {i + 1}:")
        print(qc.draw())
        print()
