class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            l = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:l] == word2:
                return ""
            for j in range(l):
                if word1[j] != word2[j]:
                    graph[word2[j]].add(word1[j])
                    break
        res = []
        visited = {}
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in graph[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)
        for c in graph:
            if dfs(c):
                return ""
        return "".join(res)