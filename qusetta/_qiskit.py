"""Translating circuits to and from ``qiskit``.

"""

import qiskit
import qusetta as qu
from typing import List
from math import pi as PI
# define PI so that in string gates we can have pi as an angle.
# Because we use eval for string gates. For example, gate = "Rz(PI/2, 1)".


__all__ = "Qiskit",


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
        raise NotImplementedError

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
        # check the result above after I implement it!
        raise NotImplementedError
