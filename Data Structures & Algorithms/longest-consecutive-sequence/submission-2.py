class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        num_starts_seq = set()
        
        for num in nums:
            num_set.add(num)
        
        for num in nums:
            if num - 1 not in num_set:
                num_starts_seq.add(num)
        
        
        if len(nums) == 0:
            max_seq_len = 0
        else:
            max_seq_len = 1

        for number in num_starts_seq:
            seq_len = 1
            while True:
                next_number = number + 1
                if next_number in num_set:
                    seq_len += 1
                else:
                    break

            if max_seq_len < seq_len:
                max_seq_len = seq_len
            
        return max_seq_len