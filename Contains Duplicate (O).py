class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
    
#counter counts each occurrence, which is not needed since we only need to know if there is a duplicate or not. Using set() will remove duplicates and we can compare the length of the original list with the length of the set. If they are not equal, it means there was at least one duplicate in the original list.