class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # 在单词的结尾节点存储该单词

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        res = []
        m, n = len(board), len(board[0])

        def dfs(i, j, parent_node):
            char = board[i][j]
            curr_node = parent_node.children.get(char)
            if not curr_node:
                return
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None
            board[i][j] = '*'
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] != '*':
                    dfs(x, y, curr_node)
            board[i][j] = char
            if not curr_node.children:
                del parent_node.children[char]

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return res