"""Translating circuits to and from ``cirq``.

"""

import cirq
import qusetta as qu
from typing import List
from math import pi as PI
# define pi so that in string gates we can have pi as an angle.
# Because we use eval for string gates. For example, gate = "Rz(pi/2, 1)".


__all__ = "Cirq",


class Cirq(qu.Conversions):
    """Translation methods for cirq's representation of a circuit.

    Example
    --------
    Create a cirq circuit.

    >>> import cirq
    >>> qubits = [cirq.LineQubit(0), cirq.LineQubit(1)]
    >>> circuit = cirq.Circuit()
    >>> circuit.append(cirq.H(q[0]))
    >>> circuit.append(cirq.CX(q[0], q[1]))

    Convert the cirq circuit to a qiskit circuit.

    >>> from qusetta import Cirq
    >>> qiskit_circuit = Cirq.to_qiskit(circuit)

    """

    @staticmethod
    def from_qusetta(circuit: List[str]) -> cirq.Circuit:
        """Convert a qusetta circuit to a cirq circuit.

        Parameters
        ----------
        circuit : list of strings.
            See ``help(qusetta.Qusetta)`` for more details on how the list of
            strings should be formatted.

        Returns
        -------
        cirq_circuit : cirq.Circuit.

        Examples
        --------
        >>> from qusetta import Cirq
        >>>
        >>> circuit = ["H(0)", "CX(0, 1)", "RX(PI/2)(0)", "SWAP(1, 2)"]
        >>> cirq_circuit = Cirq.from_qusetta(circuit)

        """
        cirq_circuit = cirq.Circuit()
        for gate in circuit:
            i = gate.index('(')
            g = gate[:i].strip().upper()
            gate = gate[i+1:]
            if g in qu.PARAMETER_GATES:
                j = gate.index(")")
                params = [float(eval(x)) for x in gate[:j].split(',')]
                i = gate.index('(')
                gate = gate[i+1:]
                j = gate.index(')')
                qubits = [cirq.LineQubit(int(x)) for x in gate[:j].split(',')]
                if g in ("RX", "RY", "RZ"):
                    g = g.lower()
                cirq_circuit.append(eval("cirq." + g)(*params)(*qubits))
            elif g in qu.PARAMETER_FREE_GATES:
                j = gate.index(")")
                qubits = [cirq.LineQubit(int(x)) for x in gate[:j].split(',')]
                cirq_circuit.append(eval("cirq." + g)(*qubits))
            else:
                raise NotImplementedError("%s is not recognized" % g)

        return cirq_circuit

    @staticmethod
    def to_qusetta(circuit: cirq.Circuit) -> List[str]:
        """Convert a cirq circuit to a qusetta circuit.

        Parameters
        ----------
        circuit : cirq.Circuit object.

        Returns
        -------
        qu_circuit : list of strings.
            See ``help(qusetta.Qusetta)`` for more details on how the list of
            strings should be formatted.

        Examples
        --------
        >>> from qusetta import Cirq
        >>> import cirq
        >>>
        >>> circuit = cirq.Circuit()
        >>> qubits = [cirq.LineQubit(i) for i in range(3)]
        >>> circuit.append(cirq.H(qubits[0]))
        >>> circuit.append(cirq.CX(qubits[0], qubits[1]))
        >>> circuit.append(cirq.Rx(1/2)(qubits[0]))
        >>> circuit.append(cirq.SWAP(qubits[1], qubits[2]))
        >>>
        >>> print(Cirq.to_qusetta(circuit))
        ["H(0)", "CX(0, 1)", "Rx(0.5)(0)", "SWAP(1, 2)"]

        """
        return [
            str(gate).replace(
                "CNOT", "CX"
            ).replace(
                "π", "PI" if (
                    hasattr(gate.gate, "exponent") and gate.gate.exponent == 1
                ) else "*PI"
            ).upper().strip()
            for gate in circuit.all_operations()
        ]
