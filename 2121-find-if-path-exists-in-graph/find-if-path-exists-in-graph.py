class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = [False]*n
        q = deque([source])
        vis[source] = True

        while q:
            u = q.popleft()
            if u == destination:
                return True
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    q.append(v)

        return False

        
        