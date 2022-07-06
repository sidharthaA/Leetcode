class Solution:
    def canFinish(self, numCourses: int,  prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        vis = []
        def dfs(cur):
            if cur in vis: return False
            if adj[cur] == []: return True
            vis.append(cur)
            for crs in adj[cur]:
                if not dfs(crs): return False
            vis.remove(cur)
            adj[cur] = []
            
            return True
        for i in range(numCourses): 
            if not dfs(i): return False
        return True