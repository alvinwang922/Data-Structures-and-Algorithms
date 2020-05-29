"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the 
encoded_string inside the square brackets is being 
repeated exactly k times. Note that k is guaranteed 
to be a positive integer. You may assume that the 
input string is always valid; No extra white spaces, 
square brackets are well-formed, etc. Furthermore, 
you may assume that the original data does not 
contain any digits and that digits are only for 
those repeat numbers, k. For example, there won't 
be input like 3a or 2[4].
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curNum = 0
        curString = ''
        for char in s:
            if char == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif char == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif char.isdigit():
                curNum = curNum*10 + int(char)
            else:
                curString += char
        return curString


print(decodeString("3[a]2[bc]"))
print(decodeString("3[a2[c]]"))
print(decodeString("2[abc]3[cd]ef"))
print("The strings above should be \"aaabcbc\", \
\"accaccacc\", and \"abcabccdcdcdef\".")
