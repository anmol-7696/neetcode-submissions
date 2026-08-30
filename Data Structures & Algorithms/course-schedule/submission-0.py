from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is my graph 
        prereqs = defaultdict(list)
        for u,v in prerequisites:
            prereqs[u].append(v)

        def isCycle(courseNum, seen):
            if courseNum in seen:
                return True
            seen.add(courseNum)
            for p in prereqs[courseNum]:
                if isCycle(p,seen):
                    return True
            prereqs[courseNum] = []
            seen.remove(courseNum)
            return False



        seen = set()
        for i in range(numCourses):
            if isCycle(i,seen):
                return False
        return True
