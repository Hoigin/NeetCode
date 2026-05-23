class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        visiting = set()
        visited = set()
        res = []

        def dfs(i):
            # 当前递归路径中再次出现 => 有环
            if i in visiting:
                return False
            # 已经确认无环
            if i in visited:
                return True
            # 进入当前路径
            visiting.add(i)
            for ne in graph[i]:
                if not dfs(ne):
                    return False
            # 离开当前路径
            visiting.remove(i)
            # 标记已检查
            visited.add(i)
            # 添加到上课序列中
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res