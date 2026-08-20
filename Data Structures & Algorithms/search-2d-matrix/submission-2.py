class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        ncols = len(matrix[0])
        l = 0
        r = nrows * ncols - 1

        while l <= r:
          m = (l+r)//2
          pm = [m//ncols, m%ncols]
          pl = [l//ncols, l%ncols]  
          pr = [r//ncols, r%ncols]

          if matrix[pm[0]][pm[1]] == target:
            return True
          elif matrix[pm[0]][pm[1]] > target:
            r = m - 1
          else:
            l = m + 1
        return False