"""Translating circuits to and from ``cirq``."""
import cirq
import qusetta as qs
from typing import List


__all__ = "Cirq",


MAPPING = {"RX": "rx", "RY": "ry", "RZ": "rz"}


class Cirq(qs.Conversions):
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
            See ``help(qusetta)`` for more details on how the list of
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
            g, params, qubits = qs.gate_info(gate)
            qubits = [cirq.LineQubit(x) for x in qubits]
            cirq_gate = getattr(cirq, MAPPING.get(g, g))
            if params:
                cirq_gate = cirq_gate(*params)
            cirq_circuit.append(cirq_gate(*qubits))

        return cirq_circuit

    @staticmethod
    def to_qusetta(circuit: cirq.Circuit) -> List[str]:
        """Convert a cirq circuit to a qusetta circuit.

        Parameters
        ----------
        circuit : cirq.Circuit object.

        Returns
        -------
        qs_circuit : list of strings.
            See ``help(qusetta)`` for more details on how the list of
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
            str(gate).strip().upper().replace(
                "CNOT", "CX"
            ).replace(
                "TOFFOLI", "CCX"
            ).replace(
                "Π", "PI" if (
                    hasattr(gate.gate, "exponent") and gate.gate.exponent == 1
                ) else "*PI"
            )
            for gate in circuit.all_operations()
            if not isinstance(gate.gate, cirq.MeasurementGate)
            # ignore measurements
        ]
