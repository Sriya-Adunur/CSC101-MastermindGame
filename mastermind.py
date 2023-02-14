# Plays codemaker in a game of mastermind.
# CSC 101, Project 3
# Given code, Summer '22
# NOTE: Do not alter this file.

import random
import mastermind_io
import mastermind_strings


def main():
    start = input("Enter the minimum character: ")
    start = mastermind_io.parse_character(start, "A")
    stop = input("Enter the maximum character: ")
    stop = mastermind_io.parse_character(stop, "F")

    start, stop = min(start, stop), max(start, stop)

    length = input("Enter the number of characters: ")
    length = mastermind_io.parse_integer(length, 4)
    turns = input("Enter the number of turns: ")
    turns = mastermind_io.parse_integer(turns, 12)

    seed = input("Enter the seed: ")
    seed = mastermind_io.parse_integer(seed, None)
    random.seed(seed)

    answer = mastermind_strings.random_string(start, stop, length)

    while turns > 0:
        guess = input("\nEnter a guess (%d characters between '%c' and '%c'): "
                      % (length, start, stop))
        guess = mastermind_io.parse_string(guess, length)
        exact = mastermind_strings.match_exactly(guess, answer)
        total = mastermind_strings.match_any(guess, answer)

        print("The guess \"%s\" contains %d exact and %d inexact matches."
              % (guess, exact, total - exact))

        if exact == length:
            turns = 0
            print("You win!")
        elif turns == 1:
            turns = 0
            print("You lose! The answer was \"%s\"." % answer)
        else:
            turns = turns - 1
            print("You have %d guesses left." % turns)


if __name__ == "__main__":
    main()
