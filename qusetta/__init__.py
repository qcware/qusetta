"""``qusetta``.

Translations and representations of quantum circuits. See ``help(qusetta)``.

The ``qusetta`` representation of a circuit is a list of strings, where each
string represents a gate. The gates can be any gates listed in
``qusetta.PARAMETER_FREE_GATES`` and ``qusetta.PARAMETER_GATES``.

The parameter gates are represented with two argument list, the first
for parameters and the second for qubits. For example, an X rotation
by an angle of ``pi/2`` on qubit 1 would be ``"Rx(PI/2)(1)"``.

The parameter free gates are represented with one argument list, that
being the qubits. So for example a Hadamard gate on qubit 3 would be
``"H(3)"``.

So for example, ``qusetta_circuit = ["H(0)", "CX(0, 1)", "RX(PI/2)(0)"]``.

"""

from ._version import *

from ._gates import *
from ._conversions import *
from ._quasar import *

__all__ = "Quasar",

try:
    import qiskit
    from ._qiskit import *
    __all__ += "Qiskit",
except (ImportError, ModuleNotFoundError) as e:
    pass

try:
    import cirq
    from ._cirq import *
    __all__ += "Cirq",
except (ImportError, ModuleNotFoundError) as e:
    pass

name = "qusetta"
