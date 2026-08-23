class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = 0
        right_max = 0
        prefix = [0] * n
        suffix = [0] * n
        water = [0] * n
        
        for i in range(1,n):
            left_max = max(left_max, height[i-1])
            prefix[i] = left_max
            right_max = max(right_max,height[n-i])
            suffix[n-i-1] = right_max
        
        for i in range(n):
            water[i] = max(min(suffix[i],prefix[i]) - height[i],0)

        return sum(water)