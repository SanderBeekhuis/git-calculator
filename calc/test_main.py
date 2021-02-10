import pytest

import calc


def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(2, 3, 4) == 9
    assert calc.add(2) == 2


def test_mult():
    assert calc.mult(2, 3) == 6
    assert calc.mult(2, 0) == 0


def test_subtraction():
    assert calc.subtract(3, 1) == 2


@pytest.fixture
def names_dict():
    return {'Sander': 'Beekhuis'}


def test_has_sander(names_dict):
    assert 'Sandert' in names_dict


def test_has_no_remy(names_dict):
    assert 'Remy' not in names_dict
