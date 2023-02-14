# Defines functions for matching strings.
# CSC 101, Project 3
# Given code, Summer '22

import random


def random_string(start, stop, length):
    """
    Generate a string of random characters within a range.
    TODO: Debug this function.

    :param start: A smallest allowable character, inclusive
    :param stop: A largest allowable character, inclusive
    :param length: A desired number of characters
    :return: A string of random characters in that range, assuming that the
             smallest character is less than or equal to the largest
    """
    string = ""

    for i in range(length):
        string = string + chr(random.randint(65, ord(stop)))

    return string


def match_exactly(guess, answer):
    """
    Match a guess with an answer, respecting position.
    TODO: Debug this function.

    :param guess: An arbitrary guessed string
    :param answer: An arbitrary correct string
    :return: The number of characters in the guessed string that appear in the
             same position within the correct string
    """
    matches = 0

    for i in range(max(len(guess), len(answer))):
        if guess[i] == answer[i]:
            matches = matches + 1

    return matches


def match_any(guess, answer):
    """
    Match a guess with an answer, ignoring position.
    TODO: Debug this function.

    :param guess: An arbitrary guessed string
    :param answer: An arbitrary correct string
    :return: The number of characters that the guessed string and the correct
             string have in common
    """
    matches = 0

    for character in guess:
        if character in answer:
            matches = matches + 1

    return matches
