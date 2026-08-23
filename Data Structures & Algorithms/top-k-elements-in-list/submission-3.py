import collections 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            if n not in m.keys():
                m[n] = 0
            m[n] = m[n] + 1
    
        m2 = {}
        for k1, v in m.items():
            if v not in m2.keys():
                m2[v] = [k1]
            else:
                m2[v].append(k1)
        od = collections.OrderedDict(sorted(m2.items()))

        res = []
        for o in od.values():
            res.extend(o)

        return res[::-1][:k]
        