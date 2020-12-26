"""
Given an array arr of integers, check if there 
exists two integers N and M such that N is the 
double of M ( i.e. N = 2 * M).
More formally check if there exists two indices 
i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
"""


from collections import Counter


class Solution:
    def checkIfExist(self, arr: List[int]):
        c = Counter(arr)
        if c[0] >= 2:
            return True
        for num in arr:
            if c[num * 2] and num != 0:
                return True
        return False

    print(checkIfExist([10, 2, 5, 3]))
    print(checkIfExist([3, 1, 7, 11]))
    print(checkIfExist([7, 1, 14, 11]))
    print("The booleans above should be True, False, and True.")
