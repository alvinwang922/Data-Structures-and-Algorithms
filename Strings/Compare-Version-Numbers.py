"""
Given two version numbers, version1 and version2, compare them.
Version numbers consist of one or more revisions joined by a 
dot '.'. Each revision consists of digits and may contain 
leading zeros. Every revision contains at least one character. 
Revisions are 0-indexed from left to right, with the leftmost 
revision being revision 0, the next revision being revision 1, 
and so on. For example 2.5.33 and 0.1 are valid version numbers.
To compare version numbers, compare their revisions in 
left-to-right order. Revisions are compared using their integer 
value ignoring any leading zeros. This means that revisions 1 
and 001 are considered equal. If a version number does not 
specify a revision at an index, then treat the revision as 0. 
For example, version 1.0 is less than version 1.1 because their 
revision 0s are the same, but their revision 1s are 0 and 1 
respectively, and 0 < 1. Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
"""


class Solution:
    def compareVersion(self, version1: str, version2: str):
        one = version1.split(".")
        two = version2.split(".")
        l1, l2 = len(one), len(two)
        smaller, larger = min(l1, l2), max(l1, l2)
        for i in range(smaller):
            if int(one[i]) == int(two[i]):
                continue
            elif int(one[i]) > int(two[i]):
                return 1
            else:
                return -1
        if l1 > l2:
            for v in one[smaller:]:
                if int(v) != 0:
                    return 1
        elif l1 < l2:
            for v in two[smaller:]:
                if int(v) != 0:
                    return -1
        return 0

    print(compareVersion("1.01", "1.001"))
    print(compareVersion("1.0.1", "1"))
    print(compareVersion("7.5.2.4", "7.5.3"))
    print("The values above should be 0, 1, and -1.")
