"""Define the qusetta representation of a circuit.

We don't do much here. The Qusetta class is defined more for ease
than for function. We simply use all the methods from the Cirq,
Qiskit, Quasar, etc. classes and wrap them in the Qusetta class.

"""

import cirq
import qiskit
import quasar
import qusetta as qu
from typing import List

__all__ = "Qusetta",


class Qusetta:
    """Translation methods for qusetta's representation of a circuit.

    qusetta's representation of a circuit is a list of strings, where each
    string represents a gate. The gates can be any gates listed in
    ``qusetta.PARAMETER_FREE_GATES`` and ``qusetta.PARAMETER_GATES``.

    The parameter gates are represented with two argument list, the first
    for parameters and the second for qubits. For example, an X rotation
    by an angle of ``pi/2`` on qubit 1 would be ``"Rx(PI/2)(1)"``.

    The parameter free gates are represented with one argument list, that
    being the qubits. So for example a Hadamard gate on qubit 3 would be
    ``"H(3)"``.

    Examples
    --------
    >>> import qusetta as qu

    Create a Qusetta circuit and convert to a cirq Circuit.

    >>> circuit = ["H(0)", "CX(0, 1)", "CX(0, 2)", "RZ(PI/4)(2)"]
    >>> cirq_circuit = qu.Qusetta.to_cirq(circuit)

    Create a Qusetta circuit from a qiskit circuit.

    >>> import qiskit
    >>> circuit = qiskit.QuantumCircuit(2)
    >>> circuit.h(0)
    >>> circuit.cx(0, 1)
    >>> qu_circuit = qu.Qusetta.from_qiskit(circuit)
    >>> print(qu_circuit)
    ["H(0)", "CX(0, 1)"]

    """

    @staticmethod
    def from_qusetta(circuit: List[str]) -> List[str]:
        """Convert from a qusetta circuit to a Qusetta circuit.

        We include this method for consistency. But it just copies
        ``circuit``.

        Parameters
        ----------
        circuit : list of strings.
            See ``help(qusetta.Qusetta)`` for more details on how the list of
            strings should be formatted.

        Return
        ------
        qu_circuit : list of strings.

        """
        return circuit.copy()

    @staticmethod
    def to_qusetta(circuit: List[str]) -> List[str]:
        """Convert from a qusetta circuit to a Qusetta circuit.

        We include this method for consistency. But it just copies
        ``circuit``.

        Parameters
        ----------
        circuit : list of strings.
            See ``help(qusetta.Qusetta)`` for more details on how the list of
            strings should be formatted.

        Return
        ------
        qu_circuit : list of strings.

        """
        return circuit.copy()

    @staticmethod
    def from_cirq(circuit: cirq.Circuit) -> List[str]:
        """Create a qusetta circuit from a cirq circuit.

        Parameters
        ----------
        circuit : cirq.Circuit object.

        Return
        ------
        qu_circuit : list of strings.
            See ``help(qusetta.Qusetta)`` for more details on how the list of
            strings is be formatted.

        """
        return qu.Cirq.to_qusetta(circuit)

    @staticmethod
    def to_cirq(circuit: List[str]) -> cirq.Circuit:
        """Create a cirq circuit from a qusetta circuit.

        Parameters
        ----------
        circuit : list of strings.
            See ``help(qusetta.Qusetta)`` for more details on how the list of
            strings is be formatted.

        Returns
        -------
        cirq_circuit : cirq.Circuit object.

        """
        return qu.Cirq.from_qusetta(circuit)

    @staticmethod
    def from_qiskit(circuit: qiskit.QuantumCircuit) -> List[str]:
        """Create a qusetta circuit from a qiskit circuit.

        Parameters
        ----------
        circuit : qiskit.QuantumCircuit object.

        Return
        ------
        qu_circuit : list of strings.
            See ``help(qusetta.Qusetta)`` for more details on how the list of
            strings is be formatted.

        """
        return qu.Qiskit.to_qusetta(circuit)

    @staticmethod
    def to_qiskit(circuit: List[str]) -> qiskit.QuantumCircuit:
        """Create a qiskit circuit from a qusetta circuit.

        Parameters
        ----------
        circuit : list of strings.
            See ``help(qusetta.Qusetta)`` for more details on how the list of
            strings is be for"Rmatted.

        Returns
        -------
        qiskit_circuit : qiskit.QuantumCircuit object.

        """
        return qu.Qiskit.from_qusetta(circuit)

    @staticmethod
    def from_quasar(circuit: quasar.Circuit) -> List[str]:
        """Create a qusetta circuit from a quasar circuit.

        Parameters
        ----------
        circuit : quasar.Circuit object.

        Return
        ------
        qu_circuit : list of strings.
            See ``help(qusetta.Qusetta)`` for more details on how the list of
            strings is be formatted.

        """
        return qu.Quasar.to_qusetta(circuit)

    @staticmethod
    def to_quasar(circuit: List[str]) -> quasar.Circuit:
        """Create a quasar circuit from a qusetta circuit.

        Parameters
        ----------
        circuit : list of strings.
            See ``help(qusetta.Qusetta)`` for more details on how the list of
            strings is be formatted.

        Returns
        -------
        quasar_circuit : quasar.Circuit object.

        """
        return qu.Quasar.from_qusetta(circuit)
