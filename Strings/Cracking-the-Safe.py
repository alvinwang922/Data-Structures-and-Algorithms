"""
There is a box protected by a password. The password is a 
sequence of n digits where each digit can be one of the 
first k digits 0, 1, ..., k-1. While entering a password, 
the last n digits entered will automatically be matched 
against the correct password. For example, assuming the 
correct password is "345", if you type "012345", the box 
will open because the correct password matches the suffix 
of the entered password. Return any password of minimum 
length that is guaranteed to open the box at some point 
of entering it.
"""


class Solution:
    def crackSafe(self, n: int, k: int):
        ans = "0" * (n - 1)
        visited = set()
        for x in range(k ** n):
            curr = ans[-n + 1:] if n > 1 else ""
            for y in range(k - 1, -1, -1):
                if curr + str(y) not in visited:
                    visited.add(curr + str(y))
                    ans += str(y)
                    break
        return ans

    print(crackSafe(1, 2))
    print(crackSafe(2, 2))
    print(crackSafe(3, 3))
    print("The strings above should be \"01\", \"01100\", \
        and \"00222122021121020120011101000\".")
