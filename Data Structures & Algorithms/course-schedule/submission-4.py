class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        visiting = set()
        visited = set()

        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            for ne in graph[i]:
                if not dfs(ne):
                    return False
            visiting.remove(i)
            visited.add(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 