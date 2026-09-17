from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        m = len(grid) # row count
        n = len(grid[0]) # col count
        rotten_fruits = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_fruits.append([i,j])
    
        t = 0 
        while rotten_fruits:
            new_queue = deque(rotten_fruits)
            rotten_fruits = deque([])
            while new_queue:
                rotten = new_queue.popleft()
                for direc in directions:
                    newpoint = [rotten[0]+direc[0], rotten[1]+direc[1]]
                    if 0 <= newpoint[0] < m and 0 <= newpoint[1] < n and grid[newpoint[0]][newpoint[1]] == 1:
                        grid[newpoint[0]][newpoint[1]] = 2
                        rotten_fruits.append(newpoint)
            t += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return t-1 if t > 0 else 0
            

        
