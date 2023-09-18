import calc


def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(2, 3, 4) == 9
    assert calc.add(2) == 2


def test_mult():
    assert calc.mult(2, 3) == 6
    assert calc.mult(2, 0) == 0
    assert calc.mult(2, 3, 4) == 24
    assert calc.mult(2) == 2


def test_subtraction():
    assert calc.subtract(3, 1) == 2
