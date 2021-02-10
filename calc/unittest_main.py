import unittest

import calc


class CalcTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(2, 3, 4), 9)
        self.assertEqual(calc.add(2), 2)

    def test_mult(self):
        self.assertEqual(calc.mult(2, 3), 6)
        self.assertEqual(calc.mult(2, 0), 0)

    def test_subtraction(self):
        self.assertEqual(calc.subtract(3, 1), 2)


class FixtureTest(unittest.TestCase):
    def setUp(self):
        self.names_dict = {'Sander': 'Beekhuis'}

    def test_has_sander(self):
        self.assertIn('Sandert', self.names_dict)

    def test_has_no_remy(self):
        self.assertNotIn('Remy', self.names_dict)
