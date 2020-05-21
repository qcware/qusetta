"""Test gate info."""

from qusetta import gate_info
from math import pi


def test_gate_info():
    assert gate_info("H(0)") == ("H", (), (0,))
    assert gate_info("CX(0, 1)") == ("CX", (), (0, 1))
    assert gate_info("RX(1.2)(3)") == ("RX", (1.2,), (3,))
    assert gate_info("RY(PI/2)(2)") == ("RY", (pi/2,), (2,))
