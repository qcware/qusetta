# if you're running this from the examples directory, then add to path
import sys; sys.path.append("..")
import qusetta as qs

# We'll look at a 3 qubit QAOA example for the Hamiltonian
#     H = z_0 z_1 + z_1 z_2
# We'll write our circuit as a big string, and then use the
# .split method around semicolons to make it into a list.

# The first element of the circuit is a column of Hadamards
circuit = "H(0); H(1); H(2); "

# next we have exp(-i z_0 z_1 gamma / 2)
circuit += "CX(0, 1); RZ({gamma})(1); CX(0, 1); "

# now the same for exp(-i z_1 z_2 gamma / 2)
circuit += "CX(1, 2); RZ({gamma})(2); CX(1, 2); "

# now we have a row of x rotations by beta
circuit += "Rx({beta})(0); Rx({beta})(1); Rx({beta})(2)"

# that's the circuit. we can format the string to substitute in for
# beta and gamma. and then we split around ; to get it into qusetta's form.

def qusetta_qaoa_circuit(beta, gamma):
    return circuit.format(beta=beta, gamma=gamma).split("; ")

# let's see what it looks like
print("QAOA circuit:", qusetta_qaoa_circuit("beta", "gamma"))
print()

# next let's substitute beta = pi/2 and gamma = pi/4
c = qusetta_qaoa_circuit("PI/2", "PI/4")
print("QAOA circuit (beta=pi/2, gamma=pi/4):", c)
print()

# now let's convert it to a cirq circuit
print("Corresponding cirq circuit:")
print(qs.Cirq.from_qusetta(c))
print()

# and a quasar circuit
print("Corresponding quasar circuit:")
print(qs.Quasar.from_qusetta(c))
print()

# and a qiskit circuit
print("Corresponding qiskit circuit:")
print(qs.Qiskit.from_qusetta(c))
print("note how the bits are reversed in the qiskit circui")
print("(see the README or qusetta.Qiskit docstring for info)")
