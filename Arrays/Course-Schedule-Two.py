"""
There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if 
prerequisites[i] = [ai, bi] this means you must take the course bi before 
the course ai. Given the total number of courses numCourses and a list of 
the prerequisite pairs, return the ordering of courses you should take to 
finish all courses. If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.
"""


def findOrder(numCourses: int, prerequisites: List[List[int]]):
    needed = [set() for _ in range(numCourses)]
    rely = [[] for _ in range(numCourses)]
    for prereq in prerequisites:
        needed[prereq[0]].add(prereq[1])
        rely[prereq[1]].append(prereq[0])
    ans, curr = [], [i for i in range(numCourses) if not needed[i]]
    while curr:
        temp = []
        for i in curr:
            ans.append(i)
            for j in rely[i]:
                needed[j].remove(i)
                if not needed[j]:
                    curr.append(j)
        curr = temp
    return ans if len(ans) == numCourses else []


print(findOrder(2, [[1, 0]]))
print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(findOrder(1, []))
print("The arrays above should be [0, 1], [0, 2, 1, 3], and [0].")
