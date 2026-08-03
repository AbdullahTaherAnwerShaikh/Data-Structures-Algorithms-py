class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        limit = min(5, len(nums))
        
        for i in range(limit):
            for j in range(i + 1, len(nums)):
                strength = (nums[i] * nums[j]) // (math.gcd(nums[i], nums[j]) ** 2)
                ans = max(ans,strength)
                    
        return ans