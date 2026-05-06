class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tab = set()
        for num in nums:
            if num not in tab:
                tab.add(num)
            else:
                return True
        return False