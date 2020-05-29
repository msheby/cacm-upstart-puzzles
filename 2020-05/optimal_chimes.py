#!/usr/bin/env python
# coding=UTF-8

"""
Find a solution for
<https://cacm.acm.org/magazines/2020/5/244323-optimal-chimes>.
"""

from __future__ import print_function
import itertools
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
    n = 1
    while True:
        if base == 1:
            yield [1 for _ in range(n)]
        else:
            saw_zero = True
            number = n
            representation = []
            while number:
                digit = number % base
                if digit == 0:
                    if saw_zero:
                        n += 1
                        number = n
                        del representation[:]
                        continue
                    saw_zero = True
                else:
                    saw_zero = False
                representation.append(digit)
                number //= base
            representation.reverse()
            yield representation
        n += 1


def get_average_duration(chiming_sequences):
    """
    Given a list of chiming sequences,
    return their average duration in seconds.

    >>> get_average_duration(TEST_CHIMING_SEQUENCES)
    Fraction(103, 12)
    """
    return fractions.Fraction(sum(map(len, chiming_sequences)),
                              len(chiming_sequences))


def upstart_202005():
    """
    Solve the optimal chimes' upstart puzzles.

    >>> get_average_duration(get_minimum_average_duration_sequences(0))
    Fraction(97, 2)
    >>> get_average_duration(get_minimum_average_duration_sequences(96))
    Fraction(1, 1)
    """
    solution = []
    for k in range(NUM_TIME_SEQUENCES + 1):
        chiming_sequences = tuple(itertools.islice(
            get_minimum_average_duration_sequences(k),
            NUM_TIME_SEQUENCES))
        average_duration = get_average_duration(chiming_sequences)
        solution.append({"chiming_sequences": chiming_sequences,
                         "k": k,
                         "minimum_average_duration": {
                             "denominator": average_duration.denominator,
                             "numerator": average_duration.numerator}})
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
