class Solution:
    def bfs(pos):
        stack = []
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for direction in directions:
            n_pos = pos + direction

    def numIslands(self, grid: List[List[str]]) -> int:
        # islands = 0
        # visited = set()

        # for i in range(len(grid[0])):
        #     for j in range(len(grid)):
        #         if grid[i][j] == 1:
        #             visited.add(grid[i][j])
        #             bfs(grid[i][j])
        #             islands += 1
        print([0,1] + [1,0])
        