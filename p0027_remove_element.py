class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        i = 0
        l = len(nums)
        while i < len(nums):
            element = nums[i]
            if element == val:
                nums.pop(i)
                l -= 1
            elif element < val:
                i += 1
            else:
                break
        return l
        
