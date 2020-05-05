# Given a string, find the first non-repeating character in it
# and return it's index. If it doesn't exist, return -1.
# Note: You may assume the string contain only lowercase letters.


class Solution(object):
    def firstUniqChar(self, s):
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0
        letters = []
        for char in s:
            letters.append(char)
        letters = sorted(letters)
        unique = []
        minIndex = float("inf")
        for i in range(len(letters) - 1):
            if letters[i] != letters[i - 1] and letters[i] != letters[i + 1]:
                unique.append(letters[i])
        if len(letters) > 1 and letters[len(letters)-1] != letters[len(letters)-2]:
            unique.append(letters[len(letters)-1])
        if len(unique) == 0:
            return -1
        for letter in unique:
            minIndex = min(minIndex, s.find(letter))
        return minIndex


print(firstUniqChar("haha"))
print(firstUniqChar("beebo"))
print(firstUniqChar("ilovecoding"))
print("The values above should be -1, 4, and 1.")
