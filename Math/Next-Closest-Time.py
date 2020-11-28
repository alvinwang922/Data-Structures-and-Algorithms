"""
Given a time represented in the format "HH:MM", form the next 
closest time by reusing the current digits. There is no limit 
on how many times a digit can be reused. You may assume the 
given input string is always valid. For example, "01:34", 
"12:09" are all valid. "1:34", "12:9" are all invalid.
"""


class Solution:
    def nextClosestTime(self, time: str):
        hour, minute = time.split(":")
        nums = sorted(set(hour + minute))
        possible = []
        for i in nums:
            for j in nums:
                possible.append(i + j)
        i = possible.index(minute)
        if i + 1 < len(possible) and possible[i + 1] < "60":
            return hour + ":" + possible[i + 1]
        i = possible.index(hour)
        if i + 1 < len(possible) and possible[i + 1] < "24":
            return possible[i + 1] + ":" + possible[0]
        return possible[0] + ":" + possible[0]

    print(nextClosestTime("19:34"))
    print(nextClosestTime("23:59"))
    print(nextClosestTime("13:55"))
    print("The strings above should be \"19:39\", \"23.59\", and \"15:11\".")
