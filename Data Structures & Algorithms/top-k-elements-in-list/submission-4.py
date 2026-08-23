class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        return [t[0] for t in c.most_common(k)]