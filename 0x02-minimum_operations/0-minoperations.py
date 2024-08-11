#!/usr/bin/python3

"""" , there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewestnumber
of operations needed to result in exactly n H characters"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters
    """
    operations = 2
    divisor = 0
    lmc = 0
    for i in range(2, 10):
        if n % i == 0:
            divisor = i
            if lmc < divisor:
                lmc = divisor

    #print(f"lmc = {lmc}")
    if lmc == 0:
        return 0

    intial_steps = lmc - 2
    operations += intial_steps

    if lmc != 0:
        remaining_steps = n / lmc

    operations = operations + remaining_steps

    return int(operations - 1)
