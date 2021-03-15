"""
Given a non-empty array of digits representing a non-negative integer, 
increment one to the integer. The digits are stored such that the most 
significant digit is at the head of the list, and each element in the 
array contains a single digit. You may assume the integer does not 
contain any leading zero, except the number 0 itself.
"""


# Iterative solution
def plusOne(digits: List[int]):
    if digits[-1] == 9:
        tracker = len(digits) - 1
        while tracker >= 0 and digits[tracker] == 9:
            tracker -= 1
        if tracker == -1:
            return [1] + [0] * len(digits)
        else:
            digits[tracker] += 1
            return digits[:tracker + 1] + [0] * \
                (len(digits) - tracker - 1)
    digits[-1] += 1
    return digits


# Recursive solution
def plusOne2(digits: List[int]):
    if len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        digits[-1] = 0
        digits[:-1] = plusOne(digits[:-1])
        return digits


print(plusOne([4, 3, 2, 1]))
print(plusOne([8, 9, 9]))
print(plusOne([9]))
print("The arrays above should be [4, 3, 2, 2], [9, 0, 0], and [1, 0].")
