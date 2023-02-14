# Tests functions for mastermind strings, input, and output.
# CSC 101, Project 3
# Given tests, Summer '22
# TODO: Complete this file.

import random
import unittest
import mastermind_io
import mastermind_strings


class TestMastermind(unittest.TestCase):
    def test01_parse_integer(self):
        integer = mastermind_io.parse_integer("1", 4)
        self.assertEqual(integer, 1)

    def test02_parse_character(self):
        character = mastermind_io.parse_character("ABC", "D")
        self.assertEqual(character, "A")

    def test03_parse_string(self):
        string = mastermind_io.parse_string("A B C.", 6)
        self.assertEqual(string, "ABC")

    def test04_random_string(self):
        random.seed(94)
        string = mastermind_strings.random_string("A", "F", 4)
        self.assertEqual(string, "EBAC")

    def test05_match_exactly(self):
        matches = mastermind_strings.match_exactly("ABCD", "CBDA")
        self.assertEqual(matches, 1)

    def test06_match_any(self):
        matches = mastermind_strings.match_any("ABCD", "CBDA")
        self.assertEqual(matches, 4)


if __name__ == "__main__":
    unittest.main()
