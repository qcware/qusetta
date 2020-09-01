"""Translating circuits to and from ``qiskit``."""
import qiskit
import qusetta as qs
from typing import List


__all__ = "Qiskit",


class Qiskit(qs.Conversions):
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

    Notes
    -----
    As we all know, qiskit is weird in the way that they index their qubits.
    In particular, they index qubits in reverse order compared to everyone
    else. Therefore, in order to ensure that the first bullet point is true,
    qusetta reverses the qubits of a qiskit circuit. Thus, as an example, a
    qusetta (or cirq, quasar) circuit ``["H(0)", "CX(0, 1)"]`` becomes a
    qiskit circuit ``["H(1)", "CX(1, 0)"]``. This is how we guarantee that
    the probability vectors are the same.

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

        See the ``Qiskit`` class docstring for info on how the bit ordering
        is changed.

        """
        n, new_circuit = -1, []
        for gate in circuit:
            g, params, qubits = qs.gate_info(gate)
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
        qs_circuit : list of strings.
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
        ["H(2)", "CX(2, 1)", "RX(0.5)(2)", "SWAP(1, 0)"]

        Notice how the bits are reversed. See the ``Qiskit`` class docstring
        for more info.

        """
        qs_circuit = []
        for gate, qubits, _ in circuit:  # _ refers to classical bits
            g = gate.name.upper()

            if g == "MEASURE":  # ignore measure gates
                continue
            elif g == "ID":
                g = "I"
            elif g == "U1":
                g = "RZ"  # same up to a phase factor
            elif g == "U2":
                # see below for why we reverse the qubits
                r = circuit.num_qubits - qubits[0].index - 1
                qs_circuit.extend([
                    "RZ(%g - PI/2)(%d)" % (gate.params[1], r),
                    "RX(PI/2)(%d)" % r,
                    "RZ(%g + PI/2)(%d)" % (gate.params[0], r)
                ])
                continue
            elif g == "U3":
                # see below for why we reverse the qubits
                r = circuit.num_qubits - qubits[0].index - 1
                qs_circuit.extend([
                    "RZ(%g - PI/2)(%d)" % (gate.params[2], r),
                    "RX(%g)(%d)" % (gate.params[0], r),
                    "RZ(%g + PI/2)(%d)" % (gate.params[1], r)
                ])
                continue

            if gate.params:
                g += "(" + ", ".join(str(x) for x in gate.params) + ")"
            # ibm is weird and reversed their qubits from everyone else.
            # So we reverse them here.
            g += "(" + ", ".join(
                str(circuit.num_qubits - q.index - 1)
                for q in qubits
            ) + ")"
            qs_circuit.append(g)

        return qs_circuit
