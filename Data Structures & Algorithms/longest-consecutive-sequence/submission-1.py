class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_seq = 1
        cur_seq = 1
        sort_nums = sorted(nums)
        prev = sort_nums[0]
        for i in sort_nums:
            if i - prev == 1:
                cur_seq += 1
            elif i - prev == 0:
                cur_seq = cur_seq
            else:
                cur_seq = 1
            prev = i
            if cur_seq > max_seq:
                max_seq = cur_seq
        return max_seq
            