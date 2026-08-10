class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while True:
            k = numbers[i] + numbers[j]
            if k == target:
                return [i,j]
            elif k < target:
                i += 1
                continue

            elif k > target:
                j -= 1
                continue