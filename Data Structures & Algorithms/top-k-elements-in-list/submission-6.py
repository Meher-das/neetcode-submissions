class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for num in nums:
            if num not in table.keys():
                table[num] = 1
            else:
                table[num] += 1

        arr = []
        for key,value in table.items():
            arr.append([value,key])
        arr.sort()

        sol = []
        k_val = k - 1
        while k_val != 0:
            sol.append(arr[k_val][1])
            k_val -= 1
        return sol
