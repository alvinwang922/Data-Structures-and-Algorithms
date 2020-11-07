"""
You are given an array A representing heights of students. 
All the students are asked to stand in rows. The students 
arrive by one, sequentially (as their heights appear in A). 
For the i-th student, if there is a row in which all the 
students are taller than A[i], the student will stand in 
one of such rows. If there is no such row, the student will 
create a new row. Your task is to find the minimum number of 
rows created.
"""


def solution(A):
    if not A:
        return 0
    ans = 1
    tracker = {0: A[0]}
    for num in A[1:]:
        added = False
        for i in range(ans):
            if num < tracker[i]:
                tracker[i] = num
                added = True
                break
        if not added:
            tracker[ans] = num
            ans += 1
    return ans


print(solution([5, 4, 3, 6, 1]))
print(solution([1, 2, 3]))
print(solution([3, 2, 4, 1, 3]))
print("The values above should be 2, 3, and 2.")
