"""Translating circuits to and from ``qiskit``."""

import qiskit
import qusetta as qu
from typing import List


__all__ = "Qiskit",


# TODO: support u3
# u3 = lambda p, r: [
#     # p = params, r = register
#     # params should be array of 3 angles in (0, 4pi).
#     # register is which register to apply gate to.
#     "rz(%g, %d)" % (p[1], r),
#     "ry(%g, %d)" % (p[0], r),
#     "rz(%g, %d)" % (p[2], r)
# ]


class Qiskit(qu.Conversions):
    """Translation methods for qiskit's representation of a circuit.

    Example
    --------
    Create a qiskit circuit.

    >>> import qiskit
    >>> circuit = qiskit.QuantumCircuit(2)
    >>> circuit.h(0)
    >>> circuit.cx(0, 1)

    Convert the qiskit circuit to a cirq circuit.

    >>> from qusetta import Qiskit
    >>> cirq_circuit = Qiskit.to_cirq(circuit)

    """

    @staticmethod
    def from_qusetta(circuit: List[str]) -> qiskit.QuantumCircuit:
        """Convert a qusetta circuit to a qiskit circuit.

        Parameters
        ----------
        circuit : list of strings.
            See ``help(qusetta)`` for more details on how the list of
            strings should be formatted.

        Returns
        -------
        qiskit_circuit : qiskit.QuantumCircuit.

        Examples
        --------
        >>> from qusetta import Qiskit
        >>>
        >>> circuit = ["H(0)", "CX(0, 1)", "RX(PI/2)(0)", "SWAP(1, 2)"]
        >>> qiskit_circuit = Qiskit.from_qusetta(circuit)

        """
        n, new_circuit = -1, []
        for gate in circuit:
            g, params, qubits = qu.gate_info(gate)
            n = max(max(qubits), n)
            new_circuit.append((g.lower(), params, qubits))

        qiskit_circuit = qiskit.QuantumCircuit(n + 1)
        for g, params, qubits in new_circuit:
            # ibm is weird and reversed their qubits from everyone else.
            # So we reverse them here.
            qubits = tuple(n - q for q in qubits)
            getattr(qiskit_circuit, g)(*(params + qubits))

        return qiskit_circuit

    @staticmethod
    def to_qusetta(circuit: qiskit.QuantumCircuit) -> List[str]:
        """Convert a qiskit circuit to a qusetta circuit.

        Parameters
        ----------
        circuit : qiskit.QuantumCircuit object.

        Returns
        -------
        qu_circuit : list of strings.
            See ``help(qusetta)`` for more details on how the list of
            strings should be formatted.

        Examples
        --------
        >>> from qusetta import Qiskit
        >>> import qiskit
        >>>
        >>> circuit = qiskit.QuantumCircuit(3)
        >>> circuit.h(0)
        >>> circuit.cx(0, 1)
        >>> circuit.rx(1/2, 0)
        >>> circuit.swap(1, 2)
        >>>
        >>> print(Qiskit.to_qusetta(circuit))
        ["H(0)", "CX(0, 1)", "RX(0.5)(0)", "SWAP(1, 2)"]

        """
        qu_circuit = []
        for gate, qubits, _ in circuit:  # _ refers to classical bits
            g = gate.name.upper()
            if g == "ID":
                g = "I"
            if gate.params:
                g += "(" + ", ".join(str(x) for x in gate.params) + ")"
            # ibm is weird and reversed their qubits from everyone else.
            # So we reverse them here.
            g += "(" + ", ".join(
                str(circuit.num_qubits - q.index - 1)
                for q in qubits
            ) + ")"
            qu_circuit.append(g)
        return qu_circuit
