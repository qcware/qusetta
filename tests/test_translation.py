"""Test the translation functionality.

Phases and exact gates may be different in the circuit, but the
resulting probability distribution is the same; that's all we care about.

"""

import cirq
import qiskit
import quasar
import qusetta as qs
from math import pi
import numpy as np
import random


class Simulator:

    cirq_backend = cirq.Simulator(dtype=np.complex128)
    qiskit_backend = qiskit.BasicAer.get_backend('statevector_simulator')
    quasar_backend = quasar.QuasarSimulatorBackend()

    @staticmethod
    def cirq(circuit: cirq.Circuit) -> np.ndarray:
        return Simulator.cirq_backend.simulate(circuit).final_state

    @staticmethod
    def qiskit(circuit: qiskit.QuantumCircuit) -> np.ndarray:
        return qiskit.execute(
            circuit, Simulator.qiskit_backend
        ).result().get_statevector()

    @staticmethod
    def quasar(circuit: quasar.Circuit) -> np.ndarray:
        return Simulator.quasar_backend.run_statevector(circuit)


def assert_equal(c0, c1, simulator0, simulator1=None):
    simulator1 = simulator1 or simulator0
    np.testing.assert_allclose(
        np.abs(simulator0(c0)) ** 2,
        np.abs(simulator1(c1)) ** 2
    )


# begin test functions that work on arbitrary circuits


def cirq_vs_qusetta(cirq_circuit, qusetta_circuit):
    assert_equal(
        cirq_circuit,
        qs.Cirq.from_qusetta(qusetta_circuit),
        Simulator.cirq
    )
    assert_equal(
        cirq_circuit,
        qs.Cirq.from_qusetta(qs.Cirq.to_qusetta(cirq_circuit)),
        Simulator.cirq
    )


def qiskit_vs_qusetta(qiskit_circuit, qusetta_circuit):
    assert_equal(
        qiskit_circuit,
        qs.Qiskit.from_qusetta(qusetta_circuit),
        Simulator.qiskit
    )
    assert_equal(
        qiskit_circuit,
        qs.Qiskit.from_qusetta(qs.Qiskit.to_qusetta(qiskit_circuit)),
        Simulator.qiskit
    )


def quasar_vs_qusetta(quasar_circuit, qusetta_circuit):
    assert_equal(
        quasar_circuit,
        qs.Quasar.from_qusetta(qusetta_circuit),
        Simulator.quasar
    )
    assert_equal(
        quasar_circuit,
        qs.Quasar.from_qusetta(qs.Quasar.to_qusetta(quasar_circuit)),
        Simulator.quasar
    )


def cirq_vs_qiskit(cirq_circuit, qiskit_circuit):
    assert_equal(
        cirq_circuit,
        qiskit_circuit,
        Simulator.cirq,
        Simulator.qiskit
    )
    assert_equal(
        cirq_circuit,
        qs.Qiskit.to_cirq(qiskit_circuit),
        Simulator.cirq
    )
    assert_equal(
        cirq_circuit,
        qs.Cirq.from_qiskit(qiskit_circuit),
        Simulator.cirq
    )
    assert_equal(
        qs.Qiskit.from_cirq(cirq_circuit),
        qiskit_circuit,
        Simulator.qiskit
    )
    assert_equal(
        qs.Cirq.to_qiskit(cirq_circuit),
        qiskit_circuit,
        Simulator.qiskit
    )
    assert_equal(
        qiskit_circuit,
        qs.Qiskit.from_cirq(qs.Qiskit.to_cirq(qiskit_circuit)),
        Simulator.qiskit
    )
    assert_equal(
        cirq_circuit,
        qs.Cirq.from_qiskit(qs.Cirq.to_qiskit(cirq_circuit)),
        Simulator.cirq
    )


