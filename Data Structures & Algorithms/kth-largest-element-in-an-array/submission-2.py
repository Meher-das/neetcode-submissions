import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newarr = [-num for num in nums]
        heapq.heapify(newarr)
        l = len(nums)
        while len(newarr) > l-k+1:
            heapq.heappop(newarr)
        # print(newarr)
        return -newarr[0]
        