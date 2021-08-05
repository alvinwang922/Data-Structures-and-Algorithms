"""
Implement the StreamChecker class as follows:
StreamChecker(words): Constructor, init the data structure with 
the given words.
query(letter): returns true if and only if for some k >= 1, the 
last k characters queried (in order from oldest to newest, 
including this letter just queried) spell one of the words 
in the given list.
"""


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.waitlist = []
        self.trie = dict()
        for word in words:
            temp_dict = self.trie
            for letter in word:
                temp_dict = temp_dict.setdefault(letter, dict())
            temp_dict["end"] = "end"

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        curr_waitlist = []
        if letter in self.trie:
            curr_waitlist.append(self.trie[letter])
        for item in self.waitlist:
            if letter in item:
                curr_waitlist.append(item[letter])
        self.waitlist = curr_waitlist
        return any("end" in item for item in self.waitlist)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

"""
Commands: ["StreamChecker","query","query","query","query","query",\
    "query","query","query","query","query","query","query"]
Arguments: [[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],\
    ["g"],["h"],["i"],["j"],["k"],["l"]]
Output: [None,False,False,False,True,False,True,False,False,False,\
    False,False,True]
"""
