"""
On a single-threaded CPU, we execute a program containing n 
functions. Each function has a unique ID between 0 and n-1.
Function calls are stored in a call stack: when a function 
call starts, its ID is pushed onto the stack, and when a 
function call ends, its ID is popped off the stack. The 
function whose ID is at the top of the stack is the current 
function being executed. Each time a function starts or ends, 
we write a log with the ID, whether it started or ended, and 
the timestamp. You are given a list logs, where logs[i] 
represents the ith log message formatted as a string 
"{function_id}:{"start" | "end"}:{timestamp}". For example, 
"0:start:3" means a function call with function ID 0 started 
at the beginning of timestamp 3, and "1:end:2" means a function 
call with function ID 1 ended at the end of timestamp 2. Note 
that a function can be called multiple times, possibly recursively.
A function's exclusive time is the sum of execution times for all 
function calls in the program. For example, if a function is called 
twice, one call executing for 2 time units and another call executing 
for 1 time unit, the exclusive time is 2 + 1 = 3. Return the exclusive 
time of each function in an array, where the value at the ith index 
represents the exclusive time for the function with ID i.
"""


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]):
        ans = [0] * n
        stack = []
        prevTime = 0
        for log in logs:
            func, word, time = log.split(":")
            func, time = int(func), int(time)
            if word == "start":
                if stack:
                    ans[stack[-1]] += time - prevTime
                stack.append(func)
                prevTime = time
            else:
                ans[stack.pop()] += time - prevTime + 1
                prevTime = time + 1
        return ans


print(exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
print(exclusiveTime(1, ["0:start:0", "0:start:2",
                        "0:end:5", "0:start:6", "0:end:6", "0:end:7"]))
print(exclusiveTime(2, ["0:start:0", "0:start:2",
                        "0:end:5", "1:start:6", "1:end:6", "0:end:7"]))
print("The arrays above should be [3, 4], [8], and [7, 1].")
