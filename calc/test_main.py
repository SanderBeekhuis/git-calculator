import calc


def test_add():
    assert calc.add(2, 3) == 5


def test_mult():
    assert calc.mult(2, 3) == 6
    assert calc.mult(2, 0) == 0
