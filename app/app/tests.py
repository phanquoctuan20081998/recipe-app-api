"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the cals module."""

    def test_add_numvers(self):
        """Test adding numbvers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)


    def test_subtract_numbers(self):
        """Test subtractiong numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
