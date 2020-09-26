"""
Sometimes people repeat letters to represent extra feeling, such as 
"hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like 
"heeellooo", we have groups of adjacent letters that are all the same:  
"h", "eee", "ll", "ooo". For some given string S, a query word is 
stretchy if it can be made to be equal to S by any number of 
applications of the following extension operation: choose a group 
consisting of characters c, and add some number of characters c to 
the group so that the size of the group is 3 or more.
For example, starting with "hello", we could do an extension on the 
group "o" to get "hellooo", but we cannot get "helloo" since the group 
"oo" has size less than 3.  Also, we could do another extension like 
"ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the 
query word "hello" would be stretchy because of these two extension 
operations: query = "hello" -> "hellooo" -> "helllllooo" = S.
Given a list of query words, return the number of words that are stretchy. 
"""


class Solution:
    def expressiveWords(self, S: str, words: List[str]):

        def compress(word):
            compressed, count = [], []
            for char in word:
                if not compressed or compressed[-1] != char:
                    compressed.append(char)
                    count.append(1)
                else:
                    count[-1] += 1
            return compressed, count

        S_compressed, S_count = compress(S)
        ans = 0
        for word in words:
            stretch = True
            compressed, count = compress(word)
            if S_compressed != compressed:
                stretch = False
                break
            for i in range(len(S_compressed)):
                if S_count[i] < 3 and S_count[i] != count[i]:
                    stretch = False
                if S_count[i] >= 3 and S_count[i] < count[i]:
                    stretch = False
            if stretch:
                ans += 1
        return ans


print(expressiveWords("heeellooo", ["hello", "hi", "helo"]))
print(expressiveWords("dddiiiinnssssssoooo", ["dinnssoo", "ddinso", "ddiinnso", \
    "ddiinnssoo", "ddiinso", "dinsoo", "ddiinsso", "dinssoo", "dinso"]))
print(expressiveWords("abcd", ["abc"]))
print("The values above should be 1, 3, and 0.")
