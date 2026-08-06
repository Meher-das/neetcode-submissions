class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while True:
            currentsum = numbers[i] + numbers[j]
            if currentsum > target:
                j -= 1
            elif currentsum < target:
                i += 1
            else:
                return [i+1,j+1]