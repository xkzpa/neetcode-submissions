class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums) - 1
        l = 0 

        while l <= h:
            c = (l+h) // 2
            print(c)
            if nums[c] < target:
                l = c+1
            if nums[c] > target:
                h = c-1
            if nums[c] == target:
                return c
        return -1