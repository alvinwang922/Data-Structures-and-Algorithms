"""
Given a characters array tasks, representing the tasks a CPU needs 
to do, where each letter represents a different task. Tasks could 
be done in any order. Each task is done in one unit of time. For 
each unit of time, the CPU could complete either one task or just 
be idle. However, there is a non-negative integer n that represents 
the cooldown period between two same tasks (the same letter in the 
array), that is that there must be at least n units of time between 
any two same tasks. Return the least number of units of times that 
the CPU will take to finish all the given tasks.
"""


from collections import Counter


def leastInterval(tasks: List[str], n: int):
    count = Counter(tasks)
    maxOccurrence = max(count.values())
    maxTask = 0
    for occurrence in count.values():
        if occurrence == maxOccurrence:
            maxTask += 1
    interval = maxOccurrence - 1
    middle = n - (maxTask - 1)
    empty = interval * middle
    remaining = len(tasks) - (maxOccurrence * maxTask)
    idle = max(0, empty - remaining)
    return len(tasks) + idle


print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(leastInterval(["A", "A", "A", "B", "B", "B"], 0))
print(leastInterval(["A", "A", "A", "A", "A",
                     "A", "B", "C", "D", "E", "F", "G"], 2))
print("The values above should be 8, 6, and 16.")
