class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        result = []
        while q:
            course = q.popleft()
            result.append(course)
            for ne in graph[course]:
                indegree[ne] -= 1
                if indegree[ne] == 0:
                    q.append(ne)
        return result if len(result)==numCourses else []