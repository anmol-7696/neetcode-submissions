from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n -1 :
            return False

        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(c):
            visit.add(c)

            for nei in adj[c]:
                if nei not in visit:
                    dfs(nei)     
         
        dfs(0)
        return len(visit) == n
        
