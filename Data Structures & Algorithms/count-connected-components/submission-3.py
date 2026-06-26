class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()
        ans = 0

        def dfs(node):
            visit.add(node)
            for n in graph[node]:
                if n not in visit:
                    dfs(n)
        
        for i in range(n):
            if i not in visit:
                dfs(i)
                ans += 1
        
        return ans











