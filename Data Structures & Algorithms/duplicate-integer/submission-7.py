class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for num in nums:
            if num not in hashTable.keys():
                hashTable[num] = 1
            else:
                return True
        return False