"""Translating circuits to and from ``quasar``.

"""

import quasar
import qusetta as qu
from typing import List
from math import pi as PI
# define PI so that in string gates we can have pi as an angle.
# Because we use eval for string gates. For example, gate = "Rz(PI/2, 1)".


__all__ = "Quasar",


class Quasar(qu.Conversions):
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
        raise NotImplementedError

    @staticmethod
    def to_qusetta(circuit: quasar.Circuit) -> List[str]:
        """Convert a quasar circuit to a qusetta circuit.

        Parameters
        ----------
        circuit : quasar.Circuit object.

        Returns
        -------
        qu_circuit : list of strings.
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
        # check the result above after I implement it!
        raise NotImplementedError
