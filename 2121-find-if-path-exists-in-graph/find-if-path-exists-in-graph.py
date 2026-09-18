class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adjList = [[] for _ in range(n)]

        for s,d in edges:
            adjList[s].append(d)
            adjList[d].append(s)

        visited = [False]*n

        def dfs(v):
            if v == destination:
                return True

            visited[v] = True

            for neighbour in adjList[v]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True

            return False
        
        return dfs(source)

        