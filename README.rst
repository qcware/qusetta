qusetta
=======

Translating quantum circuits to and from representations -- the Rosetta Stone for quantum circuits.

.. |master_branch_circleci| image:: https://circleci.com/gh/qcware/qusetta/tree/master.svg?style=svg&circle-token=aee09028070dbb276e20c86a128132334f00a037
    :target: https://circleci.com/gh/qcware/qusetta/tree/master

*master branch*  --->   |master_branch_circleci|

*Circle CI fails right now because I have it just trying to import "quasar". Once quasar is open-sourced, then the Circle CI should start passing.*

**README contents**

.. contents::
    :local:
    :backlinks: top


Installation
------------

To install from source:

.. code:: shell

    git clone https://github.com/qcware/qusetta.git
    cd qusetta
    pip install -e .


Example usage
-------------

Please see ``help(qusetta)`` for all the functionality in ``qusetta``. The circuit representations that we support converting between are listed in ``qusetta.__all__``.

Let's create a Qiskit circuit.

.. code:: python

    from qiskit import QuantumCircuit

    circuit = QuantumCircuit(3)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.rx(1.2, 1)
    circuit.z(1)


Now we'll convert it to Cirq and Quasar.

.. code:: python

    from qusetta import Qiskit

    cirq_circuit = Qiskit.to_cirq(circuit)
    quasar_circuit = Qiskit.to_quasar(circuit)


Contributing
------------

Create a branch or fork the repo, add your functionality and tests, and submit a pull request. Before submitting any pull requests, please check the coverage report (located in the *Artifacts* tab on CircleCI of the test workflow; look for the ``index.html`` file) to ensure that you are testing the new functionality sufficiently.


To do
-----

- Currently I only have circuit translation to/from cirq from/to qusetta (where the qusetta representation is the internal representation we use). I need to add functions for

  - qiskit to/from qusetta, and
  - quasar to/from qusetta.

  Once those are in place, the code's infrastructure already takes care of qiskit to/from cirq to/from quasar etc.

- I also probably need to support for more gates, and figure out something to do with measure gates.
