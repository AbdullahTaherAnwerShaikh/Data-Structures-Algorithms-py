class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix=nums[0]
        i = 1
        while i<len(nums) and nums[i]==nums[i-1]+1:
            prefix += nums[i]
            i+=1
        while prefix in nums:
            prefix+=1
        return prefix