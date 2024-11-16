class Calculator:
    def add(self, x, y): return x + y

import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self): self.assertEqual(Calculator().add(2, 3), 5)
