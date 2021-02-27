"""
In a town, there are N people labelled from 1 to N. There
is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b]
representing that the person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of
the town judge.  Otherwise, return -1.
"""


class Solution(object):
    def findJudge(self, N, trust):
        if len(trust) == 1:
            return trust[0][1]
        isTownJudge = [True] * N
        for i in range(len(trust)):
            isTownJudge[trust[i][0] - 1] = False
        counter = 0
        for j in range(len(isTownJudge)):
            if isTownJudge[j] == True:
                for k in range(len(trust)):
                    if trust[k][1] == j + 1:
                        counter += 1
                if counter == N - 1:
                    return j + 1
        return -1

    print(findJudge(2, [[1, 2]]))
    print(findJudge(3, [[1, 3], [2, 3]]))
    print(findJudge(3, [[[1, 3], [2, 3], [3, 1]]]))
    print(findJudge(3, [[1, 2], [2, 3]]))
    print(findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
    print("The values above should be 2, 3, -1, -1, and 3")
