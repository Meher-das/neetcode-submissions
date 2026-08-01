class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        stack = []
        traversed_map = set()
        n,m = len(grid), len(grid[0])
        def dfs(point):
            area = 0
            traversed_map.add((point[0],point[1]))
            stack.append([point[0],point[1]])
            directions = ((0,1),(0,-1),(1,0),(-1,0))
            while stack:
                x,y = stack.pop()
                area += 1
                for d in directions:
                    x_new, y_new = x+d[0], y+d[1]
                    if 0 <= x_new < n and 0 <= y_new < m and grid[x_new][y_new] == 1 and (x_new, y_new) not in traversed_map:
                        stack.append([x_new,y_new])
                        traversed_map.add((x_new,y_new))
            return area

        for i in range(n):
            for j in range(m):
                if (i,j) not in traversed_map and grid[i][j] == 1:
                    area = dfs([i,j])
                    max_area = max(max_area, area)
        return max_area
        