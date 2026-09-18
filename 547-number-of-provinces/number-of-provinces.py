class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # n = len(isConnected)
        # visited = [False]*n
        # provinces = 0

        # def dfs(city):
        #     visited[city] = True

        #     for i in range(n):
        #         if isConnected[city][i] == 1 and not visited[i]:
        #             dfs(i)

        # for i in range(n):
        #     if not visited[i]:
        #         provinces += 1
        #         dfs(i)

        # return provinces

        n = len(isConnected)
        visited = [False]*n
        prov = 0

        def dfs(city):
            visited[city] = True

            for i in range(n):
                if isConnected[city][i] == 1 and not visited[i]:
                    dfs(i)


        for i in range(n):
            if not visited[i]:
                prov += 1
                dfs(i)

        return prov
        