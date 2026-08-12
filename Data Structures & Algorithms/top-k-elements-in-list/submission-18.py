import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if not num in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        array = [[-value, key] for key, value in hashmap.items()]
        heapq.heapify(array)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(array)[1])
        return result



