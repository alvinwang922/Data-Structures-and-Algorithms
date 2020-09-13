"""
Given a string of lowercase English letters and an integer of the substring length, 
determine the substring of that length that contains the most vowels. Vowels are in 
the set {a, e, i, o, u}. If there is more than one substring with the maximum number 
of vowels, return the one that starts at the lowest index. If there are no vowels in 
the input string, return the string "Not found!" without quotes.
"""


def findSubstring(s, k):
    # Write your code here
    start, currNum, maxNum = 0, 0, 0
    vowels = {"a", "e", "i", "o", "u"}
    for char in s[:k]:
        if char in vowels:
            currNum += 1
            maxNum += 1
    for i in range(1, len(s) - k):
        print(currNum)
        if s[i - 1] in vowels:
            currNum -= 1
        if s[i + k - 1] in vowels:
            currNum += 1
        if currNum > maxNum:
            maxNum = currNum
            start = i
    if currNum == 0:
        return "Not found!"
    return s[start:start + k]


print(findSubstring("azerdii", 5))
print(findSubstring("qwdftr", 2))
print(findSubstring("eiuaooo", 4))
print("The strings above should be \"erdii\", \"Not found!\", and \"eiua\".")
