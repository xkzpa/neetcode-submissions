class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        positions = {}
        result = [-1] * len(nums1)
        for i,n in enumerate(nums2):
            positions[n] = i
        
        for indx, n in enumerate(nums1):
            if n in positions:
                for i in range(positions[n], len(nums2)):
                    if n < nums2[i]:
                        result[indx] = nums2[i]
                        break                                
        return result