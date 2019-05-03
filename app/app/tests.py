from django.test import TestCase

from app.calc import add, substract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test addition"""
        self.assertEqual(add(3, 8), 11)

    def test_bubstract_numbers(self):
        """Test substraction"""
        self.assertEqual(substract(5, 2), 3)
