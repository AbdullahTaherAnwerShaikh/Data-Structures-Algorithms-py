class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        strDic = {}
        for i in strs:
            temp = "".join(sorted(i))
            if temp in strDic:
                ans[strDic[temp]].append(i)
            else:
                strDic[temp]=len(ans)
                ans.append([i])
        return ans