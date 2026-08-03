class Solution:
    def countValidPrefixes(self, s: str) -> int:
        ans, count, count1 = 0,0,0
        for char in s:
            if char == "0":
                count+=1
            else:
                count1+=1
            if abs(count - count1) <= 1:
                ans += 1
        return ans