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

    def test02_parse_integer(self):
        integer = mastermind_io.parse_integer("152", 4)
        self.assertEqual(integer, 152)

    def test03_parse_integer(self):
        integer = mastermind_io.parse_integer("16", 4)
        self.assertEqual(integer, 16)

    def test04_parse_integer(self):
        integer = mastermind_io.parse_integer("0", 4)
        self.assertEqual(integer, 4)

    def test05_parse_integer(self):
        integer = mastermind_io.parse_integer("-3", 4)
        self.assertEqual(integer, 4)

    def test05_parse_integer(self):
        integer = mastermind_io.parse_integer("-3", 4)
        self.assertEqual(integer, 4)

    def test06_parse_integer(self):
        integer = mastermind_io.parse_integer("0",4)
        self.assertEqual(integer, 4)

    def test07_parse_integer(self):
        integer = mastermind_io.parse_integer("-1", 4)
        self.assertEqual(integer, 4)

    def test01_parse_character(self):
        character = mastermind_io.parse_character("ABC", "D")
        self.assertEqual(character, "A")

    def test02_parse_character(self):
        character = mastermind_io.parse_character("36ABC", "D")
        self.assertEqual(character, "A")

    def test03_parse_character(self):
        character = mastermind_io.parse_character(" ", "D")
        self.assertEqual(character, "D")

    def test03_parse_character(self):
        character = mastermind_io.parse_character("", "D")
        self.assertEqual(character, "D")

    def test04_parse_character(self):
        character = mastermind_io.parse_character("hello", "D")
        self.assertEqual(character, "H") 

    def test01_parse_string(self):
        string = mastermind_io.parse_string("A B C.", 6)
        self.assertEqual(string, "ABC")

    def test02_parse_string(self):
        string = mastermind_io.parse_string("abc4", 6)
        self.assertEqual(string, "ABC")

    def test03_parse_string(self):
        string = mastermind_io.parse_string("3 bc  d", 4)
        self.assertEqual(string, "BCD")

    def test04_parse_string(self):
        string = mastermind_io.parse_string("F, G, H, F, F", 4)
        self.assertEqual(string, "FGHF")

    def test01_random_string(self):
        random.seed(94)
        string = mastermind_strings.random_string("A", "F", 4)
        self.assertEqual(string, "EBAC")

    def test02_random_string(self):
        random.seed(96)
        string = mastermind_strings.random_string("E", "F", 4)
        self.assertEqual(string, "FFFE")

    def test03_random_string(self):
        random.seed(9)
        string = mastermind_strings.random_string("S", "T", 4)
        self.assertEqual(string, "TTTS")

    def test01_match_exactly(self):
        matches = mastermind_strings.match_exactly("ABCD", "CBDA")
        self.assertEqual(matches, 1)

    def test02_match_exactly(self):
        matches = mastermind_strings.match_exactly("A  BCD", "CBDA")
        self.assertEqual(matches, 0)

    def test03_match_exactly(self):
        matches = mastermind_strings.match_exactly("ACR", "CBDADD")
        self.assertEqual(matches, 0)

    def test01_match_any(self):
        matches = mastermind_strings.match_any("ABCD", "CBDA")
        self.assertEqual(matches, 4)

    def test02_match_any(self):
        matches = mastermind_strings.match_any("ACD", "CBADD")
        self.assertEqual(matches, 3)

    def test03_match_any(self):
        matches = mastermind_strings.match_any("AABB", "EBAC")
        self.assertEqual(matches, 2)

    def test04_match_any(self):
        matches = mastermind_strings.match_any("AA", "AB")
        self.assertEqual(matches, 1)

    def test05_match_any(self):
        matches = mastermind_strings.match_any("FGHF", "HFFG")
        self.assertEqual(matches, 4)

    def test06_match_any(self):
        matches = mastermind_strings.match_any("FG", "HFFG")
        self.assertEqual(matches, 2)


if __name__ == "__main__":
    unittest.main()
