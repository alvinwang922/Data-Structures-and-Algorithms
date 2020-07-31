"""
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" 
cells are those horizontally or vertically neighboring. The same letter cell may not be 
used more than once in a word.
"""


class Node:
    def __init__(self):
        self.word = ""
        self.children = defaultdict(Node)


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]):
        if not board:
            return None
        trie = Trie()
        for word in words:
            trie.add(word)
        res, self.rows, self.cols = [], len(board), len(board[0])
        for i, line in enumerate(board):
            for j, c in enumerate(line):
                if c in trie.root.children:
                    res = self.dfs(board, trie.root.children[c], i, j, res)
        return res

    def dfs(self, board, node, x, y, res):
        if node.word:
            res.append(node.word)
            node.word = ""
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        curr, board[x][y] = board[x][y], "#"
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and board[nx][ny] in node.children:
                res = self.dfs(
                    board, node.children[board[nx][ny]], nx, ny, res)
        board[x][y] = curr
        return res
