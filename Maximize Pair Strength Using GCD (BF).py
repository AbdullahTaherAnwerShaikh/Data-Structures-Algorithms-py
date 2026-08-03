class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        res = 0
        curr = 0
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                curr = (nums[i] * nums[j]) // math.gcd(nums[i], nums[j]) ** 2
                res = max(curr,res)
        return res