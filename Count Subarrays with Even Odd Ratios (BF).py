class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        even,odd,result =0,0,0
        n = len(nums)

        for i in range(n):
            even = 0
            odd = 0
            for j in range(i,n):
                if (nums[j] % 2) == 1 :
                    odd += 1
                else:
                    even += 1
                if (odd > 0):
                    if even * b <= odd * a:
                        result += 1
        return result