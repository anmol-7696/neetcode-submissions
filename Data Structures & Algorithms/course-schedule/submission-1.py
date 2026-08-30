from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[u].append[v]
        
        def isCycle(courseNum, seen):
            if courseNum in seen:
                return True
            seen.add(courseNum)
            for p in graph[courseNum]:
                if isCycle(p, seen):
                    return True
            graph[courseNum] = []
            seen.remove(courseNum)
            return False

        seen = set()
        for i in range(numCourses):
            if isCycle(i,seen):
                return False
        return True