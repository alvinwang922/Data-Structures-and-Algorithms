"""
You're given strings J representing the types of stones that are jewels, and S 
representing the stones you have.  Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str):
        jewels = set()
        counter = 0
        for char in J:
            jewels.add(char)
        for char in S:
            if char in jewels:
                counter += 1
        return counter


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))
print(numJewelsInStones("aA", "AaAaBbBAaaC"))
print("The numbers above should be 3, 0, 7.")
