class Solution:

    def __init__(self):
        self.islands = 0
        self.visited = set()

    def bfs(self,pos):
        stack = []
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for direction in directions:
            n_pos = [pos[0]+direction[0], pos[0]+direction[1]]
            if n_pos not in self.visited and grid[n_pos[0],n_pos[1]] == '1' and n_pos[0] > 0 and n_pos[0] < len(grid[0]) and n_pos[1] > 0 and n_pos[1] < len(grid):
                stack.append(n_pos)
                visted.add(n_pos)
        
        while stack:
            bfs(stack.pop())

    def numIslands(self, grid: List[List[str]]) -> int:

        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[i][j] == '1':
                    self.visited.add(grid[i][j])
                    self.bfs([i,j])
                    self.islands += 1
        
        return self.islands