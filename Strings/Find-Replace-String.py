"""
To some string S, we will perform some replacement operations that 
replace groups of letters with new ones (not necessarily the same size).
Each replacement operation has 3 parameters: a starting index i, a 
source word x and a target word y.  The rule is that if x starts at 
position i in the original string S, then we will replace that 
occurrence of x with y.  If not, we do nothing. For example, if we have 
S = "abcd" and we have some replacement operation i = 2, x = "cd", 
y = "ffff", then because "cd" starts at position 2 in the original 
string S, we will replace it with "ffff". Using another example on 
S = "abcd", if we have both the replacement operation i = 0, 
x = "ab", y = "eee", as well as another replacement operation i = 2, 
x = "ec", y = "ffff", this second operation does nothing because in 
the original string S[2] = 'c', which doesn't match x[0] = 'e'.
All these operations occur simultaneously.  It's guaranteed that there 
won't be any overlap in replacement: for example, S = "abc", 
indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.
"""


class Solution:
    def findReplaceString(self, S: str, indexes: List[int],
                          sources: List[str], targets: List[str]):
        changes = []
        for i in range(len(indexes)):
            if S[indexes[i]:indexes[i] + len(sources[i])] == sources[i]:
                changes.append([indexes[i], sources[i], targets[i]])
        tracker, ans = 0, ""
        changes.sort()
        for i in range(len(changes)):
            while tracker < changes[i][0]:
                ans += S[tracker]
                tracker += 1
            ans += changes[i][2]
            tracker += len(changes[i][1])
        ans += S[tracker:]
        return ans


# Another solution
class Solution:
    def findReplaceString(self, S: str, indexes: List[int],
                          sources: List[str], targets: List[str]):
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S
        return S


print(findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))
print(findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]))
print(findReplaceString("abcd", [1, 2], ["a", "dd"], ["eee", "ffff"]))
print("The string above should be \"eeebffff\", \"eeecf\", and \"abcd\".")
