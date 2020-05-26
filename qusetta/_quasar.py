"""Translating circuits to and from ``quasar``."""

import quasar
import qusetta as qs
from typing import List


__all__ = "Quasar",


MAPPING = {"RX": "Rx", "RY": "Ry", "RZ": "Rz"}


class Quasar(qs.Conversions):
    """Translation methods for quasar's representation of a circuit.

    Example
    --------
    Create a quasar circuit.

    >>> import quasar
    >>> circuit = quasar.Circuit(2)
    >>> circuit.H(0)
    >>> circuit.CX(0, 1)

    Convert the quasar circuit to a cirq circuit.

    >>> from qusetta import Quasar
    >>> cirq_circuit = Quasar.to_cirq(circuit)

    """

    @staticmethod
    def from_qusetta(circuit: List[str]) -> quasar.Circuit:
        """Convert a qusetta circuit to a quasar circuit.

        Parameters
        ----------
        circuit : list of strings.
            See ``help(qusetta)`` for more details on how the list of
            strings should be formatted.

        Returns
        -------
        quasar_circuit : quasar.Circuit.

        Examples
        --------
        >>> from qusetta import Quasar
        >>>
        >>> circuit = ["H(0)", "CX(0, 1)", "RX(PI/2)(0)", "SWAP(1, 2)"]
        >>> quasar_circuit = Quasar.from_qusetta(circuit)

        """
        quasar_circuit = quasar.Circuit()
        for gate in circuit:
            g, params, qubits = qs.gate_info(gate)
            # qusetta's angles are twice what quasars are
            params = tuple(x / 2 for x in params)
            getattr(quasar_circuit, MAPPING.get(g, g))(*(qubits + params))
        return quasar_circuit

    @staticmethod
    def to_qusetta(circuit: quasar.Circuit) -> List[str]:
        """Convert a quasar circuit to a qusetta circuit.

        Parameters
        ----------
        circuit : quasar.Circuit object.

        Returns
        -------
        qs_circuit : list of strings.
            See ``help(qusetta)`` for more details on how the list of
            strings should be formatted.

        Examples
        --------
        >>> from qusetta import Quasar
        >>> import quasar
        >>>
        >>> circuit = quasar.Circuit()
        >>> circuit.H(0)
        >>> circuit.CX(0, 1)
        >>> circuit.Rx(0, theta=1/4)
        >>> circuit.SWAP(1, 2)
        >>>
        >>> print(Quasar.to_qusetta(circuit))
        ["H(0)", "CX(0, 1)", "RX(0.5)(0)", "SWAP(1, 2)"]

        """
        qs_circuit = []
        for (_, qubits), gate in circuit.gates.items():  # _ has time info
            g = gate.name.upper()
            if gate.parameters:
                g += "(" + ", ".join(
                    str(x * 2)  # quasar's angles are half what qusetta's are.
                    for x in gate.parameters.values()
                ) + ")"
            g += "(" + ", ".join(str(q) for q in qubits) + ")"
            qs_circuit.append(g)
        return qs_circuit
