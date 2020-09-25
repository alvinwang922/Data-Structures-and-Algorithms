"""
You have a lock in front of you with 4 circular wheels. Each wheel 
has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example we can 
turn '9' to be '0', or '0' to be '9'. Each move consists of turning 
one wheel one slot. The lock initially starts at '0000', a string 
representing the state of the 4 wheels. You are given a list of 
deadends dead ends, meaning if the lock displays any of these codes, 
the wheels of the lock will stop turning and you will be unable to 
open it. Given a target representing the value of the wheels that 
will unlock the lock, return the minimum total number of turns 
required to open the lock, or -1 if it is impossible.
"""


class Solution:
    def openLock(self, deadends: List[str], target: str):
        depth = -1
        visited, q = set(deadends), deque(["0000"])
        while q:
            depth += 1
            for _ in range(len(q)):
                elem = q.popleft()
                if elem == target:
                    return depth
                if elem in visited:
                    continue
                visited.add(elem)
                q.extend(self.next(elem))
        return -1

    def next(self, elem):
        res = []
        for i, num in enumerate(elem):
            num = int(num)
            res.append(elem[:i] + str((num - 1) % 10) + elem[i + 1:])
            res.append(elem[:i] + str((num + 1) % 10) + elem[i + 1:])
        return res


print(openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
print(openLock(["8888"], "0009"))
print(openLock(["8887", "8889", "8878", "8898",
                "8788", "8988", "7888", "9888"], "8888"))
print(openLock(["0000"], "8888"))
print("The values above should be 6, 1, -1, and -1.")
