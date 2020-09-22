"""
You are given a data structure of employee information, which includes the 
employee's unique id, their importance value and their direct subordinates' id.
For example, employee 1 is the leader of employee 2, and employee 2 is the 
leader of employee 3. They have importance value 15, 10 and 5, respectively. 
Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has 
[2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 
is also a subordinate of employee 1, the relationship is not direct.
Now given the employee information of a company, and an employee id, you need 
to return the total importance value of this employee and all their subordinates.
"""


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int):
        relations = dict()
        for employee in employees:
            relations[employee.id] = employee.subordinates
        relevant = {id}
        self.recurse(relations, id, relevant)
        total = 0
        for employee in employees:
            if employee.id in relevant:
                total += employee.importance
        return total

    def recurse(self, relations, id, relevant):
        for employee in relations[id]:
            relevant.add(employee)
            self.recurse(relations, employee, relevant)


print(getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1))
print(getImportance([[1, 2, [2]], [2, 3, []]], 2))
print("The value above should be 11 and 3.")
