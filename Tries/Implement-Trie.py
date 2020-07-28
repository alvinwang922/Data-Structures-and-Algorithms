# Implement a trie with insert, search, and startsWith methods.


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str):
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t["end"] = "end"

    def search(self, word: str):
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for char in word:
            if char not in t:
                return False
            t = t[char]
        if "end" in t:
            return True
        return False

    def startsWith(self, prefix: str):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for char in prefix:
            if char not in t:
                return False
            t = t[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

print("Input of /"["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
      [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]/" should result in an output of \
        /"[None, None, True, False, True, None, True]/".")
