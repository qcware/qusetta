qusetta
=======

Translating quantum circuits to and from representations -- the Rosetta Stone for quantum circuits.

.. |master_branch_circleci| image:: https://circleci.com/gh/qcware/qusetta/tree/master.svg?style=svg
    :target: https://circleci.com/gh/qcware/qusetta/tree/master

*master branch*  --->   |master_branch_circleci|


**README contents**

.. contents::
    :local:
    :backlinks: top


Installation
------------

To install:

.. code:: shell

    pip install git+https://github.com/qcware/qusetta

Or you can clone the repository and then install:

.. code:: shell

    git clone https://github.com/qcware/qusetta.git
    cd qusetta
    pip install -e .


Example usage
-------------

Please see ``help(qusetta)`` for all the functionality in *qusetta*. The circuit representations that we support converting between are listed in ``qusetta.__all__``.

Convert a qiskit circuit to cirq and quasar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's create a qiskit circuit.

.. code:: python

    from qiskit import QuantumCircuit

    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.rx(1.2, 1)
    circuit.z(1)


Now we'll convert it to cirq and quasar.

.. code:: python

    from qusetta import Qiskit

    cirq_circuit = Qiskit.to_cirq(circuit)
    quasar_circuit = Qiskit.to_quasar(circuit)

Or equivalently we could have done

.. code:: python

    from qusetta import Cirq, Quasar

    cirq_circuit = Cirq.from_qiskit(circuit)
    quasar_circuit = Quasar.from_qiskit(circuit)


We can also convert it to a *qusetta* circuit (see the next section).

.. code:: python
    
    from qusetta import Qiskit
    qusetta_circuit = Qiskit.to_qusetta(circuit)


Create qiskit, cirq, and quasar circuits from a qusetta circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A *qusetta* circuit is simply a list of strings, all uppercase, where each string represents a gate. For example,

- a Hadamard gate on qubit 0 looks like :code:`"H(0)"`,
- a CX gate with qubit 0 being the control and qubit 2 the target looks like :code:`"CX(0, 2)"`,
- an Rx gate by an angle of 1.2 on qubit 1 looks like :code:`"RX(1.2)(1)"` (note that the parameters and qubits go in separate parentheses),
- an Rz gate by an angle of pi/2 on qubit 0 looks like :code:`"RZ(PI/2)(0)"` (note how qusetta can evaluate the expression ``PI/2``),
- etc.

We can specify our circuit in *qusetta* form, and then translate it to all the other circuit types.

.. code:: python

    from qusetta import Qiskit, Cirq, Quasar

    qusetta_circuit = ["H(0)", "CX(0, 1)", "RY(PI/3)(2)", "T(1)", "S(0)"]

    qiskit_circuit = Qiskit.from_qusetta(qusetta_circuit)
    cirq_circuit = Cirq.from_qusetta(qusetta_circuit)
    quasar_circuit = Quasar.from_qusetta(qusetta_circuit)


Important details about the translation
---------------------------------------

Consider starting with a circuit cA written with A (e.g. A could be cirq, qiskit, etc). Then we use *qusetta* to translate to B, C, etc, therefore creating cB, cC, etc. The translations are defined such that simulating cA with A will give the same probability vector as simulating cB with B, cC with C, etc. A few things to note.

- The simulations will give the same *probability vector* but not necessarily give the same *state vector*; they may be off by global phases.
- The translations will ensure that the circuits give the same probability vector, but the circuits themselves may not be equivalent. Gate ordering will often be different through translations.
- As we all know, qiskit is different in the way that they index their qubits. In particular, they index qubits in reverse order compared to everyone else. Therefore, in order to ensure that the first bullet point is true, *qusetta* reverses the qubits of a qiskit circuit. Thus, as an example, a qusetta (or cirq, quasar) circuit ``["H(0)", "CX(0, 1)"]`` becomes a qiskit circuit ``["H(1)", "CX(1, 0)"]``. This is how we guarantee that the probability vectors are the same.


A note on the purpose of qusetta
--------------------------------

It is my personal opinion that something like *qusetta* shouldn't really exist, or at least should not be assumed to be robust. From the perspective of QC Ware, I think we should be encouraging users to adopt quasar rather than encouraging them to translate their qiskit/cirq/etc circuits to quasar. Any act of translation necessarily loses some of the features unique to each circuit type (as an example, qiskit allows for classical registers and feedback, but neither cirq nor quasar to my knowledge allow this). Therefore, people should only use *qusetta* when their circuits are very basic; if a user wants to include more advanced features in their circuit, then they are clearly advanced enough to do the translation themselves. All this being said, there are many features missing from *qusetta* that would allow better translation between circuit types. After all, *qusetta*'s internal representation of circuits is just a list of strings; if a circuit is too complicated to reasonably represent with such a data structure, then it should be written in one of the actual quantum programming languages!


Contributing
------------

Create a branch or fork the repo, add your functionality and tests, and submit a pull request. Before submitting any pull requests, please check the coverage report (located in the *Artifacts* tab on CircleCI of the test workflow; look for the ``index.html`` file) to ensure that you are testing the new functionality sufficiently.

To add a new circuit representation (call it ``A``), you need to

- add the ``to_A`` and ``from_A`` classmethods in the ``_conversions.py`` file.
- add a class ``A`` in a new file ``_a.py`` that has ``to_qusetta`` and ``from_qusetta`` staticmethods. The class should inherit from ``qusetta.Conversions``. 

With those defined, all the circuit representations will be able to translate to/from the new representation ``A``.

Then you need to add tests for translating to and from all of the other circuit types. Follow the pattern in ``tests/test_translation.py`` and add to it.


To do
-----

- Maybe do something with measurement gates besides just ignoring them.
- Add more circuit tests (e.g. ``test_circuit_3``, ``test_circuit_4``, etc).
- More gates.
