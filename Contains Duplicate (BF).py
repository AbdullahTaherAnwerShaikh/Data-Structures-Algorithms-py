class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict=Counter(nums)
        for i in numsDict:
            if numsDict[i]>1: return True
        return False
    
#Counter counts each occurrence and makes a dictionary of the numbers and their counts. We can iterate through the dictionary and check if any number has a count greater than 1, which would indicate a duplicate. If we find such a number, we return True. If we finish checking all numbers and find no duplicates, we return False.