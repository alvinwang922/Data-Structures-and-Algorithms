"""
You are given an inclusive range [lower, upper] and a sorted unique integer 
array nums, where all elements are in the inclusive range. A number x is 
considered missing if x is in the range [lower, upper] and x is not in nums.
Return the smallest sorted list of ranges that cover every missing number 
exactly. That is, no element of nums is in any of the ranges, and each missing 
number is in one of the ranges.Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
"""


def findMissingRanges(nums: List[int], lower: int, upper: int):
    ans = []

    def helper(lower, upper):
        if lower == upper:
            return str(lower)
        else:
            return str(lower) + "->" + str(upper)
    if not nums:
        ans.append(helper(lower, upper))
        return ans
    if nums[0] > lower:
        ans.append(helper(lower, nums[0] - 1))
    for i in range(len(nums) - 1):
        if nums[i+1] > nums[i] + 1:
            ans.append(helper(nums[i] + 1, nums[i + 1] - 1))
    if nums[len(nums) - 1] < upper:
        ans.append(helper(nums[-1] + 1, upper))
    return ans


print(findMissingRanges([0, 1, 3, 50, 75], 0, 99))
print(findMissingRanges([], 1, 1))
print(findMissingRanges([], -3, -1))
print("The arrays above should be [\"2\",\"4 -> 49\",\"51 -> 74\",\
    \"76 -> 99\"], [\"1\"], and [\"-3 -> -1\"].")