def cirq_vs_quasar(cirq_circuit, quasar_circuit):
    assert_equal(
        cirq_circuit,
        quasar_circuit,
        Simulator.cirq,
        Simulator.quasar
    )
    assert_equal(
        cirq_circuit,
        qs.Quasar.to_cirq(quasar_circuit),
        Simulator.cirq
    )
    assert_equal(
        cirq_circuit,
        qs.Cirq.from_quasar(quasar_circuit),
        Simulator.cirq
    )
    assert_equal(
        qs.Quasar.from_cirq(cirq_circuit),
        quasar_circuit,
        Simulator.quasar
    )
    assert_equal(
        qs.Cirq.to_quasar(cirq_circuit),
        quasar_circuit,
        Simulator.quasar
    )
    assert_equal(
        quasar_circuit,
        qs.Quasar.from_cirq(qs.Quasar.to_cirq(quasar_circuit)),
        Simulator.quasar
    )
    assert_equal(
        cirq_circuit,
        qs.Cirq.from_quasar(qs.Cirq.to_quasar(cirq_circuit)),
        Simulator.cirq
    )


def qiskit_vs_quasar(qiskit_circuit, quasar_circuit):
    assert_equal(
        qiskit_circuit,
        quasar_circuit,
        Simulator.qiskit,
        Simulator.quasar
    )
    assert_equal(
        qiskit_circuit,
        qs.Quasar.to_qiskit(quasar_circuit),
        Simulator.qiskit
    )
    assert_equal(
        qiskit_circuit,
        qs.Qiskit.from_quasar(quasar_circuit),
        Simulator.qiskit
    )
    assert_equal(
        qs.Quasar.from_qiskit(qiskit_circuit),
        quasar_circuit,
        Simulator.quasar
    )
    assert_equal(
        qs.Qiskit.to_quasar(qiskit_circuit),
        quasar_circuit,
        Simulator.quasar
    )
    assert_equal(
        quasar_circuit,
        qs.Quasar.from_qiskit(qs.Quasar.to_qiskit(quasar_circuit)),
        Simulator.quasar
    )
    assert_equal(
        qiskit_circuit,
        qs.Qiskit.from_quasar(qs.Qiskit.to_quasar(qiskit_circuit)),
        Simulator.qiskit
    )


# begin explicit tests with explicit circuits

def all_tests(qusetta_circuit, cirq_circuit, qiskit_circuit, quasar_circuit):
    cirq_vs_qusetta(cirq_circuit, qusetta_circuit)
    qiskit_vs_qusetta(qiskit_circuit, qusetta_circuit)
    quasar_vs_qusetta(quasar_circuit, qusetta_circuit)
    cirq_vs_qiskit(cirq_circuit, qiskit_circuit)
    cirq_vs_quasar(cirq_circuit, quasar_circuit)
    qiskit_vs_quasar(qiskit_circuit, quasar_circuit)


