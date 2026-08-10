class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for num in nums:
            table[num] = 1 + table.get(num,0)
        
        arr = []
        for key,value in table.items():
            arr.append([value,key])
        arr.sort()

        sol = []
        k_val = k
        while k_val != 0:
            k_val -= 1
            sol.append(arr[k_val][1])
        return sol
