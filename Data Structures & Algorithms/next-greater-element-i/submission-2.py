class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums1)
        m = {}
        for i,n in enumerate(nums2):
            while stack and n > stack[-1][0]:
                t, inx = stack.pop()
                m[nums2[inx]] = n
            stack.append((n,i))
        
        for i, n in enumerate(nums1):
            if n in m:
                result[i] = m.get(n)
        
        return result