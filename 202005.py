#!/usr/bin/env python
# coding=UTF-8
from __future__ import print_function
import fractions

NUM_TIME_SEQUENCES = 24 * 4


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
    saw_zero = False
    representation = []
    if number == 0:
        representation.append(0)
        saw_zero = True
    elif base == 1:
        representation.extend([1 for _ in range(number)])
    else:
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
    if representation[0] == 0:
        return None
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
        Number of different tones in the bell towers.
    """
    base = int(k) + 1
    if base < 2:
        raise ValueError
    ndigits = 0
    chiming_sequences = []
    while len(chiming_sequences) < NUM_TIME_SEQUENCES:
        ndigits += 1
        maximum = base ** ndigits
        if maximum < NUM_TIME_SEQUENCES:
            # don't waste time
            continue
        chiming_sequences = [chiming_sequence for chiming_sequence in
                             [get_chiming_sequence(n, base)
                              for n in range(maximum)]
                             if chiming_sequence]
    return chiming_sequences[:NUM_TIME_SEQUENCES]


def get_average_duration(sequences=None):
    """
    Given a list of chiming sequences,
    return their average duration in seconds.
    """
    return fractions.Fraction(sum(map(get_duration, sequences)),
                              NUM_TIME_SEQUENCES)


def upstart_202005():
    """Solve the optimal chimes' upstart puzzles."""
    solution = []
    for k in range(1, NUM_TIME_SEQUENCES + 1):
        sequences = get_minimum_average_duration_sequences(k)
        duration = get_average_duration(sequences)
        solution.append({"k": k,
                         "minimum_average_duration": {
                             "numerator": duration.numerator,
                             "denominator": duration.denominator},
                         "chiming_sequences": sequences})
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
