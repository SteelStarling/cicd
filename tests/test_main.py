"""
Test the main module.
Author: Taylor Hancock
"""

from unittest import TestCase
from main import check_distance, distance_string


class Test(TestCase):
    def test_check_distance(self):
        assert check_distance(42) == 0      # handles correct number
        assert check_distance(0) == 42      # handles smaller numbers
        assert check_distance(100) == 58    # handles larger numbers
        assert check_distance(-42) == 84    # handles negatives

    def test_distance_string(self):
        assert distance_string("42") == "42 is The Answer!"                         # handles correct number
        assert distance_string("0") == "0 is 42 away from The Correct Answer"       # handles smaller numbers
        assert distance_string("100") == "100 is 58 away from The Correct Answer"   # handles larger numbers
        assert distance_string("-42") == "-42 is 84 away from The Correct Answer"   # handles negatives
        assert distance_string("A") == "Not a Number"                               # handles non-numbers
        assert distance_string("") == "Not a Number"                                # handles empty string
        assert distance_string("", "Error") == "Error"                              # handles custom error message
