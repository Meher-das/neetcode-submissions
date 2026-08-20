import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        # print(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums) > self.k:
           heapq.heappop(self.nums)
        if not self.nums:
            return None
        return self.nums[0]
