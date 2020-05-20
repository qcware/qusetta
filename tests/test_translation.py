"""Test the translation functionality.

"""

import cirq
import qiskit
import quasar
import qusetta as qu
from math import pi


def qu_circuit():
    return [
        "H(0)", "H(1)", "CX(0, 1)", "CX(1, 0)", "CZ(2, 0)",
        "I(1)", "SWAP(0, 3)", "RY(PI)(1)", "X(2)", "S(0)",
        "Z(2)", "Y(3)", "RX(0.4*PI)(0)", "T(2)", "RZ(-0.3*PI)(2)"
    ]


def cirq_circuit():
    c = cirq.Circuit()
    q = [cirq.LineQubit(i) for i in range(4)]
    c.append(cirq.H(q[0]))
    c.append(cirq.H(q[1]))
    c.append(cirq.CX(q[0], q[1]))
    c.append(cirq.CX(q[1], q[0]))
    c.append(cirq.CZ(q[2], q[0]))
    c.append(cirq.I(q[1]))
    c.append(cirq.SWAP(q[0], q[3]))
    c.append(cirq.ry(pi)(q[1]))
    c.append(cirq.X(q[2]))
    c.append(cirq.S(q[0]))
    c.append(cirq.Z(q[2]))
    c.append(cirq.Y(q[3]))
    c.append(cirq.rx(.4*pi)(q[0]))
    c.append(cirq.T(q[2]))
    c.append(cirq.rz(-.3*pi)(q[2]))
    return c


def qiskit_circuit():
    c = qiskit.QuantumCircuit()
    c.h(0)
    c.h(1)
    c.cx(0, 1)
    c.cx(1, 0)
    c.cz(2, 0)
    c.i(1)
    c.swap(0, 3)
    c.ry(pi, 1)
    c.x(2)
    c.s(0)
    c.z(2)
    c.y(3)
    c.rx(.4*pi, 0)
    c.t(2)
    c.rz(-.3*pi, 2)
    return c


def quasar_circuit():
    c = quasar.Circuit()
    c.H(0)
    c.H(1)
    c.CX(0, 1)
    c.CX(1, 0)
    c.CZ(2, 0)
    c.I(1)
    c.SWAP(0, 3)
    c.Ry(1, pi)
    c.X(2)
    c.S(0)
    c.Z(2)
    c.Y(3)
    c.Rx(0, .2*pi)
    c.T(2)
    c.Rz(2, -.15*pi)
    return c


def test_cirq_vs_qusetta():
    c, q = cirq_circuit(), qu_circuit()
    assert qu.Cirq.from_qusetta(q) == c
    assert qu.Cirq.to_qusetta(c) == q

    sim = cirq.Simulator()
    assert sim.simulate(c) == sim.simulate(qu.Cirq.from_qusetta(q))


def test_qiskit_vs_qusetta():
    return
    c, q = qiskit_circuit(), qu_circuit()
    assert qu.Qiskit.from_qusetta(q) == c
    assert qu.Qiskit.to_qusetta(c) == q


def test_cirq_vs_qiskit():
    return
    c, q = cirq_circuit(), qiskit_circuit()
    assert qu.Cirq.from_qiskit(q) == c
    assert qu.Qiskit.to_cirq(q) == c
    assert qu.Cirq.to_qiskit(c) == q
    assert qu.Qiskit.from_cirq(c) == q

    sim = cirq.Simulator()
    assert sim.simulate(c) == sim.simulate(qu.Cirq.from_qiskit(q))
