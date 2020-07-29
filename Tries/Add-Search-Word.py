"""
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string 
containing only letters a-z or .. A . means it can represent any one letter.
"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.WordDictionary = defaultdict(set)

    def addWord(self, word: str):
        """
        Adds a word into the data structure.
        """
        self.WordDictionary[len(word)].add(word)

    def search(self, word: str):
        """
        Returns if the word is in the data structure. A word could contain 
        the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        if "." not in word:
            return word in self.WordDictionary[len(word)]
        for w in self.WordDictionary[len(word)]:
            counter = 0
            for char in word:
                if char != "." and char != w[counter]:
                    break
                counter += 1
            else:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

operations = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search",
              "search", "search"]
inputs = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
print("Running the operations above on the inputs above, the booleans returned should be \
    [None, None, None, None, False, True, True, True].")
