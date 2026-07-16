class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        tMap={}
        n = len(s)
        for i in range(n):
            if t[i] in tMap: tMap[t[i]]+=1
            else: tMap[t[i]]=1
        for i in range(n):
            if s[i] in tMap: tMap[s[i]]-=1
            else: return False
        return not any(tMap.values())