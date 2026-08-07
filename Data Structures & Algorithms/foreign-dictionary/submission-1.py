class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        graph = defaultdict(list)
        characters = set()
        for word in words:
            for c in word:
                if c not in characters:
                    characters.add(c)
        for i in range(n):
            for j in range(i+1, n):
                word1, word2 = words[i], words[j]
                if word1[:len(word2)] == word2 and len(word1) > len(word2):
                    return ""
                l = min(len(word1), len(word2))
                for k in range(l):
                    if word1[k] == word2[k]:
                        continue
                    if word1[k] not in graph[word2[k]]:
                        graph[word2[k]].append(word1[k])
                    break
        visiting = set()
        visited = set()
        self.res = ""
        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True
            visiting.add(c)
            for pre in graph[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            visited.add(c)
            self.res += c
            return True
        for c in characters:
            if not dfs(c):
                return ""
        return self.res