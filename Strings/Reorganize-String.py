"""
Given a string S, check if the letters can be rearranged so that 
two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return 
the empty string.
"""


class Solution:
    def reorganizeString(self, S: str):
        counter = Counter(S)
        i, ans = 0, [None] * len(S)
        for j in sorted(counter, key=counter.get, reverse=True):
            if counter[j] > (len(S) // 2) + (len(S) % 2):
                return ""
            for _ in range(counter[j]):
                if i >= len(S):
                    i = 1
                ans[i] = j
                i += 2
        return "".join(ans)


print(reorganizeString("aab"))
print(reorganizeString("aaab"))
print(reorganizeString("aabbbc"))
print("The strings above should be \"aba\", \", and \"bababc\".")
