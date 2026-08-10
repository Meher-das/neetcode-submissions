# from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        traversed = set()
        n = len(grid)
        m = len(grid[0])

        def minDist(point):
            directions = ((0,-1),(0,1),(1,0),(-1,0))
            mindist = grid[point[0]][point[1]]
            # traversed.add(point)
            for d in directions:
                npoint = (point[0]+d[0],point[1]+d[1])
                if not (0 <= npoint[0] < n) or not (0 <= npoint[1] < m) or npoint in traversed:
                    continue
                if grid[npoint[0]][npoint[1]] == 0:
                    dist = 1
                elif grid[npoint[0]][npoint[1]] > 0:
                    minDist(npoint)
                    dist = grid[npoint[0]][npoint[1]] + 1
                elif grid[npoint[0]][npoint[1]] == -1:
                    continue
                # traversed.add(npoint)
                mindist = min(dist,mindist)
            grid[point[0]][point[1]] = mindist
        
        for i in range(n):
            for j in range(m):
                minDist((i,j))