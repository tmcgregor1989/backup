import unittest

from src.fizz_buzz import *

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_fizz(self):
        self.assertEqual("fizz", fizz_buzz(3))

    def test_fizz_buzz_buzz(self):
        self.assertEqual("buzz", fizz_buzz(10))

    def test_fizz_buzz_divisible_by_3_and_5(self):
        self.assertEqual("fizzbuzz", fizz_buzz(30))

    def test_fizz_buzz_not_divisible_by_3_or_5(self):
        self.assertEqual("7", fizz_buzz(7))

