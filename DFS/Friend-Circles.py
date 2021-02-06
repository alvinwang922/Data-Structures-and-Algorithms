"""
There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct friend 
of B, and B is a direct friend of C, then A is an indirect friend of C. And we 
defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the 
class. If M[i][j] = 1, then the ith and jth students are direct friends with each 
other, otherwise not. And you have to output the total number of friend circles 
among all the students.
"""


class Solution:
    def findCircleNum(self, M: List[List[int]]):
        tracker = defaultdict(list)
        for i in range(len(M)):
            for j in range(i + 1, len(M[0])):
                if M[i][j] == 1:
                    tracker[i].append(j)
                    tracker[j].append(i)

        network = [False] * len(M)

        def dfs(friends):
            for friend in friends:
                if network[friend] == False:
                    network[friend] = True
                    dfs(tracker[friend])

        circles = 0
        for i in range(len(network)):
            if network[i] == False:
                circles += 1
                network[i] = True
                dfs(tracker[i])

        return circles

    print(findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    print(findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    print("The values above should be 2, 1, and 3.")
