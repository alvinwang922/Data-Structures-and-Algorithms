"""
The count-and-say sequence is a sequence of digit strings defined 
by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from 
countAndSay(n-1), which is then converted into a different digit 
string. To determine how you "say" a digit string, split it into 
the minimal number of groups so that each group is a contiguous 
section all of the same character. Then for each group, say the 
number of characters, then say the character. To convert the 
saying into a digit string, replace the counts with a number 
and concatenate every saying.
"""


class Solution:
    def countAndSay(self, n: int):
        ans = "1"
        for _ in range(n - 1):
            tracker = ans
            ans = ""
            i = 0
            while i < len(tracker):
                curr = tracker[i]
                count = 1
                i += 1
                while i < len(tracker) and tracker[i] == curr:
                    count += 1
                    i += 1
                ans += str(count) + str(curr)
        return ans


print(countAndSay(1))
print(countAndSay(4))
print(countAndSay(6))
print("The strings above should be \"1\", \"1211\", and \"312211\".")