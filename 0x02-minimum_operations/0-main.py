#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


n = 10
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 3
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))