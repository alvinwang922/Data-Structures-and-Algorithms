"""
Given two arrays A and B of length N, determine if there
is a way to make A equal to B by reversing any subarrays
from array B any number of times.
"""


def are_they_equal(array_a, array_b):
    if array_a == array_b:
        return True
    if len(array_a) != len(array_b):
        return False
    for i in range(len(array_a)):
        for j in range(i, len(array_b)):
            if array_a[i] == array_b[j]:
                if array_a[:i] + array_a[i:j + 1][::-1] \
                        + array_a[j + 1:] == array_b:
                    return True
    return False


print(are_they_equal([1, 2, 3, 4], [1, 4, 3, 2]))
print(are_they_equal([1, 2, 3, 4], [1, 2, 3, 5]))
print("The booleans above should be True and False.")
