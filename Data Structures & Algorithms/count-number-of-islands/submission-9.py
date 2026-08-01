class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        traversed_map = set()
        islandcount = 0
        n, m = len(grid), len(grid[0])
        stack = []
        def dfs(point):
            i,j = point
            stack.append([i,j])
            directions = ((0,1),(0,-1),(1,0),(-1,0))
            while stack:
                x,y = stack.pop()
                traversed_map.add((x,y))
                for direction in directions:
                    x_new, y_new = x+direction[0], y+direction[1]
                    if 0 <= x_new < n and 0 <= y_new < m and (x_new,y_new) not in traversed_map and grid[x_new][y_new] == "1":
                        stack.append([x_new,y_new])
                        # dfs((x_new,y_new))


        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in traversed_map:
                    dfs((i,j))
                    islandcount += 1
        return islandcount
        
