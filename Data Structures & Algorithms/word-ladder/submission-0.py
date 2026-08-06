class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        res = 0
        q = deque([beginWord])
        visited = {beginWord}
        while q:
            res += 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return res
                for i in range(len(curr)):
                    for c in range(97, 123):
                        if chr(c) == curr[i]:
                            continue
                        word = curr[:i] + chr(c) + curr[i+1:]
                        if word in words and word not in visited:
                            visited.add(word)
                            q.append(word)
        return 0