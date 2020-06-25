"""Parent class for conversions."""

import qusetta as qs

__all__ = 'Conversions',


class Conversions:
    """Define class methods for conversions between circuits.

    Child classes should inherit from Conversions. For example,
    ``qusetta.Cirq`` inherits from Conversions, and therefore
    has all of the conversions to and from the different circuit
    representations (ie qiskit, quasar, etc).

    A child class *must* define a ``to_qusetta`` and a ``from_qusetta``
    staticmethod.

    """

    @classmethod
    def from_cirq(cls, circuit: 'cirq.Circuit') -> 'cls.Circuit':
        """Create a ``cls`` circuit from a cirq circuit.

        This is a classmethod. If you call this method from the class,
        for example, ``qusetta.Quasar``, than the output circuit type
        will be a ``quasar.Circuit`` object.

        Parameters
        ----------
        cls : one of the classes in ``qusetta.__all__``.
        circuit : cirq.Circuit object.

        Returns
        -------
        cls_circuit : cls.Circuit object.

        """
        return cls.from_qusetta(qs.Cirq.to_qusetta(circuit))

    @classmethod
    def to_cirq(cls, circuit: 'cls.Circuit') -> 'cirq.Circuit':
        """Create a cirq circuit from a ``cls`` circuit.

        This is a classmethod. If you call this method from the class,
        for example, ``qusetta.Quasar``, than the input circuit type
        will be a ``quasar.Circuit`` object.

        Parameters
        ----------
        cls : one of the classes in ``qusetta.__all__``.
        circuit : a cls object.

        Returns
        -------
        cirq_circuit : cirq.Circuit object.

        """
        return qs.Cirq.from_qusetta(cls.to_qusetta(circuit))

    @classmethod
    def from_qiskit(cls, circuit: 'qiskit.QuantumCircuit') -> 'cls.Circuit':
        """Create a ``cls`` circuit from a qiskit circuit.

        This is a classmethod. If you call this method from the class,
        for example, ``qusetta.Quasar``, than the output circuit type
        will be a ``quasar.Circuit`` object.

        Parameters
        ----------
        cls : one of the classes in ``qusetta.__all__``.
        circuit : qiskit.QuantumCircuit object.

        Returns
        -------
        cls_circuit : cls object.

        """
        return cls.from_qusetta(qs.Qiskit.to_qusetta(circuit))

    @classmethod
    def to_qiskit(cls, circuit: 'cls.Circuit') -> 'qiskit.QuantumCircuit':
        """Create a qiskit circuit from a ``cls`` circuit.

        This is a classmethod. If you call this method from the class,
        for example, ``qusetta.Quasar``, than the input circuit type
        will be a ``quasar.Circuit`` object.

        Parameters
        ----------
        cls : one of the classes in ``qusetta.__all__``.
        circuit : a cls object.

        Returns
        -------
        qiskit_circuit : qiskit.QuantumCircuit object.

        """
        return qs.Qiskit.from_qusetta(cls.to_qusetta(circuit))

    @classmethod
    def from_quasar(cls, circuit: 'quasar.Circuit') -> 'cls.Circuit':
        """Create a ``cls`` circuit from a quasar circuit.

        This is a classmethod. If you call this method from the class,
        for example, ``qusetta.Cirq``, than the output circuit type
        will be a ``cirq.Circuit`` object.

        Parameters
        ----------
        cls : one of the classes in ``qusetta.__all__``.
        circuit : quasar.Circuit object.

        Returns
        -------
        cls_circuit : cls object.

        """
        return cls.from_qusetta(qs.Quasar.to_qusetta(circuit))

    @classmethod
    def to_quasar(cls, circuit: 'cls.Circuit') -> 'quasar.Circuit':
        """Create a quasar circuit from a ``cls`` circuit.

        This is a classmethod. If you call this method from the class,
        for example, ``qusetta.Cirq``, than the input circuit type
        will be a ``cirq.Circuit`` object.

        Parameters
        ----------
        cls : one of the classes in ``qusetta.__all__``.
        circuit : a cls object.

        Returns
        -------
        quasar_circuit : quasar.Circuit object.

        """
        return qs.Quasar.from_qusetta(cls.to_qusetta(circuit))
