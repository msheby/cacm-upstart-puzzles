#!/usr/bin/env python
# coding=UTF-8
from __future__ import print_function
import fractions

NUM_TIME_SEQUENCES = 24 * 4

# as provided in the puzzle, this should have an average duration of
# "slightly less than 8.6 seconds"
TEST_CHIMING_SEQUENCES = [
    [1, 0, 1],
    [1, 0, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
]


def get_chiming_sequence(n=0, b=10):
    """
    Given a radix *n* and a base *b*,
    create a list containing *n* expressed in base-*b*.
    If the least-significant digit would be zero or
    if there would be two consecutive zeroes,
    return None as it is not a valid chiming sequence.
    Otherwise, return the list.

    Parameters
    ----------
    n : int (default 0)
        A nonnegative integer.
    b : int (default 10)
        A nonnegative integer radix.
    """
    number = int(n)
    if number < 0:
        raise ValueError
    base = int(b)
    if base < 1:
        raise ValueError
    if base == 1:
        return [1 for _ in range(number)]
    else:
        saw_zero = True
        representation = []
        while number:
            digit = number % base
            if digit == 0:
                if saw_zero:
                    return None
                saw_zero = True
            else:
                saw_zero = False
            representation.append(digit)
            number //= base
    return representation[::-1]


def get_duration(chiming_sequence):
    """Given a chiming sequence, return its duration in seconds."""
    duration = 0
    saw_nonzero = False
    for digit in chiming_sequence:
        if digit != 0:
            duration += 1
            saw_nonzero = True
        else:
            if saw_nonzero:
                duration += 1
            saw_nonzero = False
    return duration


def get_minimum_average_duration_sequences(k=1):
    """
    Find a minimum average duration uniquely decodable code
    assuming there can be *k* different tones of bells in every cathedral.

    Parameters
    ----------
    k : int (default 1)
        Number of different tones in every cathedral.
    """
    base = int(k) + 1
    if base < 1:
        raise ValueError
    chiming_sequences = []
    start = 0
    if base == 1:
        # special case; return the unary sequences
        end = NUM_TIME_SEQUENCES + 1
        chiming_sequences.extend([chiming_sequence for chiming_sequence in
                                  [get_chiming_sequence(n, base)
                                   for n in range(start, end)]
                                  if chiming_sequence])
    else:
        end = 1
        while len(chiming_sequences) < NUM_TIME_SEQUENCES:
            chiming_sequences.extend([chiming_sequence for chiming_sequence in
                                      [get_chiming_sequence(n, base)
                                       for n in range(start, end)]
                                      if chiming_sequence])
            start = end
            end *= base
    return chiming_sequences[:NUM_TIME_SEQUENCES]


def get_average_duration(chiming_sequences=None):
    """
    Given a list of chiming sequences,
    return their average duration in seconds.

    >>> get_average_duration(TEST_CHIMING_SEQUENCES)
    Fraction(103, 12)
    """
    if chiming_sequences is None:
        chiming_sequences = []
    return fractions.Fraction(sum(map(get_duration, chiming_sequences)),
                              NUM_TIME_SEQUENCES)


def upstart_202005():
    """Solve the optimal chimes' upstart puzzles."""
    solution = []
    for k in range(NUM_TIME_SEQUENCES + 1):
        chiming_sequences = get_minimum_average_duration_sequences(k)
        average_duration = get_average_duration(chiming_sequences)
        solution.append({"k": k,
                         "minimum_average_duration": {
                             "numerator": average_duration.numerator,
                             "denominator": average_duration.denominator},
                         "chiming_sequences": chiming_sequences})
    return solution


def main():
    solution = upstart_202005()
    print("k\tminimum_average_duration_in_seconds")
    for d in solution:
        print("{0}\t{1}"
              .format(d["k"],
                      1.0 *
                      d["minimum_average_duration"]["numerator"] /
                      d["minimum_average_duration"]["denominator"]))
    # import json
    # print(json.dumps(solution, sort_keys=True, separators=(',', ':')))


if __name__ == "__main__":
    main()
