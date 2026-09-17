class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row1 = [1 for i in range(n)]
        row2 = [1 for i in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                row2[j] = row2[j-1] + row1[j]
            row1, row2 = row2, row1
        return row1[-1]