def test_circuit_0():
    qusetta_circuit = [
        "H(0)", "H(1)", "CX(0, 1)", "CX(1, 0)", "CZ(2, 0)",
        "I(1)", "SWAP(0, 3)", "RY(PI)(1)", "X(2)", "S(0)",
        "Z(2)", "Y(3)", "RX(0.4*PI)(0)", "T(2)", "RZ(-0.3*PI)(2)",
        "CCX(0, 1, 2)"
    ]

    cirq_circuit = cirq.Circuit()
    q = [cirq.LineQubit(i) for i in range(4)]
    cirq_circuit.append(cirq.H(q[0]))
    cirq_circuit.append(cirq.H(q[1]))
    cirq_circuit.append(cirq.CX(q[0], q[1]))
    cirq_circuit.append(cirq.CX(q[1], q[0]))
    cirq_circuit.append(cirq.CZ(q[2], q[0]))
    cirq_circuit.append(cirq.I(q[1]))
    cirq_circuit.append(cirq.SWAP(q[0], q[3]))
    cirq_circuit.append(cirq.ry(pi)(q[1]))
    cirq_circuit.append(cirq.X(q[2]))
    cirq_circuit.append(cirq.S(q[0]))
    cirq_circuit.append(cirq.Z(q[2]))
    cirq_circuit.append(cirq.Y(q[3]))
    cirq_circuit.append(cirq.rx(.4*pi)(q[0]))
    cirq_circuit.append(cirq.T(q[2]))
    cirq_circuit.append(cirq.rz(-.3*pi)(q[2]))
    cirq_circuit.append(cirq.CCX(q[0], q[1], q[2]))

    # ibm is weird so we flip all of the qubits here
    qiskit_circuit = qiskit.QuantumCircuit(4)
    qiskit_circuit.h(3-0)
    qiskit_circuit.h(3-1)
    qiskit_circuit.cx(3-0, 3-1)
    qiskit_circuit.cx(3-1, 3-0)
    qiskit_circuit.cz(3-2, 3-0)
    qiskit_circuit.i(3-1)
    qiskit_circuit.swap(3-0, 3-3)
    qiskit_circuit.ry(pi, 3-1)
    qiskit_circuit.x(3-2)
    qiskit_circuit.s(3-0)
    qiskit_circuit.z(3-2)
    qiskit_circuit.y(3-3)
    qiskit_circuit.rx(.4*pi, 3-0)
    qiskit_circuit.t(3-2)
    qiskit_circuit.rz(-.3*pi, 3-2)
    qiskit_circuit.ccx(3-0, 3-1, 3-2)

    quasar_circuit = quasar.Circuit()
    quasar_circuit.H(0)
    quasar_circuit.H(1)
    quasar_circuit.CX(0, 1)
    quasar_circuit.CX(1, 0)
    quasar_circuit.CZ(2, 0)
    quasar_circuit.I(1)
    quasar_circuit.SWAP(0, 3)
    quasar_circuit.Ry(1, pi)
    quasar_circuit.X(2)
    quasar_circuit.S(0)
    quasar_circuit.Z(2)
    quasar_circuit.Y(3)
    quasar_circuit.Rx(0, .2*pi)
    quasar_circuit.T(2)
    quasar_circuit.Rz(2, -.15*pi)
    quasar_circuit.CCX(0, 1, 2)

    # tests
    all_tests(qusetta_circuit, cirq_circuit, qiskit_circuit, quasar_circuit)


def test_circuit_1():
    # test qiskit's u1, u2, and u3 gates

    qiskit_circuit = qiskit.QuantumCircuit(4)
    qiskit_circuit.h(0)
    qiskit_circuit.h(2)
    qiskit_circuit.u1(pi/6, 1)
    qiskit_circuit.u2(1, 2, 0)
    qiskit_circuit.ccx(1, 0, 3)
    qiskit_circuit.ccx(0, 1, 2)
    qiskit_circuit.u3(1, 2, 3, 1)
    qiskit_circuit.rx(pi/3, 1)
    qiskit_circuit.u3(1.56, 1.24, 1.69, 2)
    qiskit_circuit.u2(1.2, 5.1, 1)
    qiskit_circuit.u1(6.542, 0)

    qusetta_circuit = qs.Qiskit.to_qusetta(qiskit_circuit)
    cirq_circuit = qs.Cirq.from_qusetta(qusetta_circuit)
    quasar_circuit = qs.Quasar.from_qusetta(qusetta_circuit)

    # tests
    all_tests(qusetta_circuit, cirq_circuit, qiskit_circuit, quasar_circuit)


def test_circuit_2():
    # test that we ignore measurement gates

    qusetta_circuit = ["H(0)"]

    q = cirq.LineQubit(0)
    cirq_circuit = cirq.Circuit(cirq.H(q), cirq.measure(q))
    cirq_circuit = qs.Cirq.from_qusetta(qs.Cirq.to_qusetta(cirq_circuit))

    qiskit_circuit = qiskit.QuantumCircuit(1, 1)
    qiskit_circuit.h(0)
    qiskit_circuit.measure(0, 0)
    qiskit_circuit = qs.Qiskit.from_qusetta(
        qs.Qiskit.to_qusetta(qiskit_circuit)
    )

    quasar_circuit = quasar.Circuit()
    quasar_circuit.H(0)
    quasar_circuit = qs.Quasar.from_qusetta(
        qs.Quasar.to_qusetta(quasar_circuit)
    )

    # tests
    all_tests(qusetta_circuit, cirq_circuit, qiskit_circuit, quasar_circuit)
