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
        for i in range(len(arr)-k,len(arr)-1):
            sol.append(arr[i][1])
        return sol

