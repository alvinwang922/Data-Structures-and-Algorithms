"""
Given an array A of non-negative integers, return an 
array consisting of all the even elements of A, 
followed by all the odd elements of A. You may return 
any answer array that satisfies this condition.
"""


class Solution:
    def sortArrayByParity(self, A: List[int]):
        even, odd = 0, len(A) - 1
        while even < odd:
            while even < odd and A[even] % 2 == 0:
                even += 1
            while odd > even and A[odd] % 2 == 1:
                odd -= 1
            A[even], A[odd] = A[odd], A[even]
        return A

    print(sortArrayByParity([1, 2]))
    print(sortArrayByParity([3, 1, 2, 4]))
    print(sortArrayByParity([1, 3, 2, 5, 4, 6]))
    print("The arrays above should be [2, 1], [4, 2, 1, 3], \
        and [6, 4, 2, 5, 3, 1].")
