import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        ans = []
        heapq.heapify(ans)
        for num, freq in counts.items():
            heapq.heappush(ans,[freq,num])
            if len(ans) > k:
                heapq.heappop(ans)
        return [i[1] for i in ans]