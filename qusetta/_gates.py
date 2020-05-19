"""Define the gates that we allow in our qusetta circuit representation.

"""

__all__ = "PARAMETER_FREE_GATES", "PARAMETER_GATES"


PARAMETER_FREE_GATES = frozenset({
    "I", "H", "X", "Y", "Z", "S", "T", "CX", "CZ", 'SWAP'
})

PARAMETER_GATES = frozenset({'RX', 'RY', 'RZ'})
