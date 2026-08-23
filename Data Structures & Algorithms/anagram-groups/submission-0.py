class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {} 
        for s in strs:
            s1 = ''.join(sorted(s))
            if s1 in m.keys():
                tmp = m.get(s1)
                tmp.append(s)
                m[s1] = tmp
            else:
                m[s1] = [s]
        # return m.values()
        
        return list(m.values())