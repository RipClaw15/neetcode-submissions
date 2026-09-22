class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        return len(list(nums)) != len(list(set(nums)))