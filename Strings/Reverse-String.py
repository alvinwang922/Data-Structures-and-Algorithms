"""
Write a function that reverses a string. The input string is 
given as an array of characters char[]. Do not allocate extra 
space for another array, you must do this by modifying the 
input array in-place with O(1) extra memory. You may assume 
all the characters consist of printable ascii characters.
"""


class Solution:
    def reverseString(self, s: List[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


print(reverseString(["h", "e", "l", "l", "o"]))
print(reverseString(["H", "a", "n", "n", "a", "h"]))
print(reverseString(["e", "e", "l", "e", "o"]))
print("The arrays above should be [\"o\",\"l\",\"l\",\"e\",\"h\"], \
    [\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"], \
        and [\"o\",\"e\",\"l\",\"e\",\"e\"].")
