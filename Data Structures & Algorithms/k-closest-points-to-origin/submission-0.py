from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data = [[-sqrt(point[0]**2 + point[1]**2),point] for point in points]
        heapq.heapify(data)
        while len(data) > k:
            heapq.heappop(data)
        return [x[1] for x in data]