class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        j = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                j += 1
            else:
                result = j if result < j else result
                j = 0
        result = j if result < j else result
        return result