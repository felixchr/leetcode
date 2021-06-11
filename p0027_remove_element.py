class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        l = len(nums)
        while val in nums:
            nums.pop(nums.index(val))
            l -= 1
        return l
        
