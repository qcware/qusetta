"""Define the gates that we allow in our qusetta circuit representation."""

from typing import Tuple
from math import pi as PI
# define PI so that in string gates we can have pi as an angle.
# Because we use eval for string gates. For example, gate = "Rz(PI/2, 1)".

__all__ = "PARAMETER_FREE_GATES", "PARAMETER_GATES", "gate_info"


PARAMETER_FREE_GATES = frozenset({
    "I", "H", "X", "Y", "Z", "S", "T", "CX", "CZ", "SWAP", "CCX"
})

PARAMETER_GATES = frozenset({'RX', 'RY', 'RZ'})


def gate_info(gate: str) -> Tuple[str, Tuple[float, ...], Tuple[int, ...]]:
    """Get the gate info from a string gate.

    Parameters
    ----------
    gate : str.
        See ``help(qusetta)`` for how the gate should be specifed. As an
        example, a gate could be ``H(0)`` or ``RX(PI/2)(1)``.

    Returns
    -------
    res : tuple (str, tuple of floats, tuple of ints).
        The first element is the gate name, the second is the
        parameters (often empty), and the third is the qubits.

    Example
    -------
    >>> gate_info("CX(0, 1)")
    ("CX", (), (0, 1))
    >>> gate_info("RX(2)(3)")
    ("RX", (2,), (3,))

    """
    i = gate.index('(')
    g = gate[:i].strip().upper()
    gate = gate[i+1:]
    if g in PARAMETER_GATES:
        j = gate.index(")")
        params = tuple(float(eval(x)) for x in gate[:j].split(','))
        i = gate.index('(')
        gate = gate[i+1:]
        j = gate.index(')')
        qubits = tuple(int(x) for x in gate[:j].split(','))
    elif g in PARAMETER_FREE_GATES:
        j = gate.index(")")
        qubits = tuple(int(x) for x in gate[:j].split(','))
        params = tuple()
    else:
        raise NotImplementedError("%s is not recognized" % g)

    return g, params, qubits
