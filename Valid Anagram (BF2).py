class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        alpha = [0] * 26
        n = len(s)
        for i in range(n):
            alpha[ord(s[i]) - ord('a')] += 1
            alpha[ord(t[i]) - ord('a')] -= 1
        for check in alpha:
            if check != 0: return False
        return True