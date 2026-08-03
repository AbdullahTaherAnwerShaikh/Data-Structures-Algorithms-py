class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        store = set(nums)
        res = 0
        for num in store:
            if (num-1) not in store:
                count =0
                curr = num
                while curr in store:
                    count += 1
                    curr += 1
                    res = max(res,count)
        return res