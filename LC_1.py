class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(0,len(nums)):
            curr = nums[x]
            if target-curr in nums[x+1:]:
                break
        for y in range(x+1,len(nums)):
            if nums[y] == target-nums[x]:
                break
        ans = []
        ans.append(x)
        ans.append(y)
        return ans
        