class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numDic = {}
        for i in range(len(nums)):
            if nums[i] in numDic:
                comp=i-numDic[nums[i]]
                if comp<=k : return True
            numDic[nums[i]]=i
        return False