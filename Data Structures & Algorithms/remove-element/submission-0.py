class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        inx_to_remove = []
        for i in range(len(nums)):
            if nums[i] == val:
                inx_to_remove.append(i)
        j = 0
        for i in inx_to_remove:
            nums.pop(i-j)
            j+=1
        return len(nums)