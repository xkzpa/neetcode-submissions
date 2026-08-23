class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            if target - nums[i] in m.keys():
                return [m[target - nums[i]], i]
            else:
                m[nums[i]] = i
        return None