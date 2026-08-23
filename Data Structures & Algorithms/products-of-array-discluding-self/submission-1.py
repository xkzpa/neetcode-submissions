class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s, zero_cnt = 1, 0
        for n in nums:
            if n:
                s *= n
            else:
                zero_cnt +=1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, n in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if n else s
            else:
                res[i] = s // n
        return res