class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_dict = Counter(s)
        t_dict = Counter(t)
        for i in s_dict:
            if s_dict[i] != t_dict[i] : return False
        return True
