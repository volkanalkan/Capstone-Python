from bb84_simulation import bits as alice_bits, bases as alice_bases
from eve_interception import eve_bases, eve_results, intercepted_circuits
from bob_measurement import bob_bases, bob_results

matching_indices = [i for i in range(len(alice_bases)) if alice_bases[i] == bob_bases[i]]

alice_key = [alice_bits[i] for i in matching_indices]
bob_key = [bob_results[i] for i in matching_indices]

matching_bits = sum(1 for a, b in zip(alice_key, bob_key) if a == b)
accuracy = matching_bits / len(alice_key) * 100 if alice_key else 0

print("\n--- QKD SIMULATION SUMMARY ---")
print("Alice's bits:     ", alice_bits)
print("Alice's bases:    ", alice_bases)
print("Eve's bases:      ", eve_bases)
print("Eve's results:    ", eve_results)
print("Bob's bases:      ", bob_bases)
print("Bob's results:    ", bob_results)
print("Matching indices: ", matching_indices)
print("Alice's key:      ", alice_key)
print("Bob's key:        ", bob_key)
print(f"Key Match Ratio:  {accuracy:.2f}%")
