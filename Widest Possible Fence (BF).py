class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        cnt = Counter(planks)
        final = Counter(planks)
        
        for a,b in combinations(cnt.keys(),2):
            final[a+b] += min(cnt[a],cnt[b])
        for a in cnt:
            final[a*2] += cnt[a] // 2
        return max(final.values